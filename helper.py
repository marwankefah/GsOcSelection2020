# from flask import jsonify,request
# import sqlite3
# import sqLite_creation
#
#

def dict_factory(cursor, row):
    if (cursor == None):
        return None
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# class post:
#
#     def listing(self):
#         with sqlite3.connect("database.db") as con:
#             listingType = request.args.get('type')
#             order = request.args.get('order')
#             if (listingType != None and (listingType == 'viewCount'
#                                          or listingType == 'score')):
#                 if (order != None and (order.casefold() == 'asc' or order.casefold() == 'desc')):
#                     return jsonify(sqLite_creation.listing(liteConn, c, listingType, order)), 200
#                 else:
#                     return jsonify(sqLite_creation.listing(liteConn, c, listingType)), 200
#             else:
#                 return jsonify(success=False), 4
#
#         return jsonify(success=False), 500
#
#
#
#
#     def __init__(self, id, PostTypeId, ParentId, CreationDate, Score, Body, ViewCount,
#                  AcceptedAnswerId, OwnerUserId, LastActivityDate,CommentCount,LastEditorUserId
#                  ,LastEditDate,Title,Tags,FavoriteCount,AnswerCount,ClosedDate):
#         self.AnswerCount = AnswerCount
#         self.FavoriteCount = FavoriteCount
#         self.LastEditDate = LastEditDate
#         self.LastEditorUserId = LastEditorUserId
#         self.Title = Title
#         self.Tags = Tags
#         self.id = id
#         self.CommentCount = CommentCount
#         self.AcceptedAnswerId = AcceptedAnswerId
#         self.ParentId = ParentId
#         self.Body = Body
#         self.ViewCount = ViewCount
#         self.Score = Score
#         self.CreationDate = CreationDate
#         self.PostTypeId = PostTypeId
#         self.OwnerUserId = OwnerUserId
#         self.LastActivityDate = LastActivityDate
#
#
#     def listing(self,type,c,liteConn,by='ASC'):
#         if(c==None):
#             return
#         if(type=='viewCount' or type=='score'):
#             query='SELECT * FROM posts WHERE PostTypeId=1 ORDER BY'+type+' '+by+ ';'
#             with liteConn:
#                 c.execute(query)
#                 return c.fetchAll()
#
#
#
#
#
