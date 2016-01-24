# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(0, t) :
    inp = raw_input()
    mylist = inp.split(" ", 3)
    a = int(mylist[0])
    b = int(mylist[1])
    n = int(mylist[2])
    
    s = ""
    inc = a
    for j in range(0, n) :
        inc += ((2**j) * b)
        s = s + str(inc)
        if(j != n-1) :
            s = s + " "
    print s