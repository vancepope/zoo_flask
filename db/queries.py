CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, group_name TEXT);"
)
CREATE_ANIMALS_TABLE = (
    """ CREATE TABLE IF NOT EXISTS animals 
        (id SERIAL PRIMARY KEY, name TEXT, quantity INTEGER, enclosure_id INTEGER,
        CONSTRAINT enclosure_id FOREIGN KEY(enclosure_id) 
        REFERENCES enclosures(id) ON DELETE CASCADE);
    """
)

CREATE_ANIMAL_FOODS_TABLE = (
    """ CREATE TABLE IF NOT EXISTS animal_foods 
        (id SERIAL PRIMARY KEY, food TEXT, food_type TEXT);
    """
)
ADD_COLUMN_TO_ANIMALS_TABLE = (
    """ ALTER TABLE animals DROP CONSTRAINT IF EXISTS food_id;
        ALTER TABLE animals
        ADD CONSTRAINT food_id FOREIGN KEY(food_id) 
        REFERENCES animal_foods(id);
    """
)
UPDATE_FOOD_ID = (
    """ UPDATE animals SET food_id = %(food_id)s WHERE id = %(animal_id)s
    """
)
INSERT_ANIMAL = (
    """ INSERT INTO   animals(name, quantity, enclosure_id) 
        SELECT  %(name)s, %(quantity)s, %(enclosure_id)s
        WHERE   %(name)s  NOT IN
            (
                SELECT  name
                FROM    animals
            )
    """
)
INSERT_ENCLOSURE = (
    """ INSERT INTO   enclosures(group_name)
        SELECT  %(group_name)s
        WHERE   %(group_name)s  NOT IN
            (
                SELECT  group_name
                FROM    enclosures
            )
    """
)
INSERT_ANIMAL_FOOD = (
        """ INSERT INTO   animal_foods(food, food_type) 
        SELECT  %(food)s, %(food_type)s
        WHERE   %(food)s  NOT IN
            (
                SELECT  food
                FROM    animal_foods
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
SELECT_ANIMAL_FOODS = (
    "SELECT * FROM animal_foods"
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