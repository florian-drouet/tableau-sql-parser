class OutputFormatting:
    def __init__(self, outputs: list, report_name: str):
        self.outputs = outputs
        self.report_name = report_name
        self.number_queries = len(self.outputs)
        self.number_tables = 0
        self.tables = []
        self.get_insights()

    def get_insights(self):
        tables = []
        for output in self.outputs:
            for values in output.values():
                if values[1] == "table":
                    tables.append(values[0])
        self.tables = [*set(tables)]
        self.number_tables = len(self.tables)

    def format_output(self):
        # fmt: off
        with open(f"{self.report_name}.md", "bw") as f:
            f.write((f"# Tableau SQL report | {self.report_name}  \n").encode("utf-8"))
            f.write((f"{self.number_queries} queries have been analyzed.  \n\n").encode("utf-8"))
            f.write((f"{self.number_tables} tables used: {self.tables}  \n\n").encode("utf-8"))
            for index, output in enumerate(self.outputs, start=1):
                f.write((f"\nQuery number {index}:\n").encode("utf-8"))
                f.write(("| index | input | type |\n|---:|:---|:---|\n").encode("utf-8"))
                for index, lines in output.items():
                    f.write((f"| {index} |").encode("utf-8"))
                    for element in lines:
                        f.write((f" {element} |").encode("utf-8"))
                    f.write(("\n").encode("utf-8"))
        # fmt: on
