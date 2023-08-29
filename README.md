# tableau-sql-parser
SQL parser for Tableau custom SQL requests

## Usage

Given a .twb or a .twbx Tableau archive, you can extract these information:
- number of queries analyzed
- tables used
- a tree-like structure describing `schema.tables.column`

The CLI command to use is `sqlparse`:

`sqlparse -f file/to/parse.twb(x) -r custom_report_name -o`

Type `sqlparse --help` for more details.

## Contribute

In a python environment with poetry installed, run:

`poetry install`

to setup the virtual environment. Then run

`poetry shell`

to enter the virtual environnement previously created.

To check if everything-s working fine, run:

`pytest`

to run all existing tests.