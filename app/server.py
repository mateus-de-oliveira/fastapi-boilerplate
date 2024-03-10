import logging
import time
import random
import string
from fastapi import Request
from fastapi import FastAPI
from .api.v1.api_v1 import api_router as api_v1

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = f'{process_time:.2f}'
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    return response

app.include_router(api_v1, prefix="/api/v1")
