from timeit import default_timer as timer
import queue
from collections import deque
from queue import PriorityQueue
def readfile(fileread):
    file=open(fileread,"r")
    size=file.readline()
    n=int(size)
    list1=[]

    key=file.readline()
    key=key.split()
    begin=key[0]
    end=key[1]
    for i in range(n*n):
        data=file.readline()
        content= data.split()
        list1.append(content)
    file.close()
    maze = {}
    for x in list1:
        maze[x[0]] = x[1:]
    return maze,begin,end,n

def DFS(maze,begin,end):
    start = timer()
    path=[]
    stack=[begin]
    visited=[]
    path1={}
    while len(stack)!=0:
        v=stack.pop()
        visited.append(v)
        if(v==end):
            path.append(v)
            while v!=begin:
                v=path1[v]
                path.append(v)
            path.reverse()
            end = timer()
            elapsed_time = end - start
            return path, visited,elapsed_time
        for neigbor in maze[v]: 
            if neigbor not in visited:
                stack.append(neigbor) 
                path1[neigbor]=v 
    return None

def BFS(maze,begin,end):
    start = timer()
    visited=[]
    path=[]
    path1={}
    queue=deque()
    queue.append(begin)
    while len(queue)!=0:
        v=queue.popleft()
        visited.append(v)
        if(v==end):
            path.append(v)
            while v!=begin:
                v=path1[v]
                path.append(v)
            path.reverse()
            end = timer()
            elapsed_time = end - start
            return path, visited,elapsed_time
        for neigbor in maze[v]:
            if neigbor not in visited:
                path1[neigbor]=v
                queue.append(neigbor)
    return None
               
def UCS(maze,begin,end):
    start = timer()
    visited=[]
    path=[]
    path1={}
    cost={}
    cost[begin]=0
    queue=PriorityQueue()
    queue.put((0,begin))
    while queue!=None:
        v=queue.get()[1]
        visited.append(v)
        if(v==end):
            path.append(v)
            while v!=begin:
                v=path1[v]
                path.append(v)
            path.reverse()
            end = timer()
            elapsed_time = end - start
            return path, visited,elapsed_time
        for neigbor in maze[v]:
            if neigbor not in visited:
                cost[neigbor]=cost[v] + 1
                path1[neigbor]=v
                queue.put((cost[neigbor],neigbor))
    return None
def manhattan_distance(begin,end,n):
    des1,des2=divmod(int(end),n)
    beg1,beg2=divmod(int(begin),n)
    return (abs(beg1 - des1) + abs(beg2 - des2))
    

def GDFS(maze,begin,end,sizemaze):
    start = timer()
    path=[]
    path1={}
    queue=PriorityQueue()
    queue.put((manhattan_distance(begin, end,sizemaze),begin))
    visited=[]
    while queue!=None:
        v=queue.get()[1]
        visited.append(v)
        if(v==end):
            path.append(v)
            while v!=begin:
                v=path1[v]
                path.append(v)
            path.reverse()
            end = timer()
            elapsed_time = end - start
            return path,visited,elapsed_time
        for neighbor in maze[v]:
            if neighbor not in visited:
                path1[neighbor]=v
                queue.put((manhattan_distance(neighbor,end,sizemaze),neighbor))
    return None

def astar(maze,begin,end,sizemaze):
    start = timer()
    visited=[]
    path=[]
    path1={}
    queue=PriorityQueue()
    queue.put((0+manhattan_distance(begin,end,sizemaze),begin))
    cost={}
    cost[begin] = 0
    while queue!=None:
        v=queue.get()[1]
        visited.append(v)
        if(v==end):
            path.append(v)
            while v!=begin:
                v=path1[v]
                path.append(v)
            path.reverse()
            end = timer()
            elapsed_time = end - start
            return path,visited,elapsed_time
        for neighbor in maze[v]:
            if neighbor not in visited:
                cost[neighbor] =cost[v]+ 1
                queue.put((cost[neighbor]+manhattan_distance(neighbor, end,sizemaze),neighbor))
                path1[neighbor]=v
    return None
def printBFS(filename,maze,begin,end):
    result,visited,time=BFS(maze,begin,end)
    file=open(filename,"a")
    file.write("BFS\n")
    file.write("Solution: ")
    for x in result:
        file.write("%s "%x)
    file.write("\nVisited: ")
    for x in visited:
        file.write("%s "%x)
    file.write("\nLength of visiting:")
    file.write(str(len(visited)))
    file.write("\nTime: ")
    file.write(str(time))
    file.write(" second\n\n")
    file.close()
def printDFS(filename,maze,begin,end):
    result,visited,time=DFS(maze,begin,end)
    file=open(filename,"a")
    file.write("DFS\n")
    file.write("Solution: ")
    for x in result:
        file.write("%s "%x)
    file.write("\nVisited: ")
    for x in visited:
        file.write("%s "%x)
    file.write("\nLength of visiting:")
    file.write(str(len(visited)))
    file.write("\nTime: ")
    file.write(str(time))
    file.write(" second\n\n")
    file.close()
def printUCS(filename,maze,begin,end):
    result,visited,time=UCS(maze,begin,end)
    file=open(filename,"a")
    file.write("UCS\n")
    file.write("Solution: ")
    for x in result:
        file.write("%s "%x)
    file.write("\nVisited: ")
    for x in visited:
        file.write("%s "%x)
    file.write("\nLength of visiting:")
    file.write(str(len(visited)))
    file.write("\nTime: ")
    file.write(str(time))
    file.write(" second\n\n")
    file.close()

def printGDFS(filename,maze,begin,end,size):
    result,visited,time=GDFS(maze,begin,end,size)
    file=open(filename,"a")
    file.write("GDBFS\n")
    file.write("Solution: ")
    for x in result:
        file.write("%s "%x)
    file.write("\nVisited: ")
    for x in visited:
        file.write("%s "%x)
    file.write("\nLength of visiting: ")
    file.write(str(len(visited)))
    file.write("\nTime: ")
    file.write(str(time))
    file.write(" second\n\n")
    file.close()

def printAstar(filename,maze,begin,end,size):
    result,visited,time=astar(maze,begin,end,size)
    file=open(filename,"a")
    file.write("A star\n")
    file.write("Solution: ")
    for x in result:
        file.write("%s "%x)
    file.write("\nVisited: ")
    for x in visited:
        file.write("%s "%x)
    file.write("\nLength of visiting:")
    file.write(str(len(visited)))
    file.write("\nTime: ")
    file.write(str(time))
    file.write(" second\n\n")
    file.close()

def main(inputfile,outputfile):
    maze,begin,end,n=readfile(inputfile)
    printDFS(outputfile,maze,begin,end)
    printBFS(outputfile,maze,begin,end)
    printUCS(outputfile,maze,begin,end)
    printGDFS(outputfile,maze,begin,end,n)
    printAstar(outputfile,maze,begin,end,n)

main("input_maze2.txt","output_maze2.txt")





