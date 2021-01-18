from fastapi import FastAPI
from starlette_prometheus import metrics, PrometheusMiddleware
from app.controllers.controller.controller import router
from starlette.middleware.cors import CORSMiddleware
from sentry_sdk import init as initialize_sentry
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from core.factories import settings
from core.extensions import db
from starlette.requests import Request


app = FastAPI()
db.init_app(app)


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
app.add_route("/metrics/",metrics)
app.include_router(router)


