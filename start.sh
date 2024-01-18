#!/usr/bin/env bash

alembic upgrade head
uvicorn src.main:app --proxy-headers --reload --host 0.0.0.0 --port 80