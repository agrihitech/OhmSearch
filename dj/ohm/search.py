import sqlite3
import math

kind = [ "","単独","直列","並列"]
conn = sqlite3.connect('regdb.sqlite3')
x = conn.cursor()
y = conn.cursor()

while True:
    R = int(input("Enter R:"))
    y.execute("drop table sort");
    com = 'create table sort(rid integer, error1 real, error2 real)'
    y.execute(com)
    com = "select * from registors"
    x.execute(com)
    while True:
        raw = x.fetchone()
        if raw == None:
            break
        error1 = raw[3] - R
        error2 = abs(error1)
        com = "insert into sort values("+str(raw[0])+","+str(error1)+","+str(error2)+")"
        y.execute(com)
    conn.commit()
    com = "select * from sort order by error2 asc limit 10"
    y.execute(com)
    anser = y.fetchall()
    for ans in anser:
        com = "select * from registors where id="+str(ans[0])
        x.execute(com)
        reg = x.fetchone()
        print("%s: %g, %g 仕上: %g 誤差: %g%%" % (kind[reg[4]],reg[1],reg[2],ans[1],ans[2]*100/R))
