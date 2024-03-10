import logging

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from .api.v1.api_v1 import api_router as api_v1
from .errors.error_handler import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

from .middleware.log_requests import log_requests

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

app.middleware("http")(log_requests)


app.include_router(api_v1, prefix="/api/v1")
