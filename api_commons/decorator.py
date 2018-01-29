from api_commons.common import ApiResponse


def inject_dto(dto_class, dto_object_name: str = 'dto'):
    def dto_decorator(func):
        def wrapped(*args, **kwargs):
            request = args[1]
            dto_object = dto_class.from_dict(request.data)
            if not dto_object.is_valid():
                return ApiResponse.bad_request(dto_object)
            kwargs[dto_object_name] = dto_object
            return func(*args, **kwargs)

        return wrapped

    return dto_decorator
