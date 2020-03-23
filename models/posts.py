import sqlite3
class post():
    # posts Schema
    tableName='posts'
    postDbName='postsDb'
    postsTable = ("\n"
                  "        CREATE TABLE IF NOT EXISTS posts (\n"
                  "            Id                  integer PRIMARY KEY ,\n"
                  "            PostTypeId          integer NOT NULL,\n"
                  "            ParentId            integer ,\n"
                  "            CreationDate        text NOT NULL,\n"
                  "            Score               integer NOT NULL ,\n"
                  "            Body                BLOB NOT NULL ,\n"
                  "            ViewCount           integer,\n"
                  "            AcceptedAnswerId    integer,\n"
                  "            OwnerUserId         integer NOT NULL ,\n"
                  "            LastActivityDate    text NOT NULL ,\n"
                  "            CommentCount        integer NOT NULL ,\n"
                  "            LastEditorUserId    integer,\n"
                  "            LastEditDate        text,\n"
                  "            Title               text,\n"
                  "            Tags                text,\n"
                  "            FavoriteCount       integer,\n"
                  "            AnswerCount         integer,\n"
                  "            ClosedDate          text,\n"
                  "            OwnerDisplayName    text,\n"
                  "            CONSTRAINT postsId FOREIGN KEY (ParentId,AcceptedAnswerId) REFERENCES posts(id,id),\n"
                  "            CONSTRAINT userId FOREIGN KEY (OwnerUserId,LastEditorUserId) REFERENCES  users(id,id)\n"
                  "            );                \n"
                  "                ")
    dbTables=[postsTable]

    def create_schemas(self,c):
        for idx,table in enumerate(self.dbTables):
            try:
                c.execute(table)
            except sqlite3.Error as error:
                print("Database Creation Error in index "+idx+" in Table" + table)
                print(error)

    def drop_and_create(self,c):
        if(c==None):
            return None
        # turned off  except stated from mentor
        # c.execute("""PRAGMA foreign_keys = ON;""")
        self.drop_table(self,c)
        self.create_schemas(self,c)


    def filter_by_type(self, c, listingType='id', order='DESC', searchTerm=-1):
        if(c==None):
            return None

         #no string injection in the query predfined strings
        query=' ASC;' if(order.casefold()=='asc') else ' DESC;'
        if(listingType=='id'):
            if(searchTerm!=-1):
                query='SELECT * FROM posts WHERE title like ? or body like ?'
                # anySQLite injection would be quoted and will never execute
                temp='%'+searchTerm+'%'
                # as searchTerm is provided to the execute as a parameter
                return c.execute(query,(temp,temp)).fetchall()
            else:
                # NO passing argument parameter is concatenating
                query='SELECT * FROM POSTS where creationDate is not NULL ORDER by creationDate'+query
                return c.execute(query).fetchall()

        elif(listingType=='viewCount'):
            if(searchTerm!=-1):
                # anySQLite injection would be quoted and will never execute
                query='SELECT * FROM posts WHERE viewCount IS NOT NULL AND (title like ? or body like ?) ORDER BY viewCount'+query
                # anySQLite injection would be quoted and will never execute
                temp='%'+searchTerm+'%'
                # as searchTerm is provided to the execute as a parameter
                return c.execute(query,(temp,temp)).fetchall()
            else:
                # NO passing argument parameter is concatenating
                query='SELECT * FROM POSTS  WHERE viewCount IS NOT NULL ORDER BY viewCount'+query
                return c.execute(query).fetchall()
        elif(listingType=='score'):
            if(searchTerm!=-1):
                query='SELECT * FROM posts WHERE Score IS NOT NULL and (title like ? or body like ?) ORDER BY Score'+query
                # anySQLite injection would be quoted and will never execute
                temp='%'+searchTerm+'%'
                # as searchTerm is provided to the execute as a parameter
                return c.execute(query,(temp,temp)).fetchall()
            else:
                # NO passing argument parameter is concatenating
                query='SELECT * FROM POSTS  WHERE Score IS NOT NULL ORDER BY score'+query
                return c.execute(query).fetchall()

        else:
            return []


    def drop_table(self,c):
        c.execute(""" DROP TABLE IF EXISTS posts;""")
        c.execute(""" DROP TABLE IF EXISTS users;""")


# #needed for authentication of the ownerUserId & lastUserId in the postSchema
# userTable= ("        \n"
#             "        CREATE TABLE IF NOT EXISTS users(\n"
#             "            id                  integer PRIMARY KEY ,\n"
#             "            username            text NOT NULL unique  \n"
#             "            );")




