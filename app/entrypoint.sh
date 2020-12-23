#!/bin/bash
sleep 2s

python3.8 load_data.py

pytest

uvicorn main:app --host 0.0.0.0 --port 80 --reload





