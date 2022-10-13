from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from solver import *


app=Flask(__name__)


@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/solution', methods=['POST','GET'])
def solution():
    data = request.form
    grid = generate(data)

    s=Sudoku(grid)
    a=s.validate()
    s.solve()
    
    if a:
        return render_template('solution.html',solved_puzzle=s.grid)
    else:
        return redirect(url_for('index'))
    


def generate(puzzle):
    
    grid=np.zeros((9,9))
    x=0

    for val in puzzle.values():
        if val == '':
            grid[x//9][x%9]=0
        elif int(val) in range(1, 10):
            grid[x//9][x%9]=val
        x+=1
    
    return grid

if __name__ == '__main__':
    app.secret_key='jkhjgdasjhdgs'
    app.run(debug=True,port=2200)


