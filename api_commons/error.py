class InvalidInputDataError(Exception):
    def __init__(self, msg, input_value, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.input_value = input_value


class InvalidPaginationOptionsError(Exception):
    pass


class NotFoundException(Exception):
    def __init__(self, msg, input_value, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.input_value = input_value


class ErrorCode:
    def __init__(self, error_code, dto_or_error_message=''):
        self.error_code = error_code
        self.dto_or_error_message = dto_or_error_message
