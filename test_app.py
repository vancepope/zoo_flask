import os
import sys
import pytest
import logging
import psycopg2
from db import queries
from dotenv import load_dotenv
from unittest.mock import Mock

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    handlers=[
        logging.FileHandler(r'test_app.log')
    ]
)
test_db_url = os.getenv("TEST_DATABASE_URL")

@pytest.fixture
def enclosure():
    conn = psycopg2.connect(test_db_url)
    cursor = conn.cursor()
    sample_data = [
        ('Birds','Birds'),
        ('Apes', 'Apes'),
    ]
    cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
    cursor.executemany(queries.INSERT_ENCLOSURE, sample_data)
    yield conn, cursor

def test_connection(enclosure):
    logging.info('Starting the connection test')
    conn, cursor = enclosure
    with conn:
        cursor.execute(queries.SELECT_ENCLOSURES)
        result = cursor.fetchmany(2)
        print(result, flush=True)
        assert len(result) == 2
        logging.info(result)

@pytest.fixture
def add_animal():
    conn = psycopg2.connect(test_db_url)
    cursor = conn.cursor()
    sample_data = [
        ('Eagle', 10, 1, 'Eagle'),
        ('Gorilla', 5, 2, 'Gorilla'),
    ]
    cursor.execute(queries.CREATE_ANIMALS_TABLE)
    cursor.executemany(queries.INSERT_ANIMAL, sample_data)
    yield conn, cursor
    
def test_add_animal(add_animal):
    logging.info('Starting the add_animal test')
    conn, cursor = add_animal
    with conn:
        cursor.execute(queries.SELECT_ANIMALS)
        result = cursor.fetchmany(2)
        print(result, flush=True)
        assert len(result) == 2
        logging.info(result)

# def create_animal():
#     data = request.get_json()
#     name = data["name"]
#     quantity = data["quantity"]
#     enclosure_id = data["enclosure_id"]
#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute(queries.CREATE_ANIMALS_TABLE)
#             cursor.execute(queries.INSERT_ENCLOSURE, (name, quantity, enclosure_id))

#     return {"name": f"Enclosure {name} created."}, 201

# def test_create_animal(self):
    