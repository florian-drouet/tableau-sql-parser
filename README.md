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