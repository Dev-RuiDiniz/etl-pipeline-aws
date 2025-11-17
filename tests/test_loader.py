
import pandas as pd
import pytest
from src.load import loader
from config import settings
import sqlalchemy

def test_get_engine_monkeypatch(monkeypatch):
    captured = {}
    def fake_create_engine(url):
        captured['url'] = url
        class DummyEngine: pass
        return DummyEngine()

    monkeypatch.setattr("src.load.loader.create_engine", fake_create_engine)
    # ensure settings have expected fields (these may come from your env)
    # call get_engine
    engine = loader.get_engine()
    assert engine is not None
    assert "postgresql+psycopg2://" in captured['url']
    # verify that DB user and host from settings are part of the url string
    assert settings.DB_USER in captured['url']
    assert settings.DB_HOST in captured['url']
