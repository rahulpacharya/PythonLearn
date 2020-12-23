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

# BINOMIAL EXPERIMENT
# 80 % of people who purchase pet insurance are women. 
# If 9 pet insurance owners are randomly selected, 
# find the probability that precisely 6 are women.

#n=9
#p=0.80
#x=6
from scipy import stats
probability=stats.binom.pmf(6,9,0.80)
print("Probablity of precisely 6 women selected: ",probability)

# POISSON EXPRIMENT
# If the number of vehicles that pass through a junction on a 
# busy road is at an average rate of 300 per hour, 
# find the probability that no vehicle passes in a given minute.

from scipy import stats
averagepass=300/60
probability=stats.poisson.pmf(0, averagepass)
print("Probability that no vehicle pass: ",probability)

## CHI SQUARED TEST
# The following Contigency table shows the subject preference 
# of left-handed and right- handed individuals
# Use Chi-squared test to test Homogeneity.
#Subject	Left-handed	Right-handed
#Science	30	           10
#Maths	    15	           25
#Comp Sc 	15	           5

#Null Hypothesis
# There is no difference in distribution between 
# left-handed and right-handed individuals in terms of preference 
# of subjects.

# Alternate Hypotheis
#There is a difference in subject preference between left-handed 
#and right-handed individuals.

from scipy.stats import chi2_contingency
from scipy.stats import chi2
table =[[30, 10], [15, 25], [15, 5]]
stat,p,dof,expected = chi2_contingency(table)
print("Chi squared test:")
print("statistics and p value and degrees of freedom: ",stat,p,dof)
print("expected values: ",expected)
prob = 0.95
critical = chi2.ppf(prob, dof)
print("Critical value: ",critical)
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')

	


