from tableau_sql_parser.tableau_workbook import TableauWorkbook
import click

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
def main(file_to_parse, report_name):
   click.echo(f'File name is: {file_to_parse} and report name is: {report_name}')
   my_workbook = TableauWorkbook(filename=file_to_parse, report_name=report_name)
   my_workbook._generate_output()


if __name__ == '__main__':
   main()
