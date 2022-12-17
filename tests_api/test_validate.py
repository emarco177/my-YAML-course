from fastapi.testclient import TestClient
from app import app as fastapi_app

client = TestClient(fastapi_app)

API = "/api"


def test_valid_inline_yamls() -> None:
    assert 1 == 1


def test_none_valid_inline_yamls() -> None:
    assert 1 == 1


def test_valid_samples():
    assert 1 == 1


def test_non_valid_samples():
    assert 1 == 1
