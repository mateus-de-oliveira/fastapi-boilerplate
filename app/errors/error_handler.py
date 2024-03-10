import logging

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)

def validation_exception_handler(exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"errors": exc.errors()},
    )

def http_exception_handler(exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "errors": [{
                "title": exc.detail,
                "detail": exc.detail
            }]
        }
    )

def general_exception_handler(exc: Exception):
    logger.error(f"Internal Server Error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "errors": [{
                "title": "Internal Server Error",
                "detail": "An unexpected error occurred."
            }]
        }
    )
