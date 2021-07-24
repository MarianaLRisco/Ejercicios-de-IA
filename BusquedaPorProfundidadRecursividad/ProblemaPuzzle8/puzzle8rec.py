import numpy as np
import sys
sys.setrecursionlimit(10000)

def in_list(node,list_nodes):
    for n in list_nodes:
        if (node == n).all():
            return True
    return False

def swap(matrix, index1 , index2):
    temp = matrix[tuple(index1)]
    matrix[tuple(index1)] = matrix[tuple(index2)]
    matrix[tuple(index2)] = temp
    return matrix

solution = np.array([[1,2,3],
                     [8,0,4],
                     [7,6,5]])
visited_nodes = []
movements = [[1,0],[0,1],[0,-1],[-1,0]]

def depth_first_search(node,result):
    # print(node,'_________________\n')
    visited_nodes.append(node)
    if (node == solution).all():
        return result

    x,y = np.where(node == 0)
    childs = []
    for move in movements:
        if 0 <= x + move[0] <= 2\
        and 0 <= y + move[1] <= 2:
            child = swap(node.copy(), [x,y],[x+move[0], y+move[1]])
            childs.append(child)
            # visited_nodes.append(child)
            # print(child,'\n')
    for child in childs:    
        if not in_list(child,visited_nodes):
            sol = depth_first_search(child, result+[child])
            if sol:
                return sol


if __name__ == "__main__":

    # init_state= np.array([[5,4,0],
    #                       [6,1,8],
    #                       [7,3,2]])
    init_state= np.array([[1,0,3],
                          [8,2,6],
                          [7,5,4]])

    results = depth_first_search(init_state, [init_state])
    for result in results:
        print(result,'\n')