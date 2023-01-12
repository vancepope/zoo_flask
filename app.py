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
def create_animals():
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
def create_enclosures():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, (name,))
            result = cursor.fetchone()[0]
            return {"name": f"Enclosure {name} created.", "message": "{result}"}, 201


@app.get("/api/animal/<int:id>")
def get_animal():
    data = request.get_json()
    animal_id = data["id"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ANIMAL_BY_ID, (animal_id, ))
            result = cursor.fetchone()[0]
            print(result, flush=True)
            return result, 200
        
@app.get("/api/enclosure/<int:id>")
def get_enclosure():
    data = request.get_json()
    enclosure_id = data["id"]
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
           cursor.execute(queries.SELECT_ANIMALS)
           result = cursor.fetchall()
           return list(result), 200
       
@app.get("/api/enclosures")
def get_animals():
    with connection:
        with connection.cursor() as cursor:
           cursor.execute(queries.SELECT_ENCLOSURES)
           result = cursor.fetchall()
           return list(result), 200
        
@app.post("api/add_enclosure")
def add_enclosure():
    data = request.get_json()
    name = data["name"]
    dupe = data["dupe"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ENCLOSURE, (name, dupe))
            result = cursor.fetchone()[0]
            print(result, flush=True)
            return result, 201
        
@app.post("api/add_animal")
def add_animal():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    dupe = data["dupe"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ANIMAL, (name, quantity, enclosure_id, dupe))
            result = cursor.fetchone()[0]
            print(result, flush=True)
            return result, 201


@app.get("/api/display_animals")
def display_animals():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.DISPLAY_ANIMALS)
            result = cursor.fetchall()
            return result, 200
