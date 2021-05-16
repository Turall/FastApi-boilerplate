import string
import random
import time
import logging

from fastapi import FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from core.extensions import db
from core.factories import settings
from app.controllers.controller.controller import router


app = FastAPI()
db.init_app(app)
log = logging.getLogger(__name__)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """log_requests.

    :param request:
    :type request: Request
    :param call_next:
    """
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    log.info(
        f"RID={idem} REGION={request.headers.get('cf-ipcountry')} CLIENT_IP={request.headers.get('cf-connecting-ip')} START REQUEST PATH={request.url.path} METHOD={request.method} "
    )
    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    log.info(
        f"RID={idem} COMPLETED={formatted_process_time}ms REQUEST={request.method.upper()} {request.url.path} STATUS_CODE={response.status_code}"
    )

    return response


@app.on_event("startup")
async def startup():
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    print("SHUTDOWN")


cors_origins = [i.strip() for i in settings.CORS_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)
app.include_router(router)
