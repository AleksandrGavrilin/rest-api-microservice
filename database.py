TORTOISE_MODELS_LIST = ["app.models", "aerich.models"]
TORTOISE_ORM = {
    "connections": {
           # "default": "postgres://testuser:test1234@localhost/TortoiseDB"
           "default": "postgres://admin:123456@postgres_container/Space_team_project"
    },
    "apps": {
            "models": {
                "models": TORTOISE_MODELS_LIST,
                "default_connection": "default",
            },
        },
}
