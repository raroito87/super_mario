from flask import Flask, render_template, request
from src import MarioAndPrincess
import sqlite3
from sqlite3 import Error
import time
from flask import g

DATABASE = '/path/to/database.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/result/<raw_grid>/<int:N>')
def result(raw_grid, N):
    t0 = time.time()
    n = int(len(raw_grid)/N)
    list_grid = []
    for i in range(n):
        list_grid.append(raw_grid[N*i: N*(i+1)])

    paths = MarioAndPrincess().get_paths(N, list_grid)
    #p = ', '.join(paths)
    #print(p)
    t1 = time.time() - t0
    print('time elapsed:', t1)
    return render_template('result.html', grid=list_grid, paths=paths)  # we can use variable posts inside outs home.html

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
        return None
    finally:
        conn.close()

def main(database):

    sql_create_projects_table = """CREATE TABLE IF NOT EXIST projects(
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date test
    );"""
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print('Error! cannot create a database connection')


def create_table(conn, create_table_sql):
    try:
        c=conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)