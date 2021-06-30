#!/bin/sh
gunicorn --workers 2 --threads 2 -b 0.0.0.0:8080 app:app