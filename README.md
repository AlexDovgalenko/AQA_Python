### This is the Automation testing framework designed with educational matter based on Python 3.

## Latest Build status:

![CircleCI branch](https://img.shields.io/circleci/project/github/AlexDovgalenko/AQA_Python/master.svg?style=plastic)


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
python3 -v -m pytest -n 4 tests --alluredir ./reports
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
