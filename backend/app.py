# builtin
import random
import time
import asyncio
import sys
import os
from contextlib import asynccontextmanager

# external
from fastapi import FastAPI
from openai import AsyncOpenAI, completions
from fastapi.middleware.cors import CORSMiddleware


# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


# internal imports
from src.globals.environment import Environment
from src.api.routes import router
from src.modules.classifier import ClassifierModule


def setup_clients(app: FastAPI):
    environment: Environment = app.state.environment
    openai_client: AsyncOpenAI = AsyncOpenAI(api_key=app.state.environment.OPENAI_KEY)
    app.state.openai_client = openai_client


def setup_globals(app: FastAPI):
    enviornment: Environment = Environment()
    app.state.environment = enviornment


def setup_modules(app: FastAPI):
    classifier_module: ClassifierModule = ClassifierModule(
        openai_client=app.state.openai_client
    )
    app.state.classifier_module = classifier_module


@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup
    setup_globals(app=app)
    setup_clients(app=app)
    setup_modules(app=app)
    yield


app: FastAPI = FastAPI(lifespan=lifespan)
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
