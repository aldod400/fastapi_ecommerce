from fastapi import HTTPException


class BadRequestError(HTTPException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(status_code=400, detail=message)


class NotFoundError(HTTPException):
    def __init__(self, message: str = "Not found"):
        super().__init__(status_code=404, detail=message)


class ConflictError(HTTPException):
    def __init__(self, message: str = "Conflict"):
        super().__init__(status_code=409, detail=message)


class UnauthorizedError(HTTPException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(status_code=401, detail=message)


class ForbiddenError(HTTPException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(status_code=403, detail=message)


class InternalServerError(HTTPException):
    def __init__(self, message: str = "Internal server error"):
        super().__init__(status_code=500, detail=message)


class ServiceUnavailableError(HTTPException):
    def __init__(self, message: str = "Service unavailable"):
        super().__init__(status_code=503, detail=message)


class ValidationError(HTTPException):
    def __init__(self, message: str = "Validation error"):
        super().__init__(status_code=422, detail=message)
