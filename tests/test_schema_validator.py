import pytest
import pandas as pd
from dqkit.schema_validator import SchemaValidator

@pytest.fixture
def df_curr():
    df = {
    "customer_id": [1, 2, 3],
    "name": ["Joy", "Hannah", "Daniel"],
    "age": ["23", "54", "17"],
    "number": ["45678", "56789", "09876"]
    }
    data_curr = pd.DataFrame(df)
    yield data_curr

@pytest.fixture
def df_ref():
    df= {
    "customer_id": [1, 2, 3],
    "name": ["Joy", "Hannah", "Daniel"],
    "age": [23, 54, 17],
    "email": ["joy@gmail.com", "ann@gmail.com", "dan@gmail.com"]
    }
    data_ref = pd.DataFrame(df)
    yield data_ref


#using the fixture in a test
def test_check_columns(df_curr, df_ref):
    sv = SchemaValidator(df_curr, df_ref)
    result = sv.check_columns()
    assert "email" in result["Missing Columns"]
    assert "number" in result["Unexpected Columns"]

def test_data_types(df_curr, df_ref):
    sv = SchemaValidator(df_curr, df_ref)
    result = sv.check_dtypes()
    assert "age" in result