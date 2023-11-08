import pytest


@pytest.fixture
def browser():
    print("Я выполняюсь перед тестом")

    yield

    print("Я выполняюсь после теста")


@pytest.fixture
def login_page(browser):


@pytest.fixture
def credentials():
    return "admin", "12345"


def test_login(login_page, credentials):
    assert credentials == ("admin", "12345")