import pytest
import json
import os

from api.client.auth_client import AuthClient
from test_data import auth_data
from jsonschema import validate
from pathlib import Path


def load_schema(schema_name):

    project_root = Path(__file__).resolve().parent.parent
    schema_path = project_root / "schemas" / schema_name
    with open(schema_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def validate_schema(response_json, schema_name):
    schema = load_schema(schema_name)
    validate(instance=response_json, schema=schema)
    