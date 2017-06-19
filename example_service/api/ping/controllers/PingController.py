from api_commons.common import ApiResponse
from example_service.api.common import ExampleController


class PingController(ExampleController):
    def get(self, request):
        return ApiResponse.success()