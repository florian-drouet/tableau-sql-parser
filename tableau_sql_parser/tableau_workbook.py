import logging
import os
import zipfile

import lxml.etree
import sqlfluff

from tableau_sql_parser.output_formatting import OutputFormatting
from tableau_sql_parser.recursive_search import RecursiveSearch


class TableauWorkbook:
    """
    Defines a workbook object from a filename.
    """

    def __init__(self, filename, report_name):
        self.filename = os.path.normpath(filename)
        self.report_name = report_name
        self.xml = self._get_xml()
        self.custom_sql = self._get_custom_sql()
        self.custom_sql_parsed = self._parse_custom_sql()
        (
            self.recursive_searched_queries,
            self.columns,
            self.alias,
        ) = self._recursive_search_sql()

    def _get_xml(self):
        """
        Returns the xml of the given .twb or .twbx file.
        """

        # Ensure workbook_file is a workbook file
        twb = self.filename.split(".")

        if twb[-1][:3] != "twb" or len(twb) == 1:
            return self.filename + " is not a valid .twb or .twbx file."

        else:
            # unzip packaged workbooks to obtain xml
            if twb[-1] == "twb":
                xml = lxml.etree.parse(self.filename).getroot()

            else:
                with open(self.filename, "rb") as binfile:
                    twbx = zipfile.ZipFile(binfile)
                    name = [w for w in twbx.namelist() if w.find(".twb") != -1][0]
                    unzip = twbx.open(name)
                    xml = lxml.etree.parse(unzip).getroot()

            return xml

    def _get_custom_sql(self):
        """
        Returns a list of all unique custom sql queries in the workbook.
        """

        search = self.xml.xpath("//relation[@type='text']")
        queries = list(
            set(
                [
                    sql.text.lower().replace("<<", "<").replace(">>", ">")
                    for sql in search
                ]
            )
        )

        return queries

    def _parse_custom_sql(self):
        """
        Returns a list of all unique custom sql queries
        in the workbook parsed by sqlfluff parser
        """
        parsed_queries = []
        for sql_request in self.custom_sql:
            try:
                parsed_queries.append(sqlfluff.parse(sql_request))
            except Exception as e:
                logging.error(e)
        return parsed_queries

    def _recursive_search_sql(self):
        """
        Returns a dict where keys are index and values are a list of column/table names
        """
        recursive_searched_queries = []
        columns = []
        alias = []
        for i in range(0, len(self.custom_sql_parsed)):
            search = RecursiveSearch()
            search.recursive_depth(file_to_parse=self.custom_sql_parsed[i])
            recursive_searched_queries.append(search.stock)
            columns.append(search.columns)
            alias.append(search.alias)
        return recursive_searched_queries, columns, alias

    def _generate_output(self):
        number_queries_analyzed = len(self.recursive_searched_queries)
        report = OutputFormatting(
            report_name=self.report_name,
            alias=self.alias,
            columns=self.columns,
        )
        return report.tables_names, report.column_names, number_queries_analyzed
