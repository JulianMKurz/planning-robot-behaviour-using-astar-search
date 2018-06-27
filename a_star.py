#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:05:42 2017

@author: julian kurz
"""

import heapq

class StateRepresentation:
    def __init__(self):
        self.edges = {}
        
    def get_neighbours(self, id):
        return self.edges[id]
    
    
    
state_representation = StateRepresentation()
state_representation.edges = {
        "S": [("-s", 1), ("-l", 1), ("-ma", 2), ("-mb", 2)],
        "-s": [("S", 1), ("-ma", 1), ("-mb", 2)],
        "-l": [("S", 1), ("-mb", 1), ("-ma", 2)],
        "-ma": [("-s", 1), ("-l", 1), ("-ma", 2), ("-mb", 2)],
        "-mb": [("-s", 1), ("-l", 1), ("-ma", 2), ("-mb", 2)]
        }

class ActionsLookedAt:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def leng(self):
        return len(self.elements)
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
    

    

heuristic_1 = lambda x: sum(x)
heuristic_2 = lambda x: sum(x) + (abs(x[0]-x[2]) + abs(x[1] - x[2]))
heuristic_pessimistic = lambda x: sum(x) + (abs(x[0]+x[1]-x[2]-x[3]))

        

def a_star(parcels, heuristic, state_representation):
    nodes_opened = ActionsLookedAt()
    start_node = (parcels, "S")
    nodes_opened.put(start_node, heuristic(parcels))
    precessor = {}
    cost_so_far = {}
    precessor[start_node] = []
    cost_so_far[start_node] = 0
    
    while not nodes_opened.empty():
        current_node = nodes_opened.get()
        
        if current_node[0] == (0,0,0,0):
            result = []
            precessing_node = current_node
            while True:
                result.insert(0, precessing_node)
                
                precessing_node = precessor[precessing_node]
                
                if precessing_node == []:
                    break
                
            print(nodes_opened.leng())
            print(result)
            break
        
        for neighbour in state_representation.get_neighbours(current_node[1]):
            new_cost = cost_so_far[current_node] + neighbour[1]
            
            if neighbour[0] == "S":
                neighbour_node = (current_node[0], "S")
                
            elif neighbour[0] == "-s":
                placeholder_node = current_node[0]
                
                lst = list(placeholder_node)
                lst[0] -= 1
                placeholder_node = tuple(lst)
                
                neighbour_node = (placeholder_node, "-s")
                
            elif neighbour[0] == "-l":
                placeholder_node = current_node[0]
                lst = list(placeholder_node)
                lst[1] -= 1
                placeholder_node = tuple(lst)
                
                neighbour_node = (placeholder_node, "-l")
                
            elif neighbour[0] == "-ma":
                placeholder_node = current_node[0]
                lst = list(placeholder_node)
                lst[2] -= 1
                placeholder_node = tuple(lst)
                
                neighbour_node = (placeholder_node, "-ma")
                
            elif neighbour[0] == "-mb":
                
                placeholder_node = current_node[0]
                lst = list(placeholder_node)
                lst[3] -= 1
                placeholder_node = tuple(lst)
                
                neighbour_node = (placeholder_node, "-mb")
            
           
            if (neighbour_node not in cost_so_far or new_cost < cost_so_far[neighbour_node]) and min(neighbour_node[0]) >= 0:
               cost_so_far[neighbour_node] = new_cost
               priority = new_cost + heuristic(neighbour_node[0])
               nodes_opened.put(neighbour_node, priority)
               precessor[neighbour_node] = current_node
    
    return precessor, cost_so_far

a_star((10,14,36,8), heuristic_1, state_representation)
a_star((10,4,6,8), heuristic_2, state_representation)


