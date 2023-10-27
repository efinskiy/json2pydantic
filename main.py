import json
from typing import Dict, Any, Union
from pydantic import Json
from datamodel_code_generator.parser.jsonschema import JsonSchemaParser
from genson import SchemaBuilder


def translate(
    input_text: Union[Json, Dict[str, Any]]
) -> str:
    builder = SchemaBuilder()
    builder.add_object(input_text)
    schema = builder.to_schema()
    s = json.dumps(schema)
    parser = JsonSchemaParser(
        source=s,
        base_class="pydantic.BaseModel",
        snake_case_field=False
    )
    return parser.parse()


if '__main__' == __name__:
    source = ''
    with open('source.json', 'r') as f:
        source = f.read()

    code_gen = translate(json.loads(source))

    with open('codegen.py', 'w') as f:
        f.write(code_gen)
        f.close()
