import sqlite3
from werkzeug.exceptions import InternalServerError

from flask import Blueprint, request, jsonify,session,g
import _sqlite3
from models.posts import post as p
import  helper
fun = Blueprint('listing', __name__, url_prefix='/')

# we need here authentication in future
@fun.before_request
def before_request():
    g.threadConn = sqlite3.connect(p.postDbName)
    g.threadConn.row_factory = helper.dict_factory
    g.threadC = g.threadConn.cursor()
    return


@fun.route('/listing', methods=['GET'])
def listing():
    if(g.threadC==None):
        return jsonify(success=False), 500
    listingType = request.args.get('type')
    order = request.args.get('order')
    searchTerm=request.args.get('searchTerm')
    kwargs = dict(self=p,c=g.threadC,listingType=listingType, order=order,searchTerm=searchTerm)
    listingJson=jsonify(p.filter_by_type(**{k: v for k, v in kwargs.items() if v is not None}))
    if(listingJson!=None):
        return listingJson, 200
    else:
        raise InternalServerError


@fun.errorhandler(InternalServerError)
def handle(error):
    response = jsonify(error.description)
    response.status_code = error.code
    return response

