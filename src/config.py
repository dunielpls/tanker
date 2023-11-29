#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; tab-width: 4 -*-
# vim: ft=python fenc=utf-8
#
# Author: Daniel Isaksen <d@duniel.no>
#

from pydantic import CockroachDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    app_name: str = "Tanker"
    version: str = "0.1.0"

    database_uri: CockroachDsn = "cockroachdb+asyncpg://root@127.0.0.1:26257/defaultdb?sslmode=disable"
    # "postgresql://root@127.0.0.1:26257/defaultdb?sslmode=verify-full&sslrootcert={root-cert}&sslcert={client-cert}&sslkey={client-key}"

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        case_sensitive=False,
        secrets_dir="/run/secrets",
    )

config = Config()
