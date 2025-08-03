from clickhouse_connect import get_client

def get_clickhouse_client():
    return get_client(
        host="clickhouse-server",
        port=8123,
        username="default",
        password="",
        database="analytics"
    )
