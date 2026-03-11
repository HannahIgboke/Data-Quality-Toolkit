from dqkit.base import BaseCheck #SchemaValidator inherits from BaseCheck because it is a kind of check
import pandas as pd
from pathlib import Path

class SchemaValidator(BaseCheck):
    """
    The schema validator checks if your data (called the current data) looks like what you expect (the refernce data) it to look like.
    df_curr = what the data looks like right now that needs validation
    df_ref = what the data should look like. It contains the expected columns, their names and their data types

    The check_columns function checks for two things:
    - Columns expected in df_ref but which are mising from df_curr
    - Columns present but unexpected in df_curr
    """

    def __init__(self, dataframe, reference_schema=None):
        super().__init__(dataframe)
        self.ref_df = reference_schema

    def __str__(self):
        text = f"Schema Validator -> validating a dataframe with {self.df.shape[0]} rows and {self.df.shape[1]} columns"
        return text

    def __repr__(self):
        text = f"Schema Validator (rows= {self.df.shape[0]} rows, cols={self.df.shape[1]}, reference_schema ={True if self.ref_df is not None else False})"
        return text
    
    @classmethod
    def from_csv(cls, current_path, reference_path=None):
        dataset_name = Path(current_path).stem
        curr_df = pd.read_csv(current_path)
        ref_df = None
        if reference_path is not None:
            ref_df = pd.read_csv(reference_path)
        instance = cls(curr_df, ref_df)
        instance.dataset_name = dataset_name
        return instance

    @staticmethod
    def estimate_memory_usage(df):
        total_bytes_memory = round(((df.memory_usage(deep=True).sum())/1024), 2)
        col_memory = {}
        for col in df.columns:
            memory = round(((df[col].memory_usage(deep=True))/1024), 2)
            col_memory[col] = memory

        return {
            "total_memory_usage": f"{total_bytes_memory} KB",
            "per_column_usage": col_memory
        }


    def check_columns(self):
        if self.ref_df is None:
            return {"status": "No refrence_schema provided"}
        else:
            self.df_columns = self.df.columns
            self.ref_columns = self.ref_df.columns
            not_in_curr  = {}
            present_but_unexpected = {}
            for column in self.ref_columns:
                if column not in self.df_columns:
                    not_in_curr[column] = 1
            for column in self.df_columns:
                if column not in self.ref_columns:
                    present_but_unexpected[column] = 1

        return {
            "Missing Columns": not_in_curr, 
            "Unexpected Columns": present_but_unexpected
        }

    def check_dtypes(self):
        if self.ref_df is None:
            return {"status": "No refrence_schema provided"}
        else:
            dtype_mismatches = {}
            for column in self.df:
                if column not in self.ref_df.columns:
                    continue    
                column_type = self.df[column].dtype
                if column_type != self.ref_df[column].dtype:
                    dtype_mismatches[column] = {
                        "current": str(self.df[column].dtype),
                        "expected": str(self.ref_df[column].dtype)
                    }

        return dtype_mismatches
    
    def run(self):
        check1 = self.check_columns()
        check2 = self.check_dtypes()
        return {"Column Checks": check1, "Data Type Checks": check2}

