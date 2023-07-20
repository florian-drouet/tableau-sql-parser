from typing import Union


class RecursiveSearch:
    def __init__(self):
        self.stock = {}
        self.index = 0

    @staticmethod
    def _flatten_values(values: list[str]) -> str:
        return str(" ".join([v.strip() for v in values if v not in (" ", "")]))

    @staticmethod
    def _extract_elements(element: Union[dict, list]) -> str:
        extraction = ""
        if isinstance(element, dict):
            values_list = list(element.values())
            extraction = RecursiveSearch._flatten_values(values=values_list)
            return extraction
        if isinstance(element, list):
            for i in range(0, len(element)):
                extraction += RecursiveSearch._flatten_values(
                    values=element[i].values()
                )
            return extraction
        return

    def recursive_depth_list(self, file_to_parse: list):
        for element in file_to_parse:
            self.index += 1
            if isinstance(element, dict):
                self.recursive_depth(file_to_parse=element)

    def recursive_depth(self, file_to_parse: dict):
        for key, values in file_to_parse.items():
            self.index += 1
            if key == "from_expression_element":
                table_reference = RecursiveSearch._extract_elements(
                    values.get("table_expression").get("table_reference")
                )
                table_alias = RecursiveSearch._extract_elements(
                    values.get("alias_expression")
                )
                self.stock[self.index] = [f"{table_reference} {table_alias}", "table"]
            if key == "column_reference":
                table_column = RecursiveSearch._extract_elements(element=values)
                self.stock[self.index] = [table_column, "column"]
            if isinstance(values, dict):
                self.recursive_depth(file_to_parse=values)
            if isinstance(values, list):
                self.recursive_depth_list(file_to_parse=values)
