#------------------------------------------------------------------------------
# clob_string.py (Section 7.2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright 2017, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle

con = cx_Oracle.connect("pythonhol", "welcome", "localhost/orclpdb")
cur = con.cursor()

print("Inserting data...")
cur.execute("truncate table testclobs")
longString = ""
for i in range(5):
    char = chr(ord('A') + i)
    longString += char * 250
    cur.execute("insert into testclobs values (:1, :2)",
                (i + 1, "String data " + longString + ' End of string'))
con.commit()

def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    if defaultType == cx_Oracle.CLOB:
        return cursor.var(cx_Oracle.LONG_STRING, arraysize = cursor.arraysize)

con.outputtypehandler = OutputTypeHandler

print("Querying data...")
cur.prepare("select * from testclobs where id = :id")
cur.execute(None, {'id': 1})
(id, clobdata) = cur.fetchone()
print("CLOB length:", len(clobdata))
print("CLOB data:", clobdata)
