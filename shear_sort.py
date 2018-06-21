import numpy as np
from random import randint
from math import log,ceil
A = np.array(np.random.permutation(np.arange(0,16)))
A = np.reshape(A,(4,4))

def comp_swap(i,j,S):
    '''
    Compares elements at indices i and j
    and swaps them if S[i] > S[j]
    Assumes index i is less than j
    '''
    if i < j:
        if S[i] > S[j]:
            S[i],S[j] = S[j],S[i]
    else:
        if S[i] < S[j]:
            S[i],S[j] = S[j],S[i]

    
def odd_even_sort(S):
    '''
    does log(n) round of odd-even-compare exchange to sort Sequence s
    '''
    i = 0
    n = len(S)
    count = 0
    max_cycles = n 
    Ssorted = sorted(S)
    while i < max_cycles :
        if Ssorted != S:
            count += 1
        # compare odd indices
        if i % 2 == 0:
            j = 0
            while j < n - 1:
                comp_swap(j,j+1, S)
                print("Comparing S[{}]= {} S[{}]={}".format(j,S[j],j+1,S[j+1]))
                print("Result {}".format(S))
                j += 2 
        # compare odd indices
        else:
            j = 1
            while j < n:
                # we use mod here for case when j=n
                # and then comparison wraps around to
                # front of array
                comp_swap(j, (j+1) % n, S)
                print("Comparing S[{}]= {} S[{}]={}".format(j,S[j],(j+1)% n,S[(j+1) % n]))
                print("Result {}".format(S))
                j += 2
        i += 1
        print()
    print("Rounds till sorted:", count)
    print("Rounds: ", max_cycles)

S = [randint(0,64) for i in range(64,0,-1)]
odd_even_sort(S)
print(S)









#print(A)
'''
Algo should go something like this
S is a sequence of length n

assume n is square number. 
assume n is divisible by k 
Pi is proocessor i

1) restructure array so Pi is assigned to the subsequence from
(i-1)n/k to n/k * i

set is_even_cycle to true

while Matrix not sorted:
    if even cycle:
        sort each in increaing order if i is even and
            decreasing order otherwise
        set is_even_cycle to false
    else:
        transpose(M) # this is equiv to proccessor sending stuff
        sort each row of m in increasing
        transpose(M)
        set is_even_cycle to true

each P will use n/k log n/k comparisons to sort tehre values

suppose t = n/k which is the number of values a given proccessor
has in its memory. a given P will send t-1 values.

during an odd cycle then there are 
2[(n/k)(n/k - 1)] communications
during an even cycle there are 0 communications since 
the proccessor just sorts its own list. The nunmber of iterations 
is bounded by Log(m) where m is number of rows out of these 
log(m) steps only 1/2 the time you actually do a communication so its

log(m)/2 * 2[(n/k)(n/k - 1)] = log(m)*(n/k)(n/k - 1) <=
log(m)*(n^2)/k^2
'''
