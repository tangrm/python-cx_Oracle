#------------------------------------------------------------------------------
# bind_insert.py (Section 4.2 and 4.3)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright 2017, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle

con = cx_Oracle.connect("pythonhol", "welcome", "localhost/orclpdb")
cur = con.cursor()

rows = [ (1, "First" ), (2, "Second" ),
         (3, "Third" ), (4, "Fourth" ),
         (5, "Fifth" ), (6, "Sixth" ),
         (7, "Seventh" ) ]

cur.executemany("insert into mytab(id, data) values (:1, :2)", rows)

# Now query the results back

cur2 = con.cursor()
cur2.execute('select * from mytab')
res = cur2.fetchall()
print(res)
