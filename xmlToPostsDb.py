import sqlite3
import xml.etree.ElementTree as ET
from models.posts  import post as p
import helper
#bioinformaticS_posts_se.xml

xmlFilePaths=['bioinformatics_posts_se.xml']

# ingesting the xmlFIlePath as per defined
def xml_to_database(c,filepath):
    if(c==None):
        return None
    try:
        postsXmlTree = ET.parse(filepath)
    except FileNotFoundError as e:
        print("FILE NOT FOUND")
        return
    postsXmlRoot=postsXmlTree.getroot()
    for child in postsXmlRoot:
        columnNames = ','.join(child.attrib.keys())
        columnValues = ',:'.join(child.attrib.keys())
        # here we only parse into values :Id ,:parentId, not the actual values
        execText='INSERT INTO posts(%s) VALUES(:%s)' % (columnNames,columnValues)
        #actual values are sent here to preventSQL injection
        # if anyone tried to inject ; # any injection here ;
        #child.attrib wont find suitable mapping in the query and error will be thrown
        c.execute(execText,child.attrib)


liteConn = sqlite3.connect(p.postDbName)
liteConn.row_factory = helper.dict_factory
c = liteConn.cursor()
p.drop_and_create(p,c)

for idx,file in enumerate(xmlFilePaths):
    xml_to_database(c, file)

liteConn.commit()

liteConn.close()