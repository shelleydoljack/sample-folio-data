import os
import pathlib
import json

from folioclient import FolioClient

okapi_url = os.getenv("OKAPI_URL")
user = os.getenv("OKAPI_USER")
password = os.getenv("OKAPI_PASSWORD")
tenant = os.getenv("TENANT")

folio_client = FolioClient(okapi_url, tenant, user, password)

data_types = [
    "users",
    "bills",
    "loans",
    "circulation-logs",
    "requests",
    "instances",
    "holdings",
    "items",
    "financial-transactions",
    "funds",
    "budgets",
    "invoices",
    "invoice-lines",
    "orders",
    "order-lines",
    "receiving-history",
    "organizations",
    "interfaces",
    "notes",
    "tags",
]

count = 10


def _write_data(file_path: pathlib.Path, data_type: str, data: list) -> bool:
    data_dict = {}
    data_dict[data_type] = data
    try:
        with open(file_path, "w") as f:
            json.dump(data_dict, f)

        return True
    except Exception as e:
        print(e)
        return False


def main(**kwargs):
    data_types = kwargs.get("data_types")
    count = kwargs.get("count")
    for data in data_types:
        print(f"Getting {count} random folio records for {data}")
        file_path = pathlib.Path(".") / f"{data}.json"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        match data:
            case "users":
                random_data = folio_client.get_random_objects("/users", count=count)
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "bills":
                random_data = folio_client.get_random_objects("/accounts", count=count)
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "loans":
                random_data = folio_client.get_random_objects(
                    "/circulation/loans", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "circulation-logs":
                random_data = folio_client.get_random_objects(
                    "/audit-data/circulation/logs", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "requests":
                random_data = folio_client.get_random_objects(
                    "/circulation/requests", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "instances":
                random_data = folio_client.get_random_objects(
                    "/instance-storage/instances", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "holdings":
                random_data = folio_client.get_random_objects(
                    "/holdings-storage/holdings", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "items":
                random_data = folio_client.get_random_objects(
                    "/item-storage/items", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "financial-transactions":
                random_data = folio_client.get_random_objects(
                    "/finance-storage/transactions", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "funds":
                random_data = folio_client.get_random_objects(
                    "/finance-storage/funds", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "budgets":
                random_data = folio_client.get_random_objects(
                    "/finance-storage/budgets", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "invoices":
                random_data = folio_client.get_random_objects(
                    "/invoice-storage/invoices", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "invoice-lines":
                random_data = folio_client.get_random_objects(
                    "/invoice-storage/invoice-lines", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "orders":
                random_data = folio_client.get_random_objects(
                    "/orders-storage/purchase-orders", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "order-lines":
                random_data = folio_client.get_random_objects(
                    "/orders-storage/po-lines", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "receiving-history":
                random_data = folio_client.get_random_objects(
                    "/orders-storage/receiving-history", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "organizations":
                random_data = folio_client.get_random_objects(
                    "/organizations-storage/organizations", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "interfaces":
                random_data = folio_client.get_random_objects(
                    "/organizations-storage/interfaces", count=count
                )
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "notes":
                random_data = folio_client.get_random_objects("/notes", count=count)
                _write_data(file_path=file_path, data_type=data, data=random_data)
            case "tags":
                random_data = folio_client.get_random_objects("/tags", count=count)
                _write_data(file_path=file_path, data_type=data, data=random_data)
    return None

main(data_types=data_types, count=count)
