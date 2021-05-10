import pytest


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def pyopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('"foo"set to:', foo)
    print('"myopt"set to:', myopt)
