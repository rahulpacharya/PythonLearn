# -*- coding: utf-8 -*-

## Find the number of permutations and combinations that can be 
## formed from the word HORSE taking two letters at a time.

from itertools import combinations
from itertools import permutations 
import numpy as np
import math
arr=np.array(['H','O','R','S','E'])
print(len(list(combinations(arr,2)) ))
print(len(list(permutations(arr,2) ))) 

########################################
## In how many ways can 10 balls be picked, from 7 red out of 10,
## and 3 blue out of 8?
#######
## 10C3 (red comb) * 8C3 (blue comb)
##########
import math
red=math.factorial(10)/((math.factorial(7))*math.factorial(3))
blue=math.factorial(8)/((math.factorial(3))*math.factorial(5))
print(red*blue)
###########################
def combinations_num(n,r):
    return(math.factorial(n)/((math.factorial(n-r))*math.factorial(r)))
def permutation_num(n,r):
    return(math.factorial(n)/((math.factorial(n-r))))

red=combinations_num(10,7)
blue=combinations_num(8,3)
print(red*blue)
#####################################
## lists the marks of students by name
## Find Mean, Median, Mode, SD, IQR
from scipy import stats
import numpy as np
import statistics
dic ={"A": 90,"B": 86,"C":70,"D":95,"E":95,"F":95,"G":95}

print(dic.values())
print("Mean")
print(np.mean(list(dic.values())))
print("Median")
print(np.median(list(dic.values())))
print("Mode")
print(statistics.mode(list(dic.values())))
print("Standard Deviation")
print(np.std(list(dic.values())))
print("Variance")
print(np.var(list(dic.values())))
print("range")
print(stats.iqr(list(dic.values())))
#########################################





