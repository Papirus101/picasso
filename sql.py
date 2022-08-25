DATABASE_EXISTS = """
SELECT EXISTS (SELECT relname FROM pg_class WHERE relname = '{table_name}');
"""

CREATE_TABLE = """
CREATE TABLE {table_name} (
        crime_id bigserial primary key,
        original_crime_type_name varchar(150) NOT NULL,
        report_date timestamp NOT NULL,
        call_date timestamp NOT NULL,
        offense_date timestamp NOT NULL,
        call_time TIME NOT NULL,
        call_date_time timestamp NOT NULL,
        disposition varchar(50) NOT NULL,
        address varchar(50) NOT NULL,
        city varchar(50),
        state varchar(50),
        agency_id integer NOT NULL,
        address_type varchar(50) NOT NULL,
        common_location varchar(50)
        );
"""

INSERT_DATA="""
INSERT INTO {table_name}
VALUES ({crime_id}, '{original_crime_type_name}',
        '{report_date}', '{call_date}', '{offense_date}',
        '{call_time}', '{call_date_time}', '{disposition}',
        '{address}', '{city}', '{state}', {agency_id}, '{address_type}',
        '{common_location}');
"""


SELECT_DATA = """
SELECT *
FROM {table_name}
{where_date}
LIMIT 20
OFFSET {offset}
"""
