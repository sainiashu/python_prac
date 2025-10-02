import psycopg2

def get_connect():
    con= psycopg2.connect(dbname='subqueries',user='root@localhost',password='admin')
    cur = con.cursor()
    cur.execute("Select Count(*) from database")
    count = cur.fetchone()[0]
    con.close()
    return count

if  __name__=='__main__':
    print("connection: ",get_connect())