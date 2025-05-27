import json
import pytest
from pathlib import Path
from tableau_sql_parser.dbt_manifest_parser import DbtManifestParser


@pytest.fixture
def manifest_file(tmp_path) -> Path:
    """Creates a mock manifest.json file for testing."""
    manifest_data = {
        "nodes": {
            "model.test.model_a": {
                "resource_type": "model",
                "schema": "analytics",
                "alias": "model_a"
            },
            "seed.test.seed_a": {
                "resource_type": "seed",
                "schema": "public",
                "alias": "seed_a"
            }
        },
        "sources": {
            "source.test.source_a": {
                "schema": "raw",
                "identifier": "source_a"
            }
        }
    }
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest_data))
    return path


def test_load_manifest(manifest_file):
    parser = DbtManifestParser(manifest_file)
    assert isinstance(parser.manifest, dict)
    assert "nodes" in parser.manifest
    assert "sources" in parser.manifest


def test_extract_dbt_objects(manifest_file):
    parser = DbtManifestParser(manifest_file)
    expected = [
        {"type": "model", "schema": "analytics", "table": "model_a"},
        {"type": "seed", "schema": "public", "table": "seed_a"},
        {"type": "source", "schema": "raw", "table": "source_a"},
    ]
    assert parser.dbt_objects == expected


def test_get_schema_table_strings(manifest_file):
    parser = DbtManifestParser(manifest_file)
    expected = sorted([
        "analytics.model_a",
        "public.seed_a",
        "raw.source_a"
    ])
    assert parser.get_schema_table_strings() == expected


def test_get_tables(manifest_file):
    parser = DbtManifestParser(manifest_file)
    expected = sorted(["model_a", "seed_a", "source_a"])
    assert parser.get_tables() == expected


def test_get_all_table_names(manifest_file):
    parser = DbtManifestParser(manifest_file)
    expected = sorted([
        "analytics.model_a",
        "public.seed_a",
        "raw.source_a",
        "model_a",
        "seed_a",
        "source_a"
    ])
    assert sorted(parser.get_all_table_names()) == expected


def test_missing_file_raises(tmp_path):
    non_existent_path = tmp_path / "missing_manifest.json"
    with pytest.raises(FileNotFoundError):
        DbtManifestParser(non_existent_path)