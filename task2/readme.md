# Tests for https://holidayapi.com/

# Directory
<br>├── conf
<br>│   └── conf.json 
<br>├── readme.md
<br>├── pytest.ini
<br>├── run_test.py
<br>├── requirements.txt
<br>├── test
<br>│   ├── holiday_api_test_cases.md
<br>│   ├── test_countries.py
<br>│   ├── test_endpoints_status.py
<br>│   └── test_holidays.py
<br>└── utils
<br>    └── client.py
    
- `test` folder is for tests
- `utils` folder is for adding utils
- `conf` folder is for confidental items, like apikey, etc
- `test.holiday_api_test_cases.md` for test case reference
- `pytest.ini` to add custom markers
- `requirements.txt` to mention libraries required for tests

# Excute Tests
- `python run_test.py` to run whole suite
- `python run_test.py --smoke-test` to run smoke tests
- `python run_test.py --keyword {your_keyword}` to run selective tests
- Junit reports will be available at `task2/test.xml`

# TODO:
- Logging for better understanding and debugging failure.
- Load TestCases from json file 
- Encapsulate different response for better readability
