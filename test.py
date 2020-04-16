from collections import defaultdict
import numpy as np

#the following code's psuedo code was taken from
# https://stackoverflow.com/questions/25340898/algorithm-to-find-and-print-simple-cycle-in-complexity-of-on-on-undirected-gra

class Graph:
    # Constructor
    def __init__(self, V, E):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = V
        self.E = E
        self.p = [None] * V
        self.color = defaultdict(list)
        self.loopElem = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def Visit(self, u):
        cycle = False
        #partially visited the node
        self.color[u] = 1
        # print(u)
        for i in self.graph[u]:
            #if the node is unvisited i.e. white
            if self.color[i] == 0:
                # we saying that u is the parent of i
                self.p[i] = u
                self.Visit(i)

            elif self.color[i] == 1:
                cycle = True
                self.loopElem = i
                break
    #DFS has reached its end, we are assigning black color to it
        self.color[u] = 2

        if cycle:
            print("cycle detected")
            self.PrintCycle(self.loopElem, u)

# we are sending loopElement and its adjacent element
    def PrintCycle(self, v, u):
        if v == u :
            print(v)
        else:
            print(v)
            self.PrintCycle(self.p[v], u)

    def DFSCheckCycle(self,s):
        # for v in self.graph:
        #white = 0, grey = 1, black = 2,
        # initially allot all the nodes white color
        self.color = [0] * self.V

        # print(s)
        self.p[s] = -1
        for u in self.graph[s]:
            if self.color[u] == 0:
                #to indicate the root
                self.p[u] = s
                self.Visit(u)
            else:
                self.PrintCycle(u, s)



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
    # to get the edges data from 3rd index in data array
    for i in data[2:]:
        g.addEdge(i[0], i[1])

    g.DFSCheckCycle(0)



