import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(Path(__file__).parent / '.env')
from registry import router
from settings import public_config

logging.basicConfig(level=logging.INFO)
client = AsyncIOMotorClient(os.environ['MONGO_URL'])
db = client[os.environ['DB_NAME']]


@asynccontextmanager
async def lifespan(app):
    public_config()
    await db.agents.create_index('handle_key', unique=True)
    await db.agents.create_index('ref_code', unique=True)
    await db.agents.create_index('request_id', unique=True)
    await db.agents.create_index('created_at')
    await db.counters.create_index('name', unique=True)
    await db.counters.update_one({'name': 'agent_number'}, {'$setOnInsert': {'value': 0}}, upsert=True)
    app.state.db = db
    yield
    client.close()


app = FastAPI(title='LastZhood Survivor Registry', lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ['CORS_ORIGINS'].split(','),
    allow_credentials=False,
    allow_methods=['GET', 'POST'],
    allow_headers=['Content-Type'],
)
app.include_router(router, prefix='/api')


@app.get('/api/')
async def root():
    return {'service': 'LastZhood Survivor Registry', 'status': 'online'}