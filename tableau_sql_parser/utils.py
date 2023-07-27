import os
import click


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, "r")  # return an open file handle

def tree_output(column_names: list) -> str:
    increment = 0
    tree = ""

    for i in range(0, len(column_names)):
        current_line = column_names[i].split(".")

        for index, element in enumerate(current_line[increment:], start=increment):
            click.echo(index*'|--'+element)
            tree+=index*'|--'+element+"\n"

        if i != len(column_names)-1:
            next_line = column_names[i+1].split(".")

        max_length = max(len(current_line), len(next_line))

        for i in range(0, max_length-1):
            if current_line[i:i+1]==next_line[i:i+1] and len(current_line[i:i+1])>0 and len(next_line[i:i+1])>0:
                increment+=1
            elif increment>0:
                increment-=1

            if increment >= max_length:
                increment = max_length-1
    return tree

def generate_report(tables_names: list, column_names: list, number_queries: int, report_name: str):
    joined_tables = " | ".join([table for table in tables_names if table != ""])
    tree = tree_output(column_names=column_names)
    with open(f"{report_name}.txt", "w") as f:
        f.write(f"Custom Tableau SQL Report | {report_name}\n")
        f.write("---\n")
        f.write(f"\nNumber of queries analyzed: {number_queries}\n")
        f.write("---\n")
        f.write("\nTables are:\n")
        f.write(joined_tables+"\n")
        f.write("---\n")
        f.write("\nColumns are:\n")
        f.write(tree)
        f.write("---\n")
