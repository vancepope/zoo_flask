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
        logging.FileHandler(r'app.log')
    ]
)

@app.get("/")
def hello_monty():
    return ""

@app.post("/api/enclosure")
def create_enclosures():
    logging.info("Starting in create_enclosures method")
    data = request.get_json()
    group_name = data["group_name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, {"group_name": group_name})
    return {"message": f"{group_name} has been created."}, 201
        
@app.post("/api/animal")
def create_animals():
    logging.info("Starting in create_animals method")
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ANIMALS_TABLE)
            cursor.execute(queries.INSERT_ANIMAL, {"name": name, "quantity": quantity, "enclosure_id": enclosure_id})
    return {"message": f"{name} has been created."}, 201



@app.get("/api/animal/<int:id>")
def get_animal(id):
    logging.info("Starting in get_animals method")
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ANIMAL_BY_ID, (id, ))
            result = cursor.fetchone()
            print(result, flush=True)
            return {"id": result[0], "name": result[1], "quantity": result[2], "enclosure_id": result[3]}, 200
        
@app.get("/api/enclosure/<int:enclosure_id>")
def get_enclosure(enclosure_id):
    logging.info("Starting in get_enclosure method")
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ENCLOSURE_BY_ID, (enclosure_id, ))
            result = cursor.fetchone()
            print(result, flush=True)
            return {"id": result[0], "group_name": result[1]}, 200
        
@app.get("/api/animals")
def get_animals():
    logging.info("Starting in get_animals method")
    data = []
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.SELECT_ANIMALS)
            result = cursor.fetchall()
            for row in result:
                data.append({"id": row[0], "name": row[1], "quantity": row[2], "enclosure_id": row[3]})
            return data, 200
       
@app.get("/api/enclosures")
def get_enclosures():
    logging.info("Starting in get_enclosures method")
    data = []
    with connection:
        with connection.cursor() as cursor:
           cursor.execute(queries.SELECT_ENCLOSURES)
           result = cursor.fetchall()
           for x in result:
               data.append({"id": x[0], "group_name": x[1]})
           return data, 200
        
@app.post("/api/add_enclosure")
def add_enclosure():
    logging.info("Starting in add_enclosure method")
    data = request.get_json()
    group_name = data["group_name"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ENCLOSURE, {"group_name": group_name})
    return {"message": f"{group_name} has been created."}, 201
        
@app.post("/api/add_animal")
def add_animal():
    logging.info("Starting in add_animal method")
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    with connection:
       with connection.cursor() as cursor:
            cursor.execute(queries.INSERT_ANIMAL, {"name": name, "quantity": quantity, "enclosure_id": enclosure_id})
    return {"message": f"{name} has been created."}, 201


@app.get("/api/display_animals")
def display_animals():
    logging.info("Starting in display_animals method")
    data = []
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.DISPLAY_ANIMALS)
            result = cursor.fetchall()
            for x in result:
                data.append({"enclosure_id": x[0], "group_name": x[1], "animal_id": x[2], "name": x[3], "quantity": x[4]})
            return data, 200
