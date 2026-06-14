import sqlite3

def connect_db(db = "database/candidates.db"):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    return connection,cursor

def create_table():
    conn,cursor = connect_db()

    cursor.execute('''
        create table if not exists candidates(
            candidate_id integer primary key,
            candidate_name string,
            candidate_email string,
            candidate_point integer
            );
        ''')
    conn.commit()
    conn.close()

def get_all_candidates():
    conn,cursor = connect_db()
    cursor.execute("select * from candidates;")
    
    candidates = cursor.fetchall()

    conn.close()
    return candidates

def add_candidate(candidate_id,candidate_name,candidate_email,candidate_point = 0):
    conn,cursor = connect_db()
    
    cursor.execute('''
        insert into candidates (candidate_id,candidate_name,candidate_email,candidate_point) values(?,?,?,?)
    ''',(candidate_id,candidate_name,candidate_email,candidate_point))
    
    conn.commit()
    conn.close()

def get_candidate_by_id(candidate_id):
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM candidates WHERE candidate_id = ?', (candidate_id))

    candidate = cursor.fetchone()
    
    conn.close()
    
    return candidate

def add_point(candidate_id,point):
    conn,cursor = connect_db()
    cursor.execute('update candidates set candidate_point = candidate_point + ? where candidate_id = ?',(point,candidate_id))

    conn.commit()
    conn.close()

def get_candidate_points(sort = -1):
    sort = "DESC" if sort == -1 else "ASC"

    conn,cursor = connect_db()
    cursor.execute(f'select candidate_name,candidate_point from candidates order by candidate_point {sort};')

    candidates = cursor.fetchall()
    conn.close()

    return candidates

def init_db():
    create_table()