from abc import ABC, abstractmethod
import pandas as pd

class BaseCheck(ABC):
    def __init__(self, dataframe):
        self.df = dataframe

    @property
    def df(self):
        return self._df
    
    @df.setter
    def df(self, value):
        print("Checking input type...")
        if not isinstance(value, pd.DataFrame):
            raise TypeError ("Your input is not a dataframe")
        else:
            self._df = value

    #this ensures that every method that inherits from it must provide their own implementation of the run function
    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        text = f"Data Checker -> dataframe with {self.df.shape[0]} rows and {self.df.shape[1]} columns"
        return text

    def __repr__(self):
        text = f"Data Checker (rows= {self.df.shape[0]} rows, cols={self.df.shape[1]})"
        return text
