import sys
import types

# Temporary patch if 'ssl' module is not available in sandbox environments
if 'ssl' not in sys.modules:
    sys.modules['ssl'] = types.SimpleNamespace()

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="PDF Question Extractor")

app.include_router(router)
