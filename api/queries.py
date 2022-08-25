import asyncpg
import os

async def get_db_conntection():
    conn = await asyncpg.connect(
                    host=os.getenv('DB_HOST'),
                    database=os.getenv('DB_NAME'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASS')
                    )
    return conn


def generate_where_date(date_from, date_to):
    where_statement = ""
    if date_from is not None:
        where_statement += f"WHERE report_date >= '{date_from}'"
    if date_to is not None and where_statement:
        where_statement += f" AND report_date <= '{date_to}'"
    return where_statement


async def get_data(sql: str):
    cur = await get_db_conntection()
    data = await cur.fetch(sql)
    return data
