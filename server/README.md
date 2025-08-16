# Todo Server

```bash
uv run uvicorn main:app --app-dir src --host 0.0.0.0 --reload 
```

## Alembic

- init alembic

    ```bash
    # uv run alembic init <directory>
    uv run alembic init migrations
    ```

- check current migration and history

    ```bash
    uv run alembic current # current
    uv run alembic history [--verbose] # history
    ```

- create migration

    ```bash
    uv run alembic revision --autogenerate -m "Create todo table"
    ```

