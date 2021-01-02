from marshmallow import Schema, fields
from marshmallow import ValidationError
import json

import typing as t


class InvalidInputError(Exception):
    """Invalid model input."""


class CrossSaleRequestSchema(Schema):
    id = fields.Integer()
    Gender = fields.Str()
    Age = fields.Integer()
    Driving_License = fields.Integer()
    Region_Code = fields.Float()
    Previously_Insured = fields.Integer()
    Vehicle_Age = fields.Str()
    Vehicle_Damage = fields.Str()
    Annual_Premium = fields.Float()
    Policy_Sales_Channel = fields.Float()
    Vintage = fields.Integer()



def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    print(indexes)
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = CrossSaleRequestSchema(strict=True, many=True)


    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages
        
    print('This is', errors)
    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
