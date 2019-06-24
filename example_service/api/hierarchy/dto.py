from rest_framework import serializers

from api_commons.dto import BaseDto, RelatedDtoField


def child_validator(value):
    try:
        int(value)
    except ValueError:
        raise serializers.ValidationError("Should be integer")


class ChildDto(BaseDto):
    child_param_1 = serializers.CharField(required=True, validators=[child_validator])


class ParentDto(BaseDto):
    param_1 = serializers.CharField(required=True, validators=[child_validator])
    child = RelatedDtoField(ChildDto, required=False)
