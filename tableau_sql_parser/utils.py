import os
import shutil

import click
from platformdirs import user_cache_dir

from tableau_sql_parser import APP_NAME, CACHE_FILENAME


def tree_output(column_names: list) -> str:
    increment = 0
    tree = ""

    for i in range(0, len(column_names)):
        current_line = column_names[i].split(".")

        for index, element in enumerate(current_line[increment:], start=increment):
            click.echo(index * "|--" + element)
            tree += index * "|--" + element + "\n"

        if i != len(column_names) - 1:
            next_line = column_names[i + 1].split(".")

        max_length = max(len(current_line), len(next_line))

        for ii in range(0, max_length - 1):
            if (
                current_line[ii : ii + 1] == next_line[ii : ii + 1]
                and len(current_line[ii : ii + 1]) > 0
                and len(next_line[ii : ii + 1]) > 0
            ):
                increment += 1
            elif increment > 0:
                increment -= 1

            if increment >= max_length:
                increment = max_length - 1
    return tree


def generate_report(
    tables_names: list, column_names: list, number_queries: int, report_name: str
) -> None:
    joined_tables = " | ".join([table for table in tables_names if table != ""])
    tree = tree_output(column_names=column_names)
    with open(f"{report_name}.txt", "w") as f:
        f.write(f"Custom Tableau SQL Report | {report_name}\n")
        f.write("---\n")
        f.write(f"\nNumber of queries analyzed: {number_queries}\n")
        f.write("---\n")
        f.write("\nTables are:\n")
        f.write(joined_tables + "\n")
        f.write("---\n")
        f.write("\nColumns are:\n")
        f.write(tree)
        f.write("---\n")


def resolve_manifest_path() -> str:
    """Manage cached manifest.json: use, replace, or delete."""
    cache_dir = user_cache_dir(APP_NAME)
    os.makedirs(cache_dir, exist_ok=True)
    cached_manifest_path = os.path.join(cache_dir, CACHE_FILENAME)

    if os.path.exists(cached_manifest_path):
        click.echo("📦 Cached manifest.json file detected.")
        action = click.prompt(
            "Do you want to use the cached file? (use / replace / delete)",
            type=click.Choice(["use", "replace", "delete"]),
            default="use"
        )

        if action == "use":
            click.echo(f"Using cached manifest: {cached_manifest_path}")
            return cached_manifest_path

        elif action == "replace":
            manifest_path = click.prompt(
                "Enter the path to the new manifest file",
                type=click.Path(exists=True)
            )
            shutil.copy(manifest_path, cached_manifest_path)
            click.echo(f"✅ Replaced cached manifest with: {manifest_path}")
            return cached_manifest_path

        elif action == "delete":
            os.remove(cached_manifest_path)
            click.echo("🗑️ Deleted cached manifest file.")
            return None
    else:
        if click.confirm("Do you want to add a manifest file?", default=False):
            manifest_path = click.prompt(
                "Enter the path to the manifest file",
                type=click.Path(exists=True)
            )
            shutil.copy(manifest_path, cached_manifest_path)
            click.echo(f"✅ Cached manifest: {cached_manifest_path}")
            return cached_manifest_path

    return None
