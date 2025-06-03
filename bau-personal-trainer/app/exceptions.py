from fastapi import HTTPException

class UserError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class DatabaseError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class DuplicateEmailError(UserError):
    pass

class ValidationError(UserError):
    pass 