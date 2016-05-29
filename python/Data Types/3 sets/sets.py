# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = (raw_input())
setraw1 = raw_input() # get space separated string input
setstring1 = setraw1.split() # split to list of strings
#print setstring1
setlist1 = list(map(int, setstring1)) # convert to int
set1 = set(setlist1)
#print set1

n2 = int(raw_input())
setraw2 = raw_input()
setstring2 = setraw2.split()
#print setstring2
setlist2 = list(map(int, setstring2))
set2 = set(setlist2)
#print set2

setdiff1 = set1.difference(set2)
setdiff2 = set2.difference(set1)
setsym = setdiff1
setsym.update(setdiff2)

listsym = list(setsym) 
listsymsort  = sorted(listsym)
for i in range(0, len(listsymsort)):
    print listsymsort[i]