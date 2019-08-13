# Coding Challenge

This repository contains my solution to a proposed coding challenge

# Task 1 (Mario saving the princess):

First task (Mario saving the princess):
Mario and the princess are trapped in a square grid (N*N), Mario needs to reach the princess
with minimum number of steps (shortest paths), while avoiding any obstacles. Mario can
move UP, DOWN, LEFT and RIGHT and can’t go outside of the grid. Create a function or a
class that given a square grid (N*N), the location of Mario and the princess will return a list
of the shortest paths possible from Mario to the princess.
Mario denoted by (m)
Princess denoted by (p)
Obstacle denoted by (x)
Free cell denoted by (-)
Your code should also validate that the given grid is a square matrix which contains one
Mario, one princess and empty cells or obstacles. Note that all letters are case sensitive. In
case one of the constrains are violated your code should identify it and raise an error flag and
empty return for the paths.
Input format:
you have two inputs [N] which is the grid size and [Grid] which is the actual map itself. [N] is
a scalar integer, while [Grid] should be a list of string where each entry is a row of the map
itself.
Example:
N = 3
Grid = [‘--m’,’-x-’,’-p-’]
- - m
- x - >>> 3*3 matrix, Mario exists at [0,2], princess at [2,1] and an obstacle at [1,1]
- p -

Output format:
Your output should be [error_flag] and [paths]. The [error_flag] is a binary output where it is
TRUE in case, we have an error and FALSE otherwise, the [paths] is a list of all the possible
moves (RIGHT-LEFT-UP-DOWN) that can be followed to get to the princess. So, the output
[paths] for the example mentioned above should be:
[(DOWN, DOWN, LEFT), (LEFT, DOWN, DOWN), (DOWN, LEFT, DOWN)]
However, since we have an obstacle in [1,1] the list should be:
[(DOWN, DOWN, LEFT)]
In case all the shortest paths are blocked your code is expected to return at least one possible
path (if exists).
As for [error_flag] it should equal FALSE because the grid is formatted correctly.

Task #2 (API and Database):

Create a REST API for using the class/function from task one. The endpoints are up to
you. However, your API should have inputs/outputs in the same style.
• Create a serverless database (SQLite) which has one table to save data coming from
the API.
• Your API should return the game result to the user and save the request time along
with input sent into the serverless database (SQLite).
Hints and notes:
1. For the API creation you can use flask or flask restful for a quick implementation.
2. Using an ORM such as sqlalchemy for the database part is a plus.
3. Adding another end point to view the log data from the database in the API is a
plus.


# Solution 1

I have created several classes to solve this task:
  - Grid: contains all the Cells and it is created
and initialized by GridHandler.
  - Cell: contains the information for each position including the type
of cell (mario, princess, blocked or free)
  - GridHandler is in charge of finding the paths. It marks
all the free Cells with a 'count' value. 'count' represents the distance in number of cells from Mario. The
Cells also saves its ‘parent’ cells to trace back the path once the princess has been found. It
uses a recurrent function to gather all the shortest paths in a list.
- MarioAndPrincess: is an interface class to run the algorithm within a call

I have created several tests to fulfill the requirements asked for this task. Test check the following:
  - correct format of the input for like correct shape of the grid or the presence of Mario and Princess in the grid
  - algoithm find all the shortest paths
  - if no path exists returns None
  - flag return Tru only if the input grid has an incorrect format
  
# Solution 2
 
I have followed this tutorial to solve this exercise:
http://www.blog.pythonlibrary.org/2017/12/12/flask-101-getting-started/

Packages used: 
Flask==1.0.2
Flask-SQLAlchemy==2.4.0
Flask-WTF==0.14.2

The input and the returning paths are saved in the database.
The API works as follows:
Base page http://127.0.0.1:5000 redirects to http://127.0.0.1:5000/input. In /input you insert the parameters 'N' and 'raw_grid' in the form of ‘['x-m', '---', '-p-']’ and then press ‘Rescue’. This redirects you to the /results page where the grid and the output are shown. If there format of the inserted parameters is wrong the error flag will display true and not paths will be listed. In case everything went of all the founds paths will be listed. The process can be restarted by pressing the button ‘Return’

To try the API run main.py.





