from dqkit.base import BaseCheck

class Quality(BaseCheck):
    def __init__(self, dataframe):
        super().__init__(dataframe)

    def __str__(self):
        text = f"Quality Checker-> validating a dataframe with {self.df.shape[0]} rows and {self.df.shape[1]} columns"
        return text

    def __repr__(self):
        text = f"Quality Checker (rows= {self.df.shape[0]} rows, cols={self.df.shape[1]})"
        return text


    def check_missing_values(self):
        count = {}
        for column in self.df:
            self.null_count = int(self.df[column].isnull().sum())
            self.null_percent = round((self.null_count/len(self.df[column]))*100, 2)
            if self.null_count == 0:
                continue
            else:
                count[column] = [self.null_count, self.null_percent]
                
        if not count:
                print("Your dataframe has no null values")
            
        return count

    def check_duplicates(self):
        self.dup_count = int(self.df.duplicated().sum())
        self.dup_rows = self.df[self.df.duplicated()]
        return {"Number of duplicate rows found": self.dup_count,
                "These are the duplicate rows": self.dup_rows}

    def check_cardinality(self):
        card = {}
        for column in self.df:
            self.card_count = self.df[column].nunique()
            card[column] = self.card_count
        return card

    def run(self):
        check1 = self.check_missing_values()
        check2 = self.check_duplicates()
        check3 = self.check_cardinality()
        return {"Missing Values": check1, 
                "Duplicates": check2,
                "Cardinality": check3}
