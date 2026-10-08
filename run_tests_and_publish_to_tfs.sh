export PYTHONPATH="/c/Users/Maxim.Gamov/PycharmProjects/r734_autotests"
cd $PYTHONPATH
pytest --alluredir allure-results --clean-alluredir ./tests/e2e/ --reruns=0 --slowmo 1000
allure generate allure-results -o allure-report --clean
allure generate --single-file allure-results -o "Z:/Maxim_Gamov/reports/$(date +%d.%m.%Y)" --clean
python publish_to_tfs.py
find /z/Maxim_Gamov/reports -mindepth 1 -type d -mtime +6 -exec rm -rf {} +