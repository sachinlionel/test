import pytest
from http import HTTPStatus
from task2.utils.client import APIClient, EndPoints
from multiprocessing import Process


class TestEndpoints:
    """
    At present this module tests only countries endpoint
    TODO: test other endpoint [languages, holidays, workday]
    """

    def concurrent_task(self):
        """
        function for testing cocurrent calls on countries API
        """
        client = APIClient(EndPoints.countries)
        response = client.get()
        assert response.code == HTTPStatus.OK, response.raw_content

    @pytest.mark.smoke
    def test_with_api(self):
        """
        test api endpoint with default valid api key
        """
        client = APIClient(EndPoints.countries)
        response = client.get()
        assert response.code == HTTPStatus.OK, response.raw_content

    @pytest.mark.smoke
    def test_without_api(self):
        """
        test api endpoint with out api key
        """
        client = APIClient(EndPoints.countries, default_api_key=False, api_key=None)
        response = client.get()
        assert response.code == HTTPStatus.UNAUTHORIZED, response.raw_content

    def test_incorrect_api(self):
        """
        test api endpoint with malformed api key
        """
        client = APIClient(EndPoints.countries, default_api_key=False, api_key="2a5e5e8f-1a10-48bf-8be7-0555d2c1hdg")
        response = client.get()
        assert response.code == HTTPStatus.UNAUTHORIZED, response.raw_content

    @pytest.mark.parametrize("num_of_concurrency", (5,10))
    def test_concurrent_call(self, num_of_concurrency):
        """
        test concurrent calls
        """
        process_list = []
        for _ in range(num_of_concurrency):
            p = Process(target=self.concurrent_task)
            process_list.append(p)
            p.start()

        # Exit code zero indicates success for concurrent_task, other wise exit code is non zero
        sum_exitcode = 0
        for p in process_list:
            p.join()
            sum_exitcode += p.exitcode
        assert sum_exitcode == 0, "one or more concurrent tests failed"
