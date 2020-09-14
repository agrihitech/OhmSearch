import sqlite3
e24 = [ 1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,
3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1]

m10 = [1e-1,1,1e1,1e2,1e3,1e4,1e5,1e6,1e7]

conn = sqlite3.connect('regdb.sqlite3')
c = conn.cursor()
com = "drop table registors"
c.execute(com)
com = ''' create table registors(id INTEGER PRIMARY KEY AUTOINCREMENT,
val1 real, val2 real, val3 real, type integer)
'''
id = 0
c.execute(com)
for m in m10:
    for r1 in e24:
        r1 *= m
        id += 1
        com = "insert into registors values("+str(id)+","+str(r1)+",0,"+str(r1)+",1)"
        c.execute(com)
        for n in m10:
            for r2 in e24:
                r2 *= n
                if r2 > r1:
                    break
                id += 1
                com = "insert into registors values("+str(id)+","+str(r1)+","+str(r2)+","+str(r1+r2)+",2)"
                c.execute(com)
                id += 1
                com = "insert into registors values("+str(id)+","+str(r1)+","+str(r2)+","+str(1.0/(1.0/r1+1.0/r2))+",3)"
                c.execute(com)
conn.commit()
conn.close()
