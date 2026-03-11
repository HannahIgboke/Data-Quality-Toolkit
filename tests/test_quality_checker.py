import pytest
import pandas as pd
from dqkit.quality_checker import Quality

@pytest.fixture
def df():
    df ={
    "customer_id": [1, 2, 3, 4, 4, 5, 6],
    "name": ["Joy", "Hannah", "Ben", "Daniel", "Daniel", None,"Jim"],
    "age": ["23", "54","45", "17", "17", None, None],
    "number": ["45678", "56789", "05566", "09876", "09876", "54679", None]
    }
    data = pd.DataFrame(df)
    yield data

def test_check_missing(df):
    quality = Quality(df)
    result = quality.check_missing_values()
    assert "name" in result
    assert "age" in result
    assert "number" in result

def test_check_duplicates(df):
    quality = Quality(df)
    result = quality.check_duplicates() 
    assert result['Number of duplicate rows found'] > 0 #I only want to check if there was a count for the duplicate values

def test_check_cardinality(df):
    quality = Quality(df)
    result = quality.check_cardinality()
    assert "customer_id" in result
    assert "name" in result
    assert "number" in result
