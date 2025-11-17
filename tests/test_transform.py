import pandas as pd
from src.transform.transformer import transform_data

def test_transform_basic():
    raw = [
        {"id": 1, "Name": "Alice", "value": 10},
        {"id": 2, "Name": "Bob", "value": 20}
    ]

    df = transform_data(raw)
    # Colunas normalizadas
    assert "name" in df.columns or "name" in df.columns
    # Comprimento correto
    assert len(df) == 2
    # Tipos: DataFrame
    assert isinstance(df, pd.DataFrame)

def test_transform_remove_duplicates():
    raw = [
        {"id": 1, "Name": "Alice"},
        {"id": 1, "Name": "Alice Duplicate"}
    ]
    df = transform_data(raw)
    assert len(df) == 1
    # id coluna presente
    assert "id" in df.columns
