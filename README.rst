      sh -c "python -m pip install --upgrade pip && 
             pip install poetry==1.0.5 && 
             poetry update && 
             poetry install && 
             poetry run uvicorn exchangeapi.bootstrap:app --host=0.0.0.0 --port=9090 --reload --debug --log-level=debug"
