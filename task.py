import os
import csv
import psycopg2
import time

from progress.bar import IncrementalBar
from sql import CREATE_TABLE, DATABASE_EXISTS, INSERT_DATA
from dotenv import load_dotenv
from loguru import logger

load_dotenv('.env')
logger.add("file_{time}.log")

def get_total_lines(filename):
    file = open(filename)
    numline = len(file.readlines())
    return numline

def db_connect():
    conn = psycopg2.connect(
                    host=os.getenv('DB_HOST'),
                    database=os.getenv('DB_NAME'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASS')
                    )
    cur = conn.cursor()
    return conn, cur


def check_table_exist(conn, cur):
    cur.execute(DATABASE_EXISTS.format(
        table_name=os.getenv('TABLE_NAME')
        ))
    b = cur.fetchone()
    if b is not None and not b[0]:
        logger.info('CREATE TABLE')
        cur.execute(CREATE_TABLE.format(
            table_name=os.getenv('TABLE_NAME')
            ))
        conn.commit()


def parse_file(filename):
    logger.info('START PARSE CSV')
    time_start = time.time()
    total_count_lines = get_total_lines(filename)
    bar = IncrementalBar('Вставляем данные в БД:', max=total_count_lines,  suffix='%(percent)d%%')
    conn, cur = db_connect()
    check_table_exist(conn, cur)
    with open(filename, 'r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            formatted_dict = {f"{'_'.join(k.lower().split())}": int(row[k]) if row[k].isdigit() else row[k].replace("'", ' ') for k in row}
            sql = INSERT_DATA.format(
                    table_name=os.getenv('TABLE_NAME'),
                    **formatted_dict)
            cur.execute(sql)
            conn.commit()
            bar.next()
        bar.finish()
        logger.info(f'PARSE FINISH, total time: {time.time() - time_start} s.\n' \
                f'total_records: {total_count_lines}')

if __name__ == "__main__":
    parse_file(f"{os.getcwd()}/police-department-calls-for-service.csv")
