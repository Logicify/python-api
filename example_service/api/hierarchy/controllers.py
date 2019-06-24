from django.http import HttpRequest

from api_commons.decorator import inject_dto
from example_service.api import errors
from api_commons.common import ApiResponse
from example_service.api.calculator.dto import CalculationRequestDto, CalculationResultDto
from example_service.api.common import ExampleController
from example_service.api.hierarchy.dto import ParentDto
from example_service.core.services import CalculationService


class HierarchyController(ExampleController):
    def get(self, request: HttpRequest):
        return ApiResponse.not_found(errors.NOT_SUPPORTED)

    @inject_dto(ParentDto)
    def post(self, request: HttpRequest, dto: ParentDto):
        if not dto.is_valid():
            return ApiResponse.bad_request(dto)
        return ApiResponse.success(dto)
