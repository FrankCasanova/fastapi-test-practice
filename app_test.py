import pytest


import asyncio

import httpx
import pytest
from asgi_lifespan import LifespanManager
import pytest_asyncio

from app import app


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
    

@pytest_asyncio.fixture
async def test_client():
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url='http://localhost:8000') as test_client:
            yield test_client


@pytest.mark.asyncio
async def test_hello_world(test_client: httpx.AsyncClient):
    response = await test_client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}            