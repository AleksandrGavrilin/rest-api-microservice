import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from app.main import app
from app.models import CounterParty, Currencies, EconomicIndicators


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="module")
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as c:
            yield c

# Checking the functionality of models:
@pytest.mark.anyio
async def test_counterparty(client: AsyncClient):
    response = await client.post("/counterparty/", json={"name": "admin", "legal_address": "gergerge", "actual_address": "cvbcvbcv",
                                                            "TIN": "456456456", "KPP": "gerge12323534gfrge",
                                                            "OGRN": "ger546457hhgerge", "OKPO": "efbgthyuk7686",
                                                            "cur_id": 1, "ec_indic_id": 1, })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "admin"
    assert "id" in data
    counterparty_id = data["id"]

    counterparty_obj = await CounterParty.get(id=counterparty_id)
    assert counterparty_obj.id == counterparty_id

    response = await client.get(f"/counterparty/{counterparty_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "admin"

    response = await client.delete(f"/counterparty/{counterparty_id}")
    assert response.status_code == 200, response.text


@pytest.mark.anyio
async def test_currencies(client: AsyncClient):
    response = await client.post("/currencies/",
                                 json={"name": "Canadian dollar", "rate": "0.7377", })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Canadian dollar"
    assert "id" in data
    currencies_id = data["id"]

    currencies_obj = await Currencies.get(id=currencies_id)
    assert currencies_obj.id == currencies_id

    response = await client.get(f"/currencies/{currencies_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Canadian dollar"

    response = await client.delete(f"/currencies/{currencies_id}")
    assert response.status_code == 200, response.text


@pytest.mark.anyio
async def test_economicindicators(client: AsyncClient):  # nosec
    response = await client.post("/economicindicators/",
                                 json={"revenue": 11111111, "expenses": 2222, "net_income": 33333,
                                       "assets": 4, "liabilities": "aaa",
                                       "capital": 555555,})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["revenue"] == 11111111
    assert "id" in data
    economicindicators_id = data["id"]

    economicindicators_obj = await EconomicIndicators.get(id=economicindicators_id)
    assert economicindicators_obj.id == economicindicators_id

    response = await client.get(f"/economicindicators/{economicindicators_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["revenue"] == 11111111

    response = await client.delete(f"/economicindicators/{economicindicators_id}")
    assert response.status_code == 200, response.text

