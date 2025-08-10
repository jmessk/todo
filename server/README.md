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

- create migration

    ```bash
    uv run alembic revision --autogenerate -m "initial migration"
    ```
