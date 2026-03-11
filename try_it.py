import pandas as pd
from dqkit.schema_validator import SchemaValidator
from dqkit.quality_checker import Quality
from dqkit.report import Report

ref = {
    "customer_id": [1, 2, 3],
    "name": ["Joy", "Hannah", "Daniel"],
    "age": [23, 54, 17],
    "email": ["joy@gmail.com", "ann@gmail.com", "dan@gmail.com"]
}

curr = {
    "customer_id": [1, 2, 3],
    "name": ["Joy", "Hannah", "Daniel"],
    "age": ["23", "54", "17"],
    "number": ["45678", "56789", "09876"]
}

curr2 = {
    "customer_id": [1, 2, 3, 4, 4, 5, 6],
    "name": ["Joy", "Hannah", "Ben", "Daniel", "Daniel", None,"Jim"],
    "age": ["23", "54","45", "17", "17", None, None],
    "number": ["45678", "56789", "05566", "09876", "09876", "54679", None]
}

df_ref = pd.DataFrame(ref)
df_curr = pd.DataFrame(curr)
df_curr2 = pd.DataFrame(curr2)

airbnb_curr = pd.read_csv("data/AB_NYC_2019.CSV")
airbnb_ref = pd.read_csv("data/airbnb_reference.csv")

https://github.com/HannahIgboke/Data-Quality-Toolkit

# run_check = SchemaValidator(df_curr, df_ref)
# print(run_check.run())

# run_check2 = Quality(df_curr)
# print(run_check2.run())
# run_check3 = Quality(df_curr2)
# print(run_check3.run())

sv = SchemaValidator.from_csv("data/AB_NYC_2019.CSV", "data/airbnb_reference.csv")
quality = Quality(airbnb_curr)

report = Report(sv, quality)
report.generate()

# print(str(sv))
# print(repr(sv))
# print(str(quality))
# print(repr(quality))
# print(type(df_curr))
# sv.df = "not a dataframe"

# print(SchemaValidator.estimate_memory_usage(df_curr))

# profile = ProfileReport(df_curr)

# # save it as an HTML file you can open in your browser
# profile.to_file("profile_report.html")

