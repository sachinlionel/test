import pytest
from http import HTTPStatus
from task2.utils.client import APIClient, EndPoints
from collections import namedtuple

# test cases for querying holidays
holiday_test_case = namedtuple("holiday_test_case", "country_code, results_count, year, month, day, status_code")
holiday_test_cases = [
    holiday_test_case(country_code='IN', results_count=78, year=2019, month=None, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='AD', results_count=25, year=2019, month=None, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='BE', results_count=35, year=2019, month=None, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='IN', results_count=6, year=2019, month=1, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='AD', results_count=2, year=2019, month=1, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='BE', results_count=2, year=2019, month=1, day=None, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='IN', results_count=1, year=2019, month=1, day=1, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='AD', results_count=1, year=2019, month=1, day=1, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='BE', results_count=1, year=2019, month=1, day=1, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='IN', results_count=0, year=2019, month=1, day=11, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='AD', results_count=0, year=2019, month=1, day=11, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='BE', results_count=0, year=2019, month=1, day=11, status_code=HTTPStatus.OK),
    holiday_test_case(country_code='BE', results_count=0, year=2019, month=13, day=11, status_code=HTTPStatus.BAD_REQUEST),
    holiday_test_case(country_code='BE', results_count=0, year=2019, month=13, day=32, status_code=HTTPStatus.BAD_REQUEST),
]

# test cases for querying upcoming holiday
upcoming_holiday_test_case = namedtuple("upcoming_holiday_test_case", "country_code, expected_holiday_date, year, month, day, status_code")
upcoming_holiday_test_cases = [
    upcoming_holiday_test_case(country_code='IN', expected_holiday_date='2019-02-05', year=2019, month=1, day=31, status_code=HTTPStatus.OK),
    upcoming_holiday_test_case(country_code='AD', expected_holiday_date='2019-03-03', year=2019, month=2, day=1, status_code=HTTPStatus.OK),
    upcoming_holiday_test_case(country_code='BE', expected_holiday_date='2019-02-14', year=2019, month=1, day=10, status_code=HTTPStatus.OK),
    upcoming_holiday_test_case(country_code='AD', expected_holiday_date=None, year=2019, month=1, day=33, status_code=HTTPStatus.BAD_REQUEST),
    upcoming_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2019, month=13, day=-1, status_code=HTTPStatus.BAD_REQUEST),
    upcoming_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2019, month=-1, day=-2, status_code=HTTPStatus.BAD_REQUEST),
    upcoming_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2021, month=-1, day=2, status_code=HTTPStatus.PAYMENT_REQUIRED),
]

# test cases for querying previous holiday
previous_holiday_test_case = namedtuple("previous_holiday_test_case", "country_code, expected_holiday_date, year, month, day, status_code")
previous_holiday_test_cases = [
    previous_holiday_test_case(country_code='IN', expected_holiday_date='2019-01-26', year=2019, month=1, day=31, status_code=HTTPStatus.OK),
    previous_holiday_test_case(country_code='AD', expected_holiday_date='2019-01-06', year=2019, month=2, day=1, status_code=HTTPStatus.OK),
    previous_holiday_test_case(country_code='BE', expected_holiday_date='2019-01-06', year=2019, month=1, day=10, status_code=HTTPStatus.OK),
    previous_holiday_test_case(country_code='AD', expected_holiday_date=None, year=2019, month=1, day=33, status_code=HTTPStatus.BAD_REQUEST),
    previous_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2019, month=13, day=-1, status_code=HTTPStatus.BAD_REQUEST),
    previous_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2019, month=-1, day=-2, status_code=HTTPStatus.BAD_REQUEST),
    upcoming_holiday_test_case(country_code='BE', expected_holiday_date=None, year=2021, month=-1, day=2, status_code=HTTPStatus.PAYMENT_REQUIRED),
]

# test cases for searching holidays
search_holiday_test_case = namedtuple("search_holiday_test_case", "search_term, country_code, results_count, year, month, day, status_code")
search_holiday_test_cases = [
    search_holiday_test_case(search_term="republic", country_code='IN', results_count=1, year=2019, month=None, day=None, status_code=HTTPStatus.OK),
    search_holiday_test_case(search_term="republic", country_code='IN', results_count=1, year=2019, month=1, day=None, status_code=HTTPStatus.OK),
    search_holiday_test_case(search_term="republic", country_code='IN', results_count=0, year=2019, month=2, day=None, status_code=HTTPStatus.OK),
    search_holiday_test_case(search_term="republic", country_code='IN', results_count=1, year=2019, month=1, day=26, status_code=HTTPStatus.OK),
    search_holiday_test_case(search_term="republic", country_code='IN', results_count=0, year=2019, month=2, day=27, status_code=HTTPStatus.OK),
    search_holiday_test_case(search_term="republic", country_code='AD', results_count=None, year=2019, month=1, day=33, status_code=HTTPStatus.BAD_REQUEST),
    search_holiday_test_case(search_term="republic", country_code='BE', results_count=None, year=2019, month=13, day=-1, status_code=HTTPStatus.BAD_REQUEST),
    search_holiday_test_case(search_term="republic", country_code='BE', results_count=None, year=2019, month=-1, day=-2, status_code=HTTPStatus.BAD_REQUEST),
    search_holiday_test_case(search_term="republic", country_code='BE', results_count=None, year=2017, month=-1, day=2, status_code=HTTPStatus.PAYMENT_REQUIRED),

]


