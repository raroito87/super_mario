Explanation of the project:

Mario and the princess are trapped in a square grid (N*N), Mario needs to reach the princess
with minimum number of steps (shortest paths), while avoiding any obstacles. Mario can
move UP, DOWN, LEFT and RIGHT and can’t go outside of the grid. Create a function or a
class that given a square grid (N*N), the location of Mario and the princess will return a list
of the shortest paths possible from Mario to the princess.
Mario denoted by (m)
Princess denoted by (p)
Obstacle denoted by (x)
Free cell denoted by (-)
Input format:
you have two inputs [N] which is the grid size and [Grid] which is the actual map itself. [N] is
a scalar integer, while [Grid] should be a list of string where each entry is a row of the map
itself.
Example:
N = 3
Grid = [‘--m’,’-x-’,’-p-’]

Output format:
Your output should be [error_flag] and [paths]. The [error_flag] is a binary output where it is
TRUE in case, we have an error and FALSE otherwise, the [paths] is a list of all the possible
moves (RIGHT-LEFT-UP-DOWN) that can be followed to get to the princess.

An Api has been created with Flask to use the code with a graphic interface