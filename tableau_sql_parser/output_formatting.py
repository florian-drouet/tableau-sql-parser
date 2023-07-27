class OutputFormatting:
    def __init__(self, report_name: str, alias: dict, columns: dict):
        self.report_name = report_name
        self.tables_names = []
        self.column_names = []
        self.alias = alias
        self.columns = columns
        self.get_column_names_all()
        self.get_tables_names()

    @staticmethod
    def get_column_names(alias: dict, columns: dict) -> list:
        column_names_full = []
        for value in columns.values():
            split = value.split(".", 1)
            potential_alias = split[0]
            if potential_alias in alias.keys():
                column_names_full.append(f"{alias[potential_alias]}.{split[1]}")
            else:
                column_names_full.append(potential_alias)
        return column_names_full
            
    def get_column_names_all(self):
        temp_column_names = []
        for i in range(0, len(self.alias)):
            temp_column_names.extend(self.get_column_names(alias=self.alias[i], columns=self.columns[i]))
        self.column_names = sorted([*set(temp_column_names)])

    def get_tables_names(self):
        temp_table_names = []
        for column in self.column_names:
            temp_table_names.append(".".join(column[::-1].split(".", 1)[1:])[::-1])
        self.tables_names = sorted([*set(temp_table_names)])
