#Program to compare number of function/search calls for a list of numbers stored in an
#array vs binary search tree based on the height of the tree resulting from the degree of randomization of the input data

import random
import matplotlib.pyplot as plt
import numpy as np

#creates Node class
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                 self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def findVal(self, val, call_count):
        if val < self.data:
            if self.left is None:
                return str(val) +" Not Found"
            return self.left.findVal(val, call_count+1)
        elif val > self.data:
            if self.right is None:
                return str(val) +" Not Found"
            return self.right.findVal(val, call_count+1)
        else:
            return call_count

class tree_stats:
    def __init__(self):
        self.height = 0
        self.call_count_avg = 0

def height(root):
    if root is None:
        return 0
    l_height = height(root.left)
    r_height = height(root.right)
    return max(l_height, r_height) + 1

#swaps 2 random positions in array
def swap(curr_list):
    n = random.randint(0, size - 1)
    r = random.randint(0, size - 1)
    curr_list[r], curr_list[n] = curr_list[n], curr_list[r]
    return curr_list

#figures average number of function calls to search for each element in list stored in binary tree
def tree_calc(num_list, curr_list, size):
    root = Node(0)
    call_cnt_tree_list = []

    for i in range(size):
        root.insert(curr_list[i])

    tree_stats.height = height(root)    

    for i in range(0, size):
        call_count = 1
        call_count = root.findVal(num_list[i], call_count)
        call_cnt_tree_list.append(call_count)
   
    tree_stats.call_count_avg = sum(call_cnt_tree_list) / len(call_cnt_tree_list)

    return tree_stats

#figures average number of search iterations to find each element in array
def array_search(num_list, curr_list, size): 
    search_cnt_list = []
    search_cnt_avg = []
    
    for i in range(0, size):
        search_cnt = 0
        while num_list[i] != curr_list[search_cnt]:
            search_cnt += 1

        search_cnt_list.append(search_cnt+1)
   
    search_cnt_avg = sum(search_cnt_list) / len(search_cnt_list)
    return search_cnt_avg
 
    
num_list = []
curr_list = []
size = 100
runs = 50
randomize_cnt_list = list(range(runs))
tree_avg_call_cnt_list = []
array_avg_search_cnt = []
height_list = []

for i in range(size):
    num_list.append(i)
    curr_list.append(i)

for i in range(0, runs):
    curr_tree_stat = tree_calc(num_list, curr_list, size)
    tree_avg_call_cnt_list.append(curr_tree_stat.call_count_avg)
    height_list.append(curr_tree_stat.height)
    array_avg_search_cnt.append(array_search(num_list, curr_list, size))
    curr_list = swap(curr_list)

fig, ax = plt.subplots(figsize = (10, 5))
plt.title('Number of Search calls in Binary Tree by Data Randomization and Tree Height')
ax2 = ax.twinx()
ax.plot(randomize_cnt_list, tree_avg_call_cnt_list, color = 'g')
ax2.bar(randomize_cnt_list, height_list, color = 'b', alpha=.25)
ax.set_xlabel('Number of Randomizations', color = 'k')
ax.set_ylabel('Average Number of Function Calls in Search', color = 'k')
ax2.set_ylabel('Tree Height', color = 'k')
plt.tight_layout()
plt.show()











