
import types
import requests
from src.extract.extractor import extract_data
import pytest

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise requests.HTTPError(f"Status {self.status_code}")

    def json(self):
        return self._json

def test_extract_success(monkeypatch):
    sample = {"results": [{"id": 1}]}

    def fake_get(url, timeout):
        return DummyResponse(sample, 200)

    monkeypatch.setattr("requests.get", fake_get)
    data = extract_data()
    assert data == sample

def test_extract_http_error(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse({}, 500)

    monkeypatch.setattr("requests.get", fake_get)
    with pytest.raises(requests.HTTPError):
        extract_data()
