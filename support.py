# queries
nameID = """
    SELECT name
    FROM names
    WHERE uid = {};
    """
nameValue = """
    SELECT uid
    FROM names
    WHERE name = '{}';
    """
queryID = """
    SELECT row_value AS value, source
    FROM {}
    WHERE uid = {};
    """
queryValue = """
    SELECT uid
    FROM {}
    WHERE row_value = '{}'; 
    """

def db_path():
    """
    Returns the path to the database file
    """
    with open('db_path.txt', 'r') as f:
        db_path = f.read()
    return db_path
