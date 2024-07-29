import sqlite3

# SQLite3 is a pre installed library with python
# you don't need to install it
# connects or creates database if it does not exist
# To view SQLite3 db in vs code you need to install the extension SQLite3 Editor from the id under :
# yy0931.vscode-sqlite3-editor
# type it in the search bar and it will show up
connection = sqlite3.connect("mytodo.db")


cursor = connection.cursor()
# creating table in database if it does not exist
# id is auto incremented so we don't need to add when inserting elements/rows
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT);
    '''
)
# inserting element by passing argument item which is a string 
def insertItem(item):
    cursor.execute(
        f'''
            INSERT INTO todo (title) values ("{item}");
        '''
    )
    # to save changes made to our table
    connection.commit()

# to getall items
# fetchall converts the result from object to a list containing our rows
def retrieveItems():
    result = cursor.execute("SELECT * FROM todo").fetchall()
    
    return result

# editing items by passing itemid which is an integer and data which is a string
def editItem(itemid, data):
    cursor.execute(
        f'''
            UPDATE todo SET (title) = "{data}" WHERE id = {itemid}
        '''
    )
    connection.commit()

# deleting items by passing itemid which is an integer
def deleteItem(itemid):
    cursor.execute(
        f'''
            DELETE FROM todo WHERE id = {itemid}
        '''
    )
    connection.commit()


    