def get_holiday_test_case_name(test_case):
    """
    test name for holiday_test_case
    """
    name = f"country: {test_case.country_code}, year: {test_case.year} " \
           f"month: {test_case.month}, day: {test_case.day}, expected_hoildays_count: {test_case.results_count}, expected_status_code " \
           f"{test_case.status_code}"
    return name


def get_upcoming_holiday_test_case_name(test_case):
    """
    test name for upcoming_holiday_test_case
    """
    name = f"country: {test_case.country_code}, year: {test_case.year} " \
           f"month: {test_case.month}, day: {test_case.day}, and expected_hoilday_date: {test_case.expected_holiday_date}, expected_status_code " \
           f"{test_case.status_code}"
    return name


def get_previous_holiday_test_case_name(test_case):
    """
    test name for previous_holiday_test_case
    """
    name = f"country: {test_case.country_code}, year: {test_case.year} " \
           f"month: {test_case.month}, day: {test_case.day}, and expected_hoilday_date: {test_case.expected_holiday_date}, expected_status_code " \
           f"{test_case.status_code}"
    return name


def get_search_holiday_test_case_name(test_case):
    """
    test name for search_holiday_test_case
    """
    name = f"search_term: {test_case.search_term}, country_code: {test_case.country_code}, year: {test_case.year} " \
           f"month: {test_case.month}, day: {test_case.day}, expected_hoildays_count: {test_case.results_count}, with expected_status_code " \
           f"{test_case.status_code}"
    return name


class TestHolidays:

    @pytest.mark.smoke
    @pytest.mark.parametrize('test_case', holiday_test_cases, ids=get_holiday_test_case_name)
    def test_holidays_count(self, test_case):
        """
        test holidays per country, by year, by month, by day
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': test_case.country_code, 'year': test_case.year, 'month': test_case.month, 'day': test_case.day})
        assert response.code == test_case.status_code
        if test_case.status_code == HTTPStatus.OK:
            holidays = response.json_content['holidays']
            assert len(holidays) == test_case.results_count, "Mismatch in holidays count"

    @pytest.mark.smoke
    @pytest.mark.parametrize('test_case', upcoming_holiday_test_cases, ids=get_upcoming_holiday_test_case_name)
    def test_upcoming_holiday_for_given_date(self, test_case):
        """
        test upcoming holiday per country, by year, by month, by day
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': test_case.country_code,
                                      'year': test_case.year,
                                      'month': test_case.month,
                                      'day': test_case.day,
                                      'upcoming': True})
        assert response.code == test_case.status_code
        if test_case.status_code == HTTPStatus.OK:
            holidays = response.json_content['holidays']
            assert holidays[0]['date'] == test_case.expected_holiday_date, "Mismatch in exepcted holiday date"

    @pytest.mark.parametrize('test_case', previous_holiday_test_cases, ids=get_previous_holiday_test_case_name)
    def test_previous_holiday_for_given_date(self, test_case):
        """
        test previous holiday per country, by year, by month, by day
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': test_case.country_code,
                                      'year': test_case.year,
                                      'month': test_case.month,
                                      'day': test_case.day,
                                      'previous': True})
        assert response.code == test_case.status_code
        if test_case.status_code == HTTPStatus.OK:
            holidays = response.json_content['holidays']
            assert holidays[0]['date'] == test_case.expected_holiday_date, "Mismatch in exepcted holiday date"

    @pytest.mark.parametrize('test_case', previous_holiday_test_cases, ids=get_previous_holiday_test_case_name)
    def test_previous_upcoming_holiday_for_given_date(self, test_case):
        """
        Negative case
        test previous & upcoming holiday per country, by year, by month, by day
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': 'IN',
                                      'year': 2019,
                                      'month': 1,
                                      'day': 1,
                                      'previous': True,
                                      'upcoming': True})
        assert response.code == HTTPStatus.BAD_REQUEST, "Expected BAD_REQUEST"

    @pytest.mark.parametrize('test_case', search_holiday_test_cases, ids=get_search_holiday_test_case_name)
    def test_search_holiday_for_given_params(self, test_case):
        """
        test search holiday positive & negative cases. (Min 5 char is valid search term)
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': test_case.country_code,
                                      'year': test_case.year,
                                      'month': test_case.month,
                                      'day': test_case.day,
                                      'search': test_case.search_term})
        assert response.code == test_case.status_code
        if test_case.status_code == HTTPStatus.OK:
            holidays = response.json_content['holidays']
            assert len(holidays) == test_case.results_count, "Mismatch in holidays count"

    @pytest.mark.smoke
    def test_holidays_limited_access(self):
        """
        Negative case
        test limited access on endpoint, endpoint is limited is one past year
        """
        client = APIClient(EndPoints.holidays)
        response = client.get(params={'country': 'BE', 'year': 2018})
        assert response.code == HTTPStatus.PAYMENT_REQUIRED, "Expected PAYMENT_REQUIRED"
