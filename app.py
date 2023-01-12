import os
import psycopg2
import logging
from db import queries
from dotenv import load_dotenv
from datetime import datetime, timezone
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(db_url)


logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    handlers=[
        logging.FileHandler(r'test_app.log')
    ]
)

@app.post("/api/animal")
def create_animal():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ANIMALS_TABLE)
            cursor.execute(queries.INSERT_ANIMAL, (name, quantity, enclosure_id))

    return {"name": f"Enclosure {name} created."}, 201

@app.post("/api/enclosure")
def create_enclosure():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, (name,))
            result = cursor.fetchone()[0]
            return {"name": f"Enclosure {name} created.", "message": "{result}"}, 201


@app.get("/api/animal/<int:animal_id>")
def get_animal(animal_id):
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ANIMAL_BY_ID, (animal_id, ))
            result = cursor.fetchone()[0]
            print(result, flush=True)
            return result, 200
        
@app.get("/api/enclosure/<int:enclosure_id>")
def get_enclosure(enclosure_id):
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    id = data["enclosure_id"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ENCLOSURE_BY_ID, (enclosure_id, ))
            result = cursor.fetchone()[0]
            print(result, flush=True)
            return result, 200
        
@app.get("/api/animals")
def get_animals():
    with connection:
        with connection.cursor() as cursor:
           cursor.execute(queries.SELECT_ENCLOSURE_BY_ID)
           result = cursor.fetchall()
           return list(result), 200