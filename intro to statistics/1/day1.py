# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
N = int(raw_input())
S = raw_input()
As = S.split(" ")

for i in range(0, N):
    As[i] = int(As[i])

def InsertionSort(Arr):
    check = 0
    n = len(Arr)
    index = 0
    while( check == 0):
        if (Arr[index] != Arr[n-1]):
            if(Arr[index] > Arr[index+1]):
                swap = Arr[index+1]
                Arr[index+1] = Arr[index]
                Arr[index] = swap
                index = 0
            else:
                index = index + 1
        else:
            check = 1
            return Arr
        
def histogram(Arr):
    D = dict()
    for i in range(0, len(Arr)):
        if( Arr[i] not in D):
            D[Arr[i]] = 1
        else:
            D[Arr[i]] = D[Arr[i]] + 1
    return D
    
def Mean(Arr):
    sum = 0
    for i in range(0, len(Arr)):
        sum = sum + Arr[i]
    mean = sum / len(Arr)
    return mean

def Median(Arr):
    if(len(Arr)%2 == 0):
        Arr = InsertionSort(Arr)
        sum = Arr[int((len(Arr)/2) - 1)] + Arr[int(len(Arr)/2)]
        avg = sum / 2
        return avg
def Mode(Dict):
    
    
print Mean(As)
print Median(As)
print histogram(As)