import pytest
from http import HTTPStatus
from task2.utils.client import APIClient, EndPoints
from collections import namedtuple

# test cases for searching countries endpoint
search_term_test_case = namedtuple("test_search_term", "search_term, results_count, status_code")
search_term_test_cases = [
    search_term_test_case(search_term='Andorra', results_count=1, status_code=HTTPStatus.OK),
    search_term_test_case(search_term='AD', results_count=12, status_code=HTTPStatus.OK),
    search_term_test_case(search_term=111, results_count=0, status_code=HTTPStatus.OK),
    search_term_test_case(search_term='x', results_count=0, status_code=HTTPStatus.BAD_REQUEST)
]

# test case fors getting countries with public_holidays & search term
public_holiday_search_term_test_case = namedtuple("public_holiday_search_term_test_case", "public_holidays, search_term, results_count, status_code")
public_holdiay_search_term_test_cases = [
    public_holiday_search_term_test_case(public_holidays=True, search_term='Andorra', results_count=1, status_code=HTTPStatus.OK),
    public_holiday_search_term_test_case(public_holidays=False, search_term='AD', results_count=12, status_code=HTTPStatus.OK),
    public_holiday_search_term_test_case(public_holidays=True, search_term=111, results_count=0, status_code=HTTPStatus.OK),
    public_holiday_search_term_test_case(public_holidays=False, search_term='x', results_count=0, status_code=HTTPStatus.BAD_REQUEST)
]


def get_search_term_test_case_name(test_case):
    """
    test name for search_term_test_case
    """
    name = f"search_term: {test_case.search_term}, expected_results_count: {test_case.results_count} " \
           f"expected_status_code: {test_case.status_code}"
    return name


def get_public_holdiay_search_term_test_case_name(test_case):
    """
    test name for public_holiday_search_term_test_case
    """
    name = f"public_holdays: {test_case.public_holidays}, search_term: {test_case.search_term}, expected_results_count: {test_case.results_count} " \
           f"expected_status_code: {test_case.status_code}"
    return name


class TestCountries:

    ALL_COUNTRIES = 250

    @pytest.mark.smoke
    def test_get_countries(self):
        """
        test get countries
        """
        client = APIClient(EndPoints.countries)
        response = client.get()
        assert response.code == HTTPStatus.OK, response.raw_content
        content = response.json_content
        countries = content.get('countries')
        assert countries, f"expected contries list, found None"
        assert len(countries) == self.ALL_COUNTRIES, "countries count did not match"

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_case", public_holdiay_search_term_test_cases, ids=get_public_holdiay_search_term_test_case_name)
    def test_get_countries_with_public_holidays(self, test_case):
        """
        test get countries with public holdiays
        """
        client = APIClient(EndPoints.countries)
        response = client.get(params={'public': test_case.public_holidays, 'search': test_case.search_term})
        assert response.code == test_case.status_code, response.raw_content
        if test_case.status_code == HTTPStatus.OK:
            content = response.json_content
            countries = content.get('countries')
            assert len(countries) == test_case.results_count, "countries count did not match"

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_case", search_term_test_cases, ids=get_search_term_test_case_name)
    def test_search_countries(self, test_case):
        """
        test search countries
        """
        client = APIClient(EndPoints.countries)
        response = client.get(params={'search': test_case.search_term})
        assert response.code == test_case.status_code, response.raw_content
        if test_case.status_code == HTTPStatus.OK:
            content = response.json_content
            countries = content.get('countries')
            assert len(countries) == test_case.results_count, "countries count did not match"
