from django.http import HttpRequest

from example_service.api import errors
from api_commons.common import ApiResponse
from example_service.api.calculator.dto import CalculationRequestDto, CalculationResultDto
from example_service.api.common import ExampleController
from example_service.core.services import CalculationService


class SumController(ExampleController):
    def get(self, request: HttpRequest):
        return ApiResponse.not_found(errors.NOT_SUPPORTED)

    def post(self, request: HttpRequest):
        dto = CalculationRequestDto.from_dict(request.data)
        if not dto.is_valid():
            return ApiResponse.bad_request(dto)
        task = CalculationService.CalculationTask(arg1=dto.arg1, arg2=dto.arg2, operator=dto.operator)
        try:
            result = CalculationService.calculate(task)
            return ApiResponse.success(
                CalculationResultDto.from_calculation_result(result)
            )
        except Exception as e: # Should be more concrete
            return ApiResponse.bad_request("Unable to calculate your expression: " + str(e))