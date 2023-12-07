import os
from .models import *
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from starlette.exceptions import HTTPException
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
async_DB = os.getenv('DB_URI', "asyncpg://admin:123456@localhost/Space_team_project")


class Status(BaseModel):
    message: str


# models of "CounterParty" table:
@app.get("/counterparty/", response_model=List[CounterParty_Pydantic])
async def get_counterparty_list():
    return await CounterParty_Pydantic.from_queryset(CounterParty.all())


@app.get("/counterparty/{counterparty_id}", response_model=CounterParty_Pydantic)
async def get_counterparty(counterparty_id: int):
    return await CounterParty_Pydantic.from_queryset_single(CounterParty.get(id=counterparty_id))


@app.post("/counterparty/", response_model=CounterParty_Pydantic)
async def add_counterparty(counterparty: CounterPartyIn_Pydantic):
    counterparty_obj = await CounterParty.create(**counterparty.model_dump(exclude_unset=True))
    return await CounterParty_Pydantic.from_tortoise_orm(counterparty_obj)


@app.delete("/counterparty/{counterparty_id}", response_model=Status)
async def delete_counterparty(counterparty_id: int):
    delete_counterparty_stroke = await CounterParty.filter(id=counterparty_id).delete()
    if not delete_counterparty_stroke:
        raise HTTPException(status_code=404, detail=f"User {counterparty_id} not found")
    return Status(message=f"Deleted counterparty {counterparty_id}")


@app.put("/counterparty/{counterparty_id}", response_model=CounterParty_Pydantic)
async def update_user(counterparty_id: int, counterparty: CounterPartyIn_Pydantic):
    await CounterParty.filter(id=counterparty_id).update(**counterparty.model_dump(exclude_unset=True))
    return await CounterParty_Pydantic.from_queryset_single(CounterParty.get(id=counterparty_id))


# models of "Currencies" table:
@app.get("/currencies/", response_model=List[Currencies_Pydantic])
async def get_currencies_list():
    return await Currencies_Pydantic.from_queryset(Currencies.all())


@app.get("/currencies/{currencies_id}", response_model=Currencies_Pydantic)
async def get_currencies(currencies_id: int):
    return await Currencies_Pydantic.from_queryset_single(Currencies.get(id=currencies_id))


@app.post("/currencies/", response_model=Currencies_Pydantic)
async def add_currency(currencies: CurrenciesIn_Pydantic):
    currency_obj = await Currencies.create(**currencies.model_dump(exclude_unset=True))
    return await Currencies_Pydantic.from_tortoise_orm(currency_obj)


@app.delete("/currencies/{currency_id}", response_model=Status)
async def delete_currencies(currency_id: int):
    delete_currency_stroke = await Currencies.filter(id=currency_id).delete()
    if not delete_currency_stroke:
        raise HTTPException(status_code=404, detail=f"User {currency_id} not found")
    return Status(message=f"Deleted currency {currency_id}")


@app.put("/currencies/{currencies_id}", response_model=Currencies_Pydantic)
async def update_user(currency_id: int, currencies: CurrenciesIn_Pydantic):
    await Currencies.filter(id=currency_id).update(**currencies.model_dump(exclude_unset=True))
    return await Currencies_Pydantic.from_queryset_single(Currencies.get(id=currency_id))


# models of "EconomicIndicators" table:
@app.get("/economicindicators/", response_model=List[EconomicIndicators_Pydantic])
async def get_economic_indicators_list():
    return await EconomicIndicators_Pydantic.from_queryset(EconomicIndicators.all())


@app.get("/economicindicators/{economicindicator_id}", response_model=EconomicIndicators_Pydantic)
async def get_economic_indicator(economicindicator_id: int):
    return await EconomicIndicators_Pydantic.from_queryset_single(EconomicIndicators.get(id=economicindicator_id))


@app.post("/economicindicators/", response_model=EconomicIndicators_Pydantic)
async def add_economicindicator(economicindicators: EconomicIndicatorsIn_Pydantic):
    economicindicator_obj = await EconomicIndicators.create(**economicindicators.model_dump(exclude_unset=True))
    return await EconomicIndicators_Pydantic.from_tortoise_orm(economicindicator_obj)


@app.delete("/economicindicators/{economicindicator_id}", response_model=Status)
async def delete_currencies(economicindicator_id: int):
    delete_currency_stroke = await EconomicIndicators.filter(id=economicindicator_id).delete()
    if not delete_currency_stroke:
        raise HTTPException(status_code=404, detail=f"User {economicindicator_id} not found")
    return Status(message=f"Deleted currency {economicindicator_id}")


@app.put("/economicindicators/{economicindicator_id}", response_model=EconomicIndicators_Pydantic)
async def update_user(economicindicator_id: int, economicindicators: EconomicIndicatorsIn_Pydantic):
    await EconomicIndicators.filter(id=economicindicator_id).update(**economicindicators.model_dump(exclude_unset=True))
    return await EconomicIndicators_Pydantic.from_queryset_single(EconomicIndicators.get(id=economicindicator_id))


register_tortoise(
    app,
    db_url=async_DB,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
