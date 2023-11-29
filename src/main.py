#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; tab-width: 4 -*-
# vim: ft=python fenc=utf-8
#
# Author: Daniel Isaksen <d@duniel.no>
#

import asyncio
import contextlib
import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import config
from routes import (api, ws)

@contextlib.asynccontextmanager
async def lifespan(app):
    # Save for later.
    app.config = config
    app.logger = logging.getLogger(app.config.app_name)

    yield

app = FastAPI(
    title=config.app_name,
    version=config.version,

    docs_url="/api/docs",
    # Disable ReDoc when we have Swagger.
    redoc_url=None,
    openapi_url="/api/openapi.json",

    # Don't redirect `/hello` to `/hello/`
    redirect_slashes=False,

    # Lifecycle hooks.
    lifespan=lifespan,
)

# WebSockets
app.include_router(
    prefix="/ws",
    router=ws.router,
)

# API
app.include_router(
    prefix="/api/v1",
    router=api.router,
)

# Static frontend
app.mount(
    path="/",
    app=StaticFiles(directory="static", html=True),
    name="frontend",
)
