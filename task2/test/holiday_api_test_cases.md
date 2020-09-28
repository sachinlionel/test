# HolidayAPi
Requires API_KEY

## List of Endpoints: 
- Countries: list & search countries with/without public holidays.
- Languages: list & search languages
- Holidays (restricted to one past year: 
    - List holidays by country, by year, by month, by day of month and search by name.
    - Get previous and upcoming holiday for give month and day
- Workday: list workdays in given start and end date

## Test Cases:

1. Generic `test.test_endpoints_status.py`
    1. Test each end point access
        - with valid API KEY - `automated`
        - with incorrect API KEY - `automated`
        - with wrong API KEY - `automated`
    2. Test Concurrent calls. - `automated`

2. Test Countries Endpoints: `test.test_countries.py`
    1. Test total count of countries. - `automated`
    2. Test total count of countries with public holidays.
        - with search valid country code - `automated`
        - with search invalid country code - `automated`
    3. Test search countries.
        - by name - `automated`
        - by country code - `automated`
        - by invalid name - `automated`
        - by numerical number - `automated`
    4. Test Post call. [Not Allowed]
    5. Test Patch call. [Not Allowed]
    6. Test Delete call. [Not Allowed]
  
2. Test Languages Endpoints: `not implemented`
    1. Test total count of Languages.
    3. Test search Languages.
        - by name
        - by languages code
        - by invalid name
        - by numerical number
    4. Test Post call. [Not Allowed]
    5. Test Patch call. [Not Allowed]
    6. Test Delete call. [Not Allowed]

3. Test Holidays Endpoints: `test.test_holidays.py`
    1. Test holdidays by country.
        - by year - `automated`
        - by month - `automated`
        - by year and month - `automated`
        - by year, month and day - `automated`
    2. Test search holidays (Min 5 chars).
        - by 1 chars - `automated`
        - by 4 chars - `automated`
        - by 5 chars - `automated`
        - by invalid name - `automated`
        - by invalid type, like integer - `automated`
    3. Test upcoming holiday for given date in a month.
        - present date - `automated`
        - future date - `automated`
        - past date - `automated`
        - date which is end of the year - `automated`
    4. Test previous holiday for given date in a month.
        - present date - `automated`
        - future date - `automated`
        - past date - `automated`
        - first day of the year - `automated`
    5. Test Post call. [Not Allowed]
    6. Test Patch call. [Not Allowed]
    7. Test Delete call. [Not Allowed]
    8. Test Limited acsess. - `automated`

4. Test Workday: `not implemeted`
    1. Test Workday for given start and end date.
    2. Test Workday for given start date only.
    2. Test Workday for given end date only.