import requests
import pytest
from src.extract.extractor import extract_data

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError("Erro HTTP")

    def json(self):
        return self._json

def test_extract_success(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse({"ok": True}, 200)

    monkeypatch.setattr("requests.get", fake_get)
    data = extract_data()
    assert data == {"ok": True}

def test_extract_error(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse({}, 500)

    monkeypatch.setattr("requests.get", fake_get)

    with pytest.raises(requests.HTTPError):
        extract_data()
