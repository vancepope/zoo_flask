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
    level=logging.WARNING,
    format= "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
    handlers=[
        logging.FileHandler(r'app.log')
    ]
)

@app.get("/")
def hello_monty():
    return ""

@app.post("/api/enclosure")
def create_enclosures():
    data = request.get_json()
    group_name = data["group_name"]
    dupe = data["dupe_name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, (group_name, dupe))
    return {"message": f"{group_name} has been created."}, 201
        
@app.post("/api/animal")
def create_animals():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    dupe = data["dupe_name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ANIMALS_TABLE)
            cursor.execute(queries.INSERT_ANIMAL, (name, quantity, enclosure_id, dupe))
    return {"message": f"{name} has been created."}, 201



@app.get("/api/animal/<int:id>")
def get_animal(id):
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ANIMAL_BY_ID, (id, ))
            result = cursor.fetchone()
            print(result, flush=True)
            return list(result), 200
        
@app.get("/api/enclosure/<int:enclosure_id>")
def get_enclosure(id):
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ENCLOSURE_BY_ID, (id, ))
            result = cursor.fetchone()
            print(result, flush=True)
            return list(result), 200
        
@app.get("/api/animals")
def get_animals():
    with connection:
        with connection.cursor() as cursor:
           cursor.execute(queries.SELECT_ANIMALS)
           result = cursor.fetchall()
           return list(result), 200
       
@app.get("/api/enclosures")
def get_enclosures():
    with connection:
        with connection.cursor() as cursor:
           cursor.execute(queries.SELECT_ENCLOSURES)
           result = cursor.fetchall()
           return list(result), 200
        
@app.post("/api/add_enclosure")
def add_enclosure():
    data = request.get_json()
    name = data["name"]
    dupe = data["dupe"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ENCLOSURE, (name, dupe))
    return {"message": f"{name} has been created."}, 201
        
@app.post("/api/add_animal")
def add_animal():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    dupe = data["dupe"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ANIMAL, (name, quantity, enclosure_id, dupe))
    return {"message": f"{name} has been created."}, 201


@app.get("/api/display_animals")
def display_animals():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.DISPLAY_ANIMALS)
            result = cursor.fetchall()
            return result, 200
