from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class CounterParty(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=False)
    legal_address = fields.TextField(null=False)
    actual_address = fields.TextField(null=False)
    TIN = fields.CharField(max_length=128, null=False)
    KPP = fields.CharField(max_length=128, null=False)
    OGRN = fields.CharField(max_length=128, null=False)
    OKPO = fields.CharField(max_length=128, null=False)
    cur_id = fields.IntField()
    ec_indic_id = fields.IntField()


class Currencies(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=False)
    rate = fields.CharField(max_length=50, null=False)


class EconomicIndicators(models.Model):
    id = fields.IntField(pk=True)
    revenue = fields.IntField()
    expenses = fields.IntField()
    net_income = fields.IntField()
    assets = fields.IntField()
    liabilities = fields.CharField(max_length=50, null=False)
    capital = fields.IntField()


CounterParty_Pydantic = pydantic_model_creator(CounterParty, name="CounterParty")
CounterPartyIn_Pydantic = pydantic_model_creator(CounterParty, name="CounterPartyIn", exclude_readonly=True)

Currencies_Pydantic = pydantic_model_creator(Currencies, name="Currencies")
CurrenciesIn_Pydantic = pydantic_model_creator(Currencies, name="CurrenciesIn", exclude_readonly=True)

EconomicIndicators_Pydantic = pydantic_model_creator(EconomicIndicators, name="EconomicIndicators")
EconomicIndicatorsIn_Pydantic = pydantic_model_creator(EconomicIndicators, name="EconomicIndicatorsIn", exclude_readonly=True)
