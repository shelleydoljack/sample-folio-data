## Environmental Variables 
After cloning/copying this repository, create a local .env file and add the following variables
to use in your notebook:

```bash
export OKAPI_URL=https://okapi-url
export OKAPI_USER=username
export OKAPI_PASSWORD=password
export TENANT=tenant
```

## Installation
To run these examples, you'll need a version of Python 3.11 or later and poetry installed on your local
machine.
- `poetry install`
- `source .env`
- `poetry run python sample_folio_data.py`