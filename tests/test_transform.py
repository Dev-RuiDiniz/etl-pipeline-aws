import pandas as pd
from src.transform.transformer import transform_data

def test_transform_basic():
    raw = [{"id": 1, "Name": "Alice"}]
    df = transform_data(raw)
    assert isinstance(df, pd.DataFrame)
    assert "name" in df.columns

def test_transform_remove_duplicates():
    raw = [{"id": 1}, {"id": 1}]
    df = transform_data(raw)
    assert len(df) == 1
