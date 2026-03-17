from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class Report():
    def __init__(self, schema_validator, quality_checker):
        self.schema = schema_validator
        self.quality = quality_checker

    def generate(self):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("report.html")
        output = template.render(
            schema = self.schema.run(),
            quality = self.quality.run(),
            dataset_name=self.schema.dataset_name if hasattr(self.schema, 'dataset_name') else "Dataset",
            current_dtypes={col: str(self.schema.df[col].dtype) for col in self.schema.df.columns},
            memory=self.schema.estimate_memory_usage(self.schema.df),
            num_rows = self.schema.df.shape[0],
            num_cols = self.schema.df.shape[1],
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        with open("report_output.html", "w", encoding="utf-8") as f:
            print(output, file = f)
        print("Report saved")