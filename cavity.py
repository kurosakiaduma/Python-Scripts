import math
import os
import random
import re
import sys

def cavityMap(grid):
    
    for idx, i in enumerate(grid):
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
                grid[idx] = i.replace(str(cavity), "X")
            else:
                pass
                
    return grid


if __name__ == "__main__":
    cavityMap(['1112', '1912', '1892', '1234'])