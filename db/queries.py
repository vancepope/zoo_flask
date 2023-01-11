CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_ANIMALS_TABLE = (
    "CREATE TABLE IF NOT EXISTS animals (id SERIAL, name REAL, quantity INTEGER, enclosure_id FOREIGN KEY(enclosure_id) REFERENCES enclosures(id) ON DELETE CASCADE);"
)
INSERT_ENCLOSURE = (
    "INSERT INTO enclosures (name) VALUES(%s) RETURNING name"
)
INSERT_ANIMAL = (
    "INSERT INTO animals (name, quantity, enclosure_id) VALUES (%s, %s, %s) RETURNING name, quantity, enclosure_id"
)
DISPLAY_ANIMALS = {
    "SELECT enclosures.id, animals.id FROM enclosures LEFT JOIN animals ON enclosures.id = animals.enclosure_id ORDER BY enclosure.id;"
}