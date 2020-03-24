
The C3G montreal node Selection Test
=============

### Selection test for Ingesting the Canadian Common CV

### Features
Ingesting XML files into SqLite database from script XML xmlToPostsDb.py
Retrieving from database  with respect to a search term with order by feature 


### sample APi doc for the route

                
----
/**
* @api {get} /?type=value&searchTerm=value   Retrieve Posts
* @apiName RetrievePosts
* @apiGroup BioPostsService
* @apiParam {String} type          (viewCount,Score)if u need to order the posts by the value specified.
* @apiParam {String} searchTerm     if u need to retrieve posts searched with title and body with this term
* @apiSuccess {Array}  posts        An array  of objects that contains data of the posts
*     HTTP/1.1 200 OK
*      [
*    {"AcceptedAnswerId": null, "AnswerCount": null, "Body": "", "ClosedDate": null, "CommentCount": 0,
*     "CreationDate": "2020-01-13T21:05:48.940", "FavoriteCount": null, "Id": 11134,
*      "LastActivityDate": "2020-01-13T21:05:48.940", "LastEditDate": "2020-01-13T21:05:48.940", "LastEditorUserId": -1,
*     "OwnerDisplayName": null, "OwnerUserId": -1, "ParentId": null, "PostTypeId": 5, "Score": 0, "Tags": null,
*     "Title": null, "ViewCount": null},
*
*      {"AcceptedAnswerId": null, "AnswerCount": null,
*        "Body": "pybedtools wraps and extends BEDTools and offers feature-level manipulations from within Python. ",
*       "ClosedDate": null, "CommentCount": 0,
*       "CreationDate": "2020-01-13T21:05:48.940", "FavoriteCount": null, "Id": 11135,
*       "LastActivityDate": "2020-01-22T14:40:32.600",
*       "LastEditDate": "2020-01-22T14:40:32.600", "LastEditorUserId": 964,
*       "OwnerDisplayName": null, "OwnerUserId": 964, "ParentId": null,
*       "PostTypeId": 4, "Score": 0, "Tags": null, "Title": null, "ViewCount": null}
*        ]
* @apiError internalServerFindingError  internal error caused by unexplained behavior
* @apiErrorExample Error-Response:
*     HTTP/1.1 403 Forbidden
*     {
*       "error": "internalServerFindingError"
*     }
*/


### Running Procedures

Run the flask server
`$ python app.py -flask `

Dependecencies used withing the flask app if there is any not within the module
Install the dependency if needed
`$ pip install {depencyName} `
ApiDoc==1.4.0
cffi==1.14.0
click==7.1.1                                                                                  
cryptography==2.8
Flask==1.1.1
flask-core==2.9.0
Flask-Cors==3.0.8
itsdangerous==1.1.0
Jinja2==2.11.1
jsonschema==2.4.0
MarkupSafe==1.1.1
npm==0.1.1
optional-django==0.1.0
psycopg2==2.8.4
psycopg2-binary==2.8.4
pycparser==2.20
six==1.14.0
Werkzeug==1.0.0



#Route to the ReactApp dir and install dependency
#`$ npm install `

#Start the Web Application 
#`$ npm  start `
