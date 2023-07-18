import argparse

from tableau_workbook import TableauWorkbook
from utils import is_valid_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tableau-sql-parser cli arguments")

    parser.add_argument(
        "-f",
        dest="filename",
        required=True,
        help="input twb or twbx file",
        metavar="FILE",
        type=lambda x: is_valid_file(parser, x),
    )

    parser.add_argument(
        "-r",
        dest="report_name",
        required=True,
        help="input report name",
        type=str,
    )

    args = parser.parse_args()
    my_workbook = TableauWorkbook(
        filename=args.filename.name, report_name=args.report_name
    )
    my_workbook._generate_output()
