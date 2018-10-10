### This is the Automation testing framework designed with educational matter based on Python 3.

## Pre-requisites:

Check python version
```
➜ python --version
Python 3.7.x
```

Prepare test environment on MAC
```
➜ brew install allure
➜ pip install -r py-requirements.txt
```


## Test execution:

To run tests manually need to run:
```
mkdir -p ./reports
python3 -m pytest  -n 4 tests/ui_tests/test_ui_jira_login.py --alluredir ./reports/
```

## Allure reporting:

To collect allure reports need to run: 
```
allure generate -c ./reports
```

To open reports run:
```
allure serve ./reports
```

## To delete python cache files need to run:
``` 
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```