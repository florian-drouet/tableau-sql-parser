class OutputFormatting:
    def __init__(
        self,
        report_name: str,
        alias: dict,
        columns: dict,
        dbt_table_names: list
    ) -> None:
        self.report_name = report_name
        self.tables_names = []
        self.column_names = []
        self.alias = alias
        self.columns = columns
        self.dbt_table_names = dbt_table_names
        self.get_column_names_all()
        self.get_tables_names()

    @staticmethod
    def get_column_names(alias: dict, columns: dict) -> list:
        column_names_full = []
        for value in columns.values():
            split = value.split(".", 1)
            potential_alias = split[0]
            if potential_alias in alias:
                column_names_full.append(f"{alias[potential_alias]}.{split[1]}")
            else:
                column_names_full.append(potential_alias)
        return column_names_full

    @staticmethod
    def filter_dbt_manifest(column_names: list, dbt_columns: list) -> None:
        """
        This function filters the dbt manifest to get the relevant information
        for the report.
        """
        filtered_elements = []
        for column in column_names:
            splitted_column = column.rsplit(".", 1)[0]
            if splitted_column in dbt_columns:
                filtered_elements.append(column)
        return filtered_elements


    def get_column_names_all(self) -> None:
        temp_column_names = []
        for i in range(0, len(self.alias)):
            temp_column_names.extend(
                self.get_column_names(alias=self.alias[i], columns=self.columns[i])
            )
            if self.dbt_table_names:
                temp_column_names = self.filter_dbt_manifest(
                    column_names=temp_column_names, dbt_columns=self.dbt_table_names
                )
        self.column_names = sorted([*set(temp_column_names)])

    def get_tables_names(self) -> None:
        temp_table_names = []
        for column in self.column_names:
            temp_table_names.append(".".join(column[::-1].split(".", 1)[1:])[::-1])
        self.tables_names = sorted([*set(temp_table_names)])
