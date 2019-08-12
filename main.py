from flask import render_template, request
from src import MarioAndPrincess
import time
from form import GridInputForm
from models import MarioMoves
from app import app
from db_setup import init_db, db_session
from db_creator import create_table
import ast
import datetime

create_table()
init_db()

@app.route('/', methods=['GET', 'POST'])
def base():
    return input()


@app.route('/input', methods=['GET', 'POST'])
def input():
    grid = GridInputForm(request.form)
    if request.method == 'POST':
        return result(raw_grid=grid.grid.data, N=int(grid.n.data))

    return render_template('input.html', form=grid)


@app.route('/result', methods=['GET', 'POST'])
def result(raw_grid, N):
    list_grid = ast.literal_eval(raw_grid)

    t0 = time.time()
    paths, error_flag = MarioAndPrincess().get_paths(N, list_grid)
    move_list = [' '.join(path) for path in paths]
    move_str  = ','.join(move_list)
    t1 = time.time() - t0

    if error_flag is False:
        save_entry(move_str, t1)

    return render_template('result.html',grid=list_grid, paths=move_list, flag=error_flag)


def save_entry(move_str, time):
    m_moves = MarioMoves()
    m_moves.id = datetime.datetime.now()
    m_moves.moves = move_str
    m_moves.time = time

    db_session.add(m_moves)
    db_session.commit()


if __name__ == '__main__':
    app.run(debug=True)