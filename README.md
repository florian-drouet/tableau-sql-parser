# tableau-sql-parser
SQL parser for Tableau custom SQL requests

## What is it ?

Given a .twb or a .twbx Tableau archive, you can extract as a report these information:
- number of queries analyzed
- tables used
- a tree-like structure describing `schema.tables.column`

## How to use it ?

**Requirement** : install [uv](https://github.com/astral-sh/uv) globally (with brew for example)  

Then run `uv sync`  
Then download a Tableau archive (.twbx or .twb)  
Then run `uv run sqlparse -f file/to/parse/archive.twb(x) -r custom_report_name -o` to extract the report  

Type `uv run sqlparse --help` for more details.