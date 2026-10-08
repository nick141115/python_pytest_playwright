pytest -m "not multiple_streams" --alluredir allure-results --clean-alluredir ./tests/e2e/ --reruns=0 --numprocesses 1
pytest -m "multiple_streams" --alluredir allure-results ./tests/e2e/ --reruns=0 --numprocesses 15
allure generate --single-file allure-results -o allure-report-file --clean