import unittest
import sys

from .conftest import pytest_report_header

__copyright__ = "Copyright 2019, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"


def _run_tests(test_suite, package_name):
    """Core function to test a test suite.

    :param test_suite: Unittest test suite
    """
    count = test_suite.countTestCases()
    print("######## Environment   ########")
    print(pytest_report_header(None))
    print("{} tests has been discovered in {}".format(count, package_name))
    print("######## Running tests ########")
    results = unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)
    print("######## Summary       ########")
    print("Errors               : {}".format(len(results.errors)))
    print("Failures             : {}".format(len(results.failures)))
    print("Expected failures    : {}".format(len(results.expectedFailures)))
    print("Unexpected successes : {}".format(len(results.unexpectedSuccesses)))
    print("Skip                 : {}".format(len(results.skipped)))
    successes = (
        results.testsRun - (
            len(results.errors) + len(results.failures) + len(results.expectedFailures)
            + len(results.unexpectedSuccesses) + len(results.skipped)))
    print("Successes            : {}".format(successes))
    print("TOTAL                : {}".format(results.testsRun))


def test_package(package=".."):
    """Test package.
    This function is called by travis without arguments.

    :param package: The package to test.
    :type package: str
    """
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover(package)
    _run_tests(test_suite, package)


if __name__ == "__main__":
    test_package()
