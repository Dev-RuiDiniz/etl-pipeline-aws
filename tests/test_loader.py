import pytest
from src.load.loader import get_engine
from config.settings import settings

def test_get_engine():
    engine = get_engine()
    assert engine is not None
