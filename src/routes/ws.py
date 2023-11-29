#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; tab-width: 4 -*-
# vim: ft=python fenc=utf-8
#
# Author: Daniel Isaksen <d@duniel.no>
#

from fastapi import (
    APIRouter,
    WebSocket,
    Request,
)

router = APIRouter()

@router.websocket("/")
async def hello(req: Request, ws: WebSocket):
    ...

