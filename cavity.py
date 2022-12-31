import math
import os
import random
import re
import sys

def cavityMap(grid):
    
    for i in grid:
        if len(i) <= 2:
            pass
        else:
            list_int = []
            front = int(i[0])
            end = int(i[-1])
            cavities = i[1:-1]
            
            for cav in cavities:
                list_int.append(int(cav))
                
            cavity = max(list_int)
            if cavity > front and cavity > end:
                grid[grid.index(cavity)] = "X"
            else:
                pass
                
    return grid    