import sqlite3
from flask import Flask, request, jsonify
import xmlToPostsDb
import helper
from models.posts  import post as p

app = Flask(__name__)
#app.secret_key = "THIS_IS_A_TEST"

# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True

# littleConn = None
# Creating the connection with the dbFile specified
try:
    liteConn = sqlite3.connect(p.postDbName)
    liteConn.row_factory = helper.dict_factory
    c = liteConn.cursor()
    # dropping and creating the schema to test the ingestion of the xml to the db
    # use p.create_schemas()
    p.create_schemas(p,c=c)
    liteConn.commit()
except sqlite3.OperationalError as e:
    print(e)
    c = None
    liteConn = None
    pass




from postsListings.listing import fun as listingModule
app.register_blueprint(listingModule)

@app.route('/')
def read_me():

    return 'Hello World!'


# Connects to the database specified in dbFile
# cli command to connect the db
@app.cli.command('initdb')
def initdb_command():
    liteConn = sqlite3.connect(p.postDbName)
    p.drop_and_create(p,c)
    liteConn.commit()
    print('Database initialized')


@app.teardown_appcontext
def close_database(error):
    if hasattr(liteConn, p.postDbName):
        liteConn.close()

if __name__ == '__main__':
    app.run(debug=True)
