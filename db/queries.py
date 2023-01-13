CREATE_ANIMALS_TABLE = (
    """ CREATE TABLE IF NOT EXISTS animals 
        (id SERIAL PRIMARY KEY, name TEXT, quantity INTEGER, enclosure_id INTEGER,
        CONSTRAINT enclosure_id FOREIGN KEY(enclosure_id) 
        REFERENCES enclosures(id) ON DELETE CASCADE);
    """
)
CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, group_name TEXT);"
)
INSERT_ANIMAL = (
    """ INSERT INTO   animals(name, quantity, enclosure_id) 
        SELECT  %s, %s, %s
        WHERE   %s NOT IN
            (
                SELECT  name
                FROM    animals
            )
    """
)
INSERT_ENCLOSURE = (
    """ INSERT INTO   enclosures(group_name)
        SELECT  %s
        WHERE   %s  NOT IN
            (
                SELECT  group_name
                FROM    enclosures
            )
    """
)
SELECT_ANIMALS = (
    "SELECT * FROM animals;"
)
SELECT_ANIMAL_BY_ID = (
    "SELECT * FROM animals WHERE id = %s;"
)
SELECT_ENCLOSURES = (
    "SELECT * FROM enclosures;"
)
SELECT_ENCLOSURE_BY_ID = (
    "SELECT * FROM enclosures WHERE id = %s;"
)
DISPLAY_ANIMALS = (
    """ SELECT enclosures.id, enclosures.group_name, animals.id, animals.name, animals.quantity 
        FROM enclosures INNER JOIN animals ON enclosures.id = animals.enclosure_id 
        ORDER BY enclosures.id;
    """
)