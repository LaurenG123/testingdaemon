

import time
import pytest

def run_tests_as_daemon():
    while True:
        # Run your tests here
        result = pytest.main(['-x', 'tests/'])  # Run pytest with exit on first failure
        if result == 0:
            print("All tests passed!")
        else:
            print("Some tests failed. Check the logs for details.")

        # Sleep for some time before running tests again
        time.sleep(3600)  # Sleep for 1 hour before running tests again

if __name__ == "__main__":
    run_tests_as_daemon()

