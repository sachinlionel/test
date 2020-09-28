import pytest
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--smoke-test', action='store_true', help='Run Smoke Tests')
PARSER.add_argument('--keywords', default='test', help='run tests with keyword')
PARSER.add_argument('--pdb', default='test', help='enable pdb on first failure')
ARGS = PARSER.parse_args()


def main():
    """
    Execute test based on command line args
    """
    test_folder = 'test'

    # default pytest args, runs whole test in test_folder
    pytest_args = [test_folder, '-vs', '--junitxml=test.xml']

    if ARGS.smoke_test:
        # to execute only smoke
        pytest_args.append('-m smoke')
    if ARGS.keywords:
        # to execute only test containing keyword
        pytest_args.append('-k ' + ARGS.keywords)
    if ARGS.pdb:
        # to enable debugger while testing on local
        pytest_args.append(ARGS.pdb)
    print(f"Running tests with following arguments {pytest_args}")
    pytest.main(pytest_args)

if __name__ == "__main__":
    main()