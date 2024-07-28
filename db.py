import sqlite3

connection = sqlite3.connect("mytodo.db")


cursor = connection.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT);
    '''
)

def insertItem(item):
    cursor.execute(
        f'''
            INSERT INTO todo (title) values ("{item}");
        '''
    )
    connection.commit()


def retrieveItems():
    result = cursor.execute("SELECT * FROM todo").fetchall()
    print(result)
    return result

def editItem(itemid, data):
    cursor.execute(
        f'''
            UPDATE todo SET (title) = "{data}" WHERE id = {itemid}
        '''
    )
    connection.commit()