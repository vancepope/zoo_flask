from flask import Flask, render_template, request
from dotenv import load_dotenv
from db import queries
import os
import psycopg2
from datetime import datetime, timezone

load_dotenv()

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(db_url)

@app.post("/api/enclosure")
def create_enclosure():
    data = request.get_json()
    name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ENCLOSURES_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, (name,))

    return {"name": f"Enclosure {name} created."}, 201

@app.post("/api/animal")
def create_animal():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    enclosure_id = data["enclosure_id"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.CREATE_ANIMALS_TABLE)
            cursor.execute(queries.INSERT_ENCLOSURE, (name, quantity, enclosure_id))

    return {"name": f"Enclosure {name} created."}, 201