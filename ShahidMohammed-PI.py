#this code was taken from the lecture notes and modified as per the requirement
# author: Shahid Mohammed Shaikbepari

from collections import defaultdict
import numpy as np

# This class represents a directed graph using adjacency
# list representation
class Graph:

    # Constructor
    def __init__(self, V, E):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = V
        self.E = E

    # def node(self, value):
    #     self.value = value
    #     self.visited = False

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = {}
        # countForConnectCheck = 0
        # for i in self.graph:
        #     visited[i] = False
        visited = [False] * self.V
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s)
            # countForConnectCheck += 1

            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                else:
                    return False, i

        # print("\n")
        return True, -1
        # return countForConnectCheck

    def DFSUtil(self, v, visited, cycle):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        #append the element to the stack
        cycle.append(v)
        # Recur for all the vertices adjacent to this vertex

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, cycle)
            else:
                print(cycle)
                #return cycle
        #as the node reached its end and didn't find loop remove it
        cycle.pop()




    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        cycle = []
        # Call the recursive helper function to print
        # DFS traversal
        # for i in self.graph[v]:
        self.DFSUtil(v, visited, cycle)
            # print("\n")

def extractData(fileName):
    # taken from my prev 595 labs
    f = open(fileName, 'r+')
    data = [np.fromstring(line, dtype=int, sep=',') for line in f.readlines()]
    f.close()
    return data


if __name__ == '__main__':

    data = extractData('input.txt')

    V = data[0][0]
    E = data[1][0]
    g = Graph(V,E)

    #to get the edges data from 3rd index in data array
    for i in data[2:]:
        g.addEdge(i[0], i[1])

    result, LoopElement =  g.BFS(0)
    if result is False:
        print("This graph is not a tree. A loop in this graph:" + str(LoopElement))
    else:
        print("This graph is a tree, i.e., it does not have a loop")
    g.DFS(LoopElement)