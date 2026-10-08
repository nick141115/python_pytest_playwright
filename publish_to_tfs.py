import glob
import json
import os
from datetime import datetime, timedelta, timezone

import requests
from requests.auth import HTTPBasicAuth

# TODO провести рефакторинг: разделить на большее количество функций и внедрить `if __name__ == "__main__":`
# Конфигурация
PROD_TFS_URL = "https://tfs.example.ru/tfs/exampletc1"
TEST_TFS_URL = "https://msk-tfs-tst-02.example-nt/tfs/exampletc1"
PROJECT = "DEP_PMO"
USERNAME = "Maxim.Gamov"
PAT = ""

ALLURE_RESULTS_DIR = r"allure-results"
ALLURE_REPORT_DIR = r".\allure-report"
ALLURE_REPORT_URL = f"file://example/Maxim_Gamov/reports/{datetime.now().strftime('%d.%m.%Y')}/index.html"
CERT_PATH = r"C:\EXAMPLE-ROOT-CA.crt"


def get_allure_report_title() -> str:
    """Чтение заголовка allure отчёта."""
    summary_path = os.path.join(ALLURE_REPORT_DIR, "widgets", "summary.json")

    if not os.path.exists(summary_path):
        raise RuntimeError("summary.json не найден. " "Убедитесь, что allure-report сгенерирован")

    with open(summary_path, encoding="utf-8") as f:
        summary = json.load(f)

    report_name = summary.get("reportName", "AllureReport")

    stop_ts = summary.get("time", {}).get("stop")
    if not stop_ts:
        raise RuntimeError("В summary.json отсутствует time.stop")

    report_date = datetime.fromtimestamp(stop_ts / 1000).strftime("%m/%d/%Y")

    return f"{report_name} {report_date}"


ALLURE_REPORT_TITLE = get_allure_report_title()

# Сопоставление статусов Allure с результатами TFS
STATUS_MAP = {
    "passed": "Passed",
    "failed": "Failed",
    "broken": "Failed",
    "skipped": "Failed",  # TFS не поддерживает отдельный skipped
}

# Сопоставление Allure severity с приоритетом TFS
SEVERITY_MAP = {
    "critical": 1,
    "normal": 2,
    "minor": 3,
    "trivial": 4,
}

# Создание Test Run'а
run_resp = requests.post(
    f"{TEST_TFS_URL}/{PROJECT}/_apis/test/runs?api-version=7.0",
    auth=HTTPBasicAuth(USERNAME, PAT),
    verify=CERT_PATH,
    json={
        "name": "Allure automated run",
        "isAutomated": True,
        "comment": f"**Просмотреть allure-отчёт за {datetime.now().strftime('%d.%m.%Y')}:**\n{ALLURE_REPORT_URL}",
    },
)
run_resp.raise_for_status()
run_id = run_resp.json()["id"]
print(f"Test Run создан: {run_id}")

# Экспорт результатов из Allure
results = []
files = glob.glob(os.path.join(ALLURE_RESULTS_DIR, "*-result.json"))
now = datetime.now(timezone.utc)

for file in files:  # noqa: C901
    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    title = data.get("name")
    status = data.get("status")

    if not title or status not in STATUS_MAP:
        continue

    outcome = STATUS_MAP[status]

    # Получение длительности
    duration_ms = 0
    if "time" in data and "duration" in data["time"]:
        duration_ms = data["time"]["duration"]
    elif "start" in data and "stop" in data:
        try:
            start_dt = datetime.fromtimestamp(int(data["start"]) / 1000)
            stop_dt = datetime.fromtimestamp(int(data["stop"]) / 1000)
            duration_ms = int((stop_dt - start_dt).total_seconds() * 1000)
        except Exception:
            duration_ms = 0

    start = now
    end = now + timedelta(milliseconds=duration_ms)

    # Приоритет и @allure.id
    priority = None
    allure_id = None
    for label in data.get("labels", []):
        lname = label.get("name", "").lower()
        if lname == "severity":
            priority = SEVERITY_MAP.get(label.get("value", "").lower())
        elif lname in {"as_id", "allure_id", "testid"}:
            allure_id = label.get("value")

    # Сообщение об ошибке
    error_message = None
    stack_trace = None
    if status in {"failed", "broken"}:
        details = data.get("statusDetails", {})
        error_message = details.get("message") or "Test failed"
        stack_trace = details.get("trace")

    # Формируем название с префиксом [@allure.id]
    display_title = f"[{allure_id}] {title}" if allure_id else title

    # Ссылка на тест-кейс в TFS
    testcase_url = None
    if allure_id:
        testcase_url_string = f"{PROD_TFS_URL}/{PROJECT}/_workitems/edit/{allure_id}"
        testcase_url = f"[{testcase_url_string}]({testcase_url_string})"

    result = {
        "state": "Completed",
        "outcome": outcome,
        "startedDate": start.isoformat() + "Z",
        "completedDate": end.isoformat() + "Z",
        "testCaseTitle": display_title,
        "automatedTestName": display_title,
        "automatedTestType": "pytest",
        "durationInMs": duration_ms,
    }

    if priority:
        result["priority"] = priority
    if error_message:
        result["errorMessage"] = error_message
    if stack_trace:
        result["stackTrace"] = stack_trace

    # Комментарий со ссылкой
    if testcase_url:
        result["comment"] = testcase_url

    results.append(result)

print(f"Сформировано результатов: {len(results)}")

if not results:
    raise RuntimeError("Нет данных Allure для загрузки")

# Отправка результатов в TFS
resp = requests.post(
    f"{TEST_TFS_URL}/{PROJECT}/_apis/test/runs/{run_id}/results?api-version=7.0",
    auth=HTTPBasicAuth(USERNAME, PAT),
    verify=CERT_PATH,
    json=results,
)
resp.raise_for_status()
print("Результаты загружены в Test Run")

# Переводим Test Run в статус complete
complete_resp = requests.patch(
    f"{TEST_TFS_URL}/{PROJECT}/_apis/test/runs/{run_id}?api-version=7.0",
    auth=HTTPBasicAuth(USERNAME, PAT),
    verify=CERT_PATH,
    json={
        "state": "Completed",
        "completedDate": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    },
)
complete_resp.raise_for_status()
print("Test Run автоматически завершён")
