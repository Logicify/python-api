from rest_framework import serializers

from api_commons.dto import BaseDto
from example_service.core.services import CalculationService
from example_service.core.services.CalculationService import CalculationResult


class CalculationRequestDto(BaseDto):
    arg1 = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)
    arg2 = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)
    operator = serializers.ChoiceField(required=True, choices=CalculationService.Operator.choices)


class CalculationResultDto(BaseDto):
    result = serializers.DecimalField(required=False, max_digits=5, decimal_places=2)
    result_int = serializers.IntegerField(required=False)
    result_str = serializers.IntegerField(required=False)

    @classmethod
    def from_calculation_result(cls, calculation_result: CalculationResult):
        dto = cls()
        dto.result = calculation_result.answer
        dto.result_int = int(calculation_result.answer)
        dto.result_str = str(calculation_result.answer)
        return dto
