import sqlite3
from flask import Flask, request, jsonify
import xmlToPostsDb
import helper
from models.posts  import post as p
from flask_cors import  CORS
app = Flask(__name__)
#app.secret_key = "THIS_IS_A_TEST"

CORS(app)
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


#/**
#* @api {get} /?type=value&searchTerm=value   Retrieve Posts
# * @apiName RetrievePosts
# * @apiGroup BIOPOSTService
# * @apiParam {String} type          (viewCount,Score)if u need to order the posts by the value specified.
# * @apiParam {String} searchTerm     if u need to retrieve posts searched with title and body with this term
# * @apiSuccess {Array}  posts        An array  of objects that contains data of the posts
# *     HTTP/1.1 200 OK
# *      [
# *    {"AcceptedAnswerId": null, "AnswerCount": null, "Body": "", "ClosedDate": null, "CommentCount": 0,
# *     "CreationDate": "2020-01-13T21:05:48.940", "FavoriteCount": null, "Id": 11134,
# *      "LastActivityDate": "2020-01-13T21:05:48.940", "LastEditDate": "2020-01-13T21:05:48.940", "LastEditorUserId": -1,
# *     "OwnerDisplayName": null, "OwnerUserId": -1, "ParentId": null, "PostTypeId": 5, "Score": 0, "Tags": null,
# *     "Title": null, "ViewCount": null},
# *
# *      {"AcceptedAnswerId": null, "AnswerCount": null,
# *        "Body": "pybedtools wraps and extends BEDTools and offers feature-level manipulations from within Python. ",
# *       "ClosedDate": null, "CommentCount": 0,
# *       "CreationDate": "2020-01-13T21:05:48.940", "FavoriteCount": null, "Id": 11135,
# *       "LastActivityDate": "2020-01-22T14:40:32.600",
# *       "LastEditDate": "2020-01-22T14:40:32.600", "LastEditorUserId": 964,
# *       "OwnerDisplayName": null, "OwnerUserId": 964, "ParentId": null,
# *       "PostTypeId": 4, "Score": 0, "Tags": null, "Title": null, "ViewCount": null}
# *        ]
# * @apiError internalServerFindingError  internal error caused by unexplained behavior
# * @apiErrorExample Error-Response:
# *     HTTP/1.1 403 Forbidden
# *     {
# *       "error": "internalServerFindingError"
# *     }
# */
from postsListings.listing import fun as listingModule
app.register_blueprint(listingModule)


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
