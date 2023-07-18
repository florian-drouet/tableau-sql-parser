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

    args = parser.parse_args()
    print(args.filename)
    my_workbook = TableauWorkbook(args.filename.name)
    print(my_workbook.recursive_searched_queries[0])
