import asyncio
from typing import Any, Dict

import httpx
import pytest
from asgi_lifespan import LifespanManager
from fastapi import status

from external_api import app, external_api


class MockExternalAPI:
    mock_data = {
        "data": [
            {
                "employee_age": 61,
                "employee_name": "Tiger Nixon",
                "employee_salary": 320800,
                "id": 1,
                "profile_image": "",
            }
        ],
        "status": "success",
        "message": "Success",
    }
    
    
    async def __call__(self,) -> Dict[str, Any]:
        return MockExternalAPI.mock_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def test_client():
    app.dependency_overrides[external_api] = MockExternalAPI()
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://localhost:8000") as test_client:
            yield test_client    


@pytest.mark.asyncio
async def test_get_employees(test_client: httpx.AsyncClient):
    response = await test_client.get("/employees")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == MockExternalAPI.mock_data            