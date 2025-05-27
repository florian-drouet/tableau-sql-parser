import json
from pathlib import Path


class DbtManifestParser:
    def __init__(self, manifest_path: Path) -> None:
        self.manifest_path = manifest_path
        self.manifest = self._load_manifest()
        self.dbt_objects = self._extract_dbt_objects()

    def _load_manifest(self) -> dict:
        """Load and parse the dbt manifest.json file."""
        if not self.manifest_path:
            raise FileNotFoundError(f"manifest.json not found at {self.manifest_path}")
        with open(self.manifest_path) as f:
            return json.load(f)

    def _extract_dbt_objects(self) -> list[dict[str, str]]:
        """
        Extract dbt-generated objects (models, seeds, sources) from the manifest.

        Returns:
            List of dicts with fields: type, schema, table
        """
        results = []

        nodes = self.manifest.get("nodes", {})
        sources = self.manifest.get("sources", {})

        # Extract models and seeds
        for node in nodes.values():
            resource_type = node.get("resource_type")
            if resource_type in {"model", "seed"}:
                schema = node.get("schema")
                table = node.get("alias")
                if schema and table:
                    results.append({
                        "type": resource_type,
                        "schema": schema,
                        "table": table
                    })

        # Extract sources
        for source in sources.values():
            schema = source.get("schema")
            table = source.get("identifier")
            if schema and table:
                results.append({
                    "type": "source",
                    "schema": schema,
                    "table": table
                })

        return results

    def get_schema_table_strings(self) -> list[str]:
        """Return distinct list of schema.table strings."""
        return sorted({f'{obj["schema"]}.{obj["table"]}' for obj in self.dbt_objects})

    def get_tables(self) -> list[str]:
        """Return distinct list of tables."""
        return sorted({obj["table"] for obj in self.dbt_objects})

    def get_all_table_names(self) -> list[str]:
        """Return all table names from the manifest."""
        schema_table_strings = self.get_schema_table_strings()
        tables = self.get_tables()
        return [*schema_table_strings, *tables]
