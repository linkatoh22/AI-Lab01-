Imagine you are participating in a game where a character is attempting to navigate through 
a maze and requires your assistance in order to escape. As illustration, in the maze 
mentioned above, the entrance is located in cell 40 and the exit is located in cell 59. In 
order to make this task less challenging, we will presume that this maze contains only a 
single entrance and exit. Additionally, it is essential to always confirm that there is a viable 
escape route from the maze. You can only move horizontally and vertically.
VNUHCM-UNIVERSITY OF SCIENCE
FACULTY OF INFORMATION TECHNOLOGY
LAB 01 | CSC14003 – Artificial Intelligence Page 2
Problem representation
Input: The maze is represented as a text file as follows.
- The first line must contain a positive integer 𝑁, representing the size of the maze.
- The second line contains 2 integers representing the entrance and exit.
- 𝑁 × 𝑁 next line contains an adjacency list or adjacency matrix.
Output: The program must print the following information to the console:
- The time to escape the maze.
- The list of nodes explored in the correct order.
- The list of nodes on the path found in the correct order.
Search strategies implementation
You are required to implement and provide results for the following search strategies:
- Breadth-first search (BFS) & Depth-first search (DFS)
- Uniform-cost search (UCS)
- Greedy Best First Search using the Manhattan distance as heuristic
- Graph-search A* using the same heuristic as above
