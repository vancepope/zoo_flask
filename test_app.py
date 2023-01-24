import os
import sys
import pytest
import logging
import psycopg2
from db import queries
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    handlers=[
        logging.FileHandler(r'test_app.log')
    ]
)
test_db_url = os.getenv("TEST_DATABASE_URL")

conn = psycopg2.connect(test_db_url)

@pytest.fixture
def connection():
    cursor = conn.cursor()
    sample_data = [
        {"group_name": 'Birds'},
        {"group_name":'Apes'},
    ]
    cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
    cursor.executemany(queries.INSERT_ENCLOSURE, sample_data)
    yield conn, cursor
def test_connection(connection):
    logging.info('Starting the connection test')
    conn, cursor = connection
    with conn:
        cursor.execute(queries.SELECT_ENCLOSURES)
        result = cursor.fetchmany(2)
        print(f"Expected Output: length > 0 | Output: {len(result)}")
        assert len(result) > 0
        logging.info(f"Expected Output: length > 0 | Output: {len(result)}")

@pytest.fixture
def create_animals():
    cursor = conn.cursor()
    sample_data = [
        {"name": "Eagle", "quantity":10, "enclosure_id":1},
        {"name": "Gorilla", "quantity": 5, "enclosure_id": 2},
    ]
    cursor.execute(queries.CREATE_ANIMALS_TABLE)
    cursor.executemany(queries.INSERT_ANIMAL, sample_data)
    yield conn, cursor
def test_create_animals(create_animals):
    logging.info('Starting the create_animals test')
    conn, cursor = create_animals
    with conn:
        cursor.execute(queries.SELECT_ANIMALS)
        result = cursor.fetchmany()
        print(f"Expected Output: length > 0 | Output: {len(result)} ")
        assert len(result) > 0
        logging.info(f"Expected Output: length > 0 | Output: {len(result)}")

@pytest.fixture
def create_enclosures():
    cursor = conn.cursor()
    sample_data = [
        {"group_name": "Dogs"},
        {"group_name": "Cats"},
    ]
    cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
    cursor.executemany(queries.INSERT_ENCLOSURE, sample_data)
    yield conn, cursor   
def test_create_enclosures(create_enclosures):
    logging.info('Starting the create_enclosures test')
    conn, cursor = create_enclosures
    with conn:
        cursor.execute(queries.SELECT_ENCLOSURES)
        result = cursor.fetchmany()
        print(f"Expected Output: length > 0 | Output: {len(result)}")
        assert len(result) > 0
        logging.info(f"Expected Output: length > 0 | Output: {len(result)}")

@pytest.fixture
def create_animal_foods():
    cursor = conn.cursor()
    sample_data = [
        {"food": "Banana", "food_type": "Fruit"},
        {"food": "Steak", "food_type": "Meat"},
    ]
    cursor.execute(queries.CREATE_ANIMAL_FOODS_TABLE)
    cursor.executemany(queries.INSERT_ANIMAL_FOOD, sample_data)
    yield conn, cursor
def test_create_animal_foods(create_animal_foods):
    logging.info('Starting the create_animal_foods test')
    conn, cursor = create_animal_foods
    with conn:
        cursor.execute(queries.SELECT_ANIMAL_FOODS)
        result = cursor.fetchmany()
        print(f"Expected Output: length == 2 | Output: {cursor.rowcount} ")
        assert cursor.rowcount == 2
        logging.info(f"Expected Output: length == 2 | Output: {cursor.rowcount}")
        
@pytest.fixture
def add_enclosure():
    cursor = conn.cursor()
    sample_data = [
        {"group_name": "Bears" },
        {"group_name": "Snakes"},
        {"group_name": "Frogs"},
    ]
    cursor.executemany(queries.INSERT_ENCLOSURE, sample_data)
    yield conn, cursor
def test_add_enclosure(add_enclosure):
    logging.info('Starting the add_enclosure test')
    conn, cursor = add_enclosure
    with conn:
        cursor.execute(queries.SELECT_ANIMALS)
        result = cursor.fetchmany()
        assert len(result) == 1
        print(f"Expected Output: length == 1 | Output: length == {len(result)}")
        logging.info(f"Expected Output: length == 1 | Output: length == {len(result)}")
        
@pytest.fixture
def add_animal():
    cursor = conn.cursor()
    sample_data = [
        {"name": "Pitbull", "quantity": 4, "enclosure_id": 3},
        {"name": "Lion", "quantity": 6, "enclosure_id": 4},
        {"name":"Tiger", "quantity": 2, "enclosure_id": 4},
    ]
    cursor.executemany(queries.INSERT_ANIMAL, sample_data)
    yield conn, cursor  
def test_add_animal(add_animal):
    logging.info('Starting the add_animal test')
    conn, cursor = add_animal
    with conn:
        cursor.execute(queries.SELECT_ANIMALS)
        result = cursor.fetchmany()
        assert len(result) == 1
        print(f"Expected Output: length == 1 | Output: length == {len(result)}")
        logging.info(f"Expected Output: length == 1 | Output: length == {len(result)}")

@pytest.fixture
def alter_animals_table():
    cursor = conn.cursor()
    sample_data = [
        {"food_id": 1, "animal_id": 2},
        {"food_id": 2, "animal_id": 4},
    ]
    cursor.execute(queries.ADD_COLUMN_TO_ANIMALS_TABLE)
    cursor.executemany(queries.UPDATE_FOOD_ID, sample_data)
    yield conn, cursor   
def test_alter_animals_table(alter_animals_table):
    logging.info('Starting the create_enclosures test')
    conn, cursor = alter_animals_table
    with conn:
        cursor.execute(queries.SELECT_ANIMALS)
        result = cursor.fetchmany()
        print(f"Expected Output: length == 1 | Output: length == {len(result)}")
        assert len(result) > 0
        logging.info(f"Expected Output: length == 1 | Output: length == {len(result)}")

def test_display_animals():
    logging.info('Starting the display_animals test')
    data = []
    cursor = conn.cursor()
    cursor.execute(queries.DISPLAY_ANIMALS)
    result = cursor.fetchall()
    for x in result:
        data.append({"enclosure_id": x[0], "group_name": x[1], "id": x[2], "name": x[3], "quantity": x[4]})
    assert len(data) > 0
    assert type(data) == list
    print(f"Expected Output: length > 0 | Output: {len(result)}")
    logging.info(f"Expected Output: length > 0 | Output: {len(result)}")
    print(f"Expected Output: type == list | type == {type(result)}")
    logging.info(f"Expected Output: type == list | type == {type(result)}")
    