#!/bin/bash

echo "=Starting runserver="
uvicorn main:app --reload --bind 0.0.0.0:8001
