from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "counterparty" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "legal_address" TEXT NOT NULL,
    "actual_address" TEXT NOT NULL,
    "TIN" VARCHAR(128) NOT NULL,
    "KPP" VARCHAR(128) NOT NULL,
    "OGRN" VARCHAR(128) NOT NULL,
    "OKPO" VARCHAR(128) NOT NULL,
    "cur_id" INT NOT NULL,
    "ec_indic_id" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "currencies" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "rate" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "economicindicators" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "revenue" INT NOT NULL,
    "expenses" INT NOT NULL,
    "net_income" INT NOT NULL,
    "assets" INT NOT NULL,
    "liabilities" VARCHAR(50) NOT NULL,
    "capital" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
