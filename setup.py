"""
Setup script for database path.
"""

instruction_text = """
Enter the path and database name of the database you want to use.
Example: /home/user/database.db
"""

def get_path():
    # get path to db
    print(instruction_text)
    path = input("Path: ")
    return path

# verify db exists
exists = False
path = get_path()
while not exists:
    try:
        open(path)
        exists = True
    except FileNotFoundError:
        print("File not found. Try again.")
        path = input("Path: ")

# write path
with open('db_path.txt', 'w') as f:
    f.write(path)
    f.close()
