import click
from utils import generate_report

from tableau_sql_parser.tableau_workbook import TableauWorkbook


@click.command()
@click.option(
    "-f",
    "--file-to-parse",
    required=True,
    help="input twb or twbx file",
    type=click.Path(exists=True),
)
@click.option(
    "-r",
    "--report-name",
    required=False,
    default="Custom Queries",
    help="input report name",
    type=str,
)
@click.option(
    "-o",
    "--is-output",
    is_flag=True,
    required=False,
)
def main(file_to_parse, report_name, is_output):
    click.echo(f"File name is: {file_to_parse} and report name is: {report_name}")
    my_workbook = TableauWorkbook(filename=file_to_parse, report_name=report_name)
    tables_names, column_names, number_queries = my_workbook._generate_output()
    if is_output:
        generate_report(
            tables_names=tables_names,
            column_names=column_names,
            number_queries=number_queries,
            report_name=report_name,
        )


if __name__ == "__main__":
    main()
