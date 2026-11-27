SOURCES = {
    "customer": "raw/customer.csv",
    # ... employees, suppliers, shippers, products
    "orders": "raw/orders.csv",
    "order_details": "raw/order_details.csv",
    "legacy_orders": "legacy/orders.csv",
    "legacy_order_details":
    "legacy/order_details.csv",
    }
con = duckdb.connect(str(DB_PATH))
con.execute("CREATE SCHEMA IF NOT EXISTS raw")
for table, path in SOURCES.items():
    csv_path = DATA_DIR / path
    con.execute(f"""
    CREATE OR REPLACE TABLE raw.{table} AS
    SELECT *
    FROM read_csv('{csv_path.as_posix()}',
    header = true)
    """)
    n = con.execute(
    f"SELECT COUNT(*) FROM raw.{table}"
    ).fetchall()[0][0]
    print(f"raw.{table} {n} rows")