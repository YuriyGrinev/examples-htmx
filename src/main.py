from apps.base import app_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def include_router(app):
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title="HTMX Example", version="0.0.1")
    include_router(app)
    configure_staticfiles(app)
    return app


app = start_application()
