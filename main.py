from flask import Flask, render_template, request, redirect, flash
from src import MarioAndPrincess
import sqlite3
from sqlite3 import Error
import time
from form import GridInputForm, ReplayForm
from models import Moves

from app import app



from db_setup import init_db, db_session
init_db()

@app.route('/input', methods=['GET', 'POST'])
def input():
    grid = GridInputForm(request.form)
    if request.method == 'POST':
        return result(raw_grid=grid.grid.data, N=int(grid.n.data))

    return render_template('input.html', form=grid)

@app.route('/display')
def display_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Moves)

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)

@app.route('/result', methods=['GET', 'POST'])
def result(raw_grid, N):
    print(raw_grid)
    replay = ReplayForm(request.form)
    if request.method == 'GET':
        print('it is get')
    if request.method == 'POST':
        print('it is post')
        #return input()

    t0 = time.time()
    n = int(len(raw_grid)/N)
    list_grid = []
    for i in range(n):
        list_grid.append(raw_grid[N*i: N*(i+1)])

    paths, error_flag = MarioAndPrincess().get_paths(N, list_grid)

    move_list = [' '.join(path) for path in paths]
    move_str  = ','.join(move_list)
    print(move_list)
    print(move_str)
    t1 = time.time() - t0
    print('time elapsed:', t1)
    return render_template('result.html',form=replay, grid=list_grid, paths=move_list, flag=error_flag)  # we can use variable posts inside outs home.html

if __name__ == '__main__':
    app.run(debug=True)