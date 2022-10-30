import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# database credentials
host = '127.0.0.1'
db_name = 'sparkifydb'
user = 'student'
password = 'student'

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect(f"host={host} dbname=studentdb user={user} password={password}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name} WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect(f"host={host} dbname={db_name} user={user} password={password}")
    cur = conn.cursor()
    
    print('Database created')
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using table list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

    print("Tables dropped")

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

    print('Tables created')

def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()