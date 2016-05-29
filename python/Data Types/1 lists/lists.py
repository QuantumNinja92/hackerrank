# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
Data = []
rawInput =  raw_input()

while True:
    Data = rawInput.split(" ")
    
    # Case Print
    if(Data[0]  == "print"):
        print L
    
    # Case Insert
    elif(Data[0] == "insert"):
        L.insert(int(Data[1]), int(Data[2]))
    
    # Case append
    elif(Data[0] == "append"):  
        L.append(int(Data[1]))
        
    # Case remove
    elif(Data[0] == "remove"):
        L.remove(int(Data[1]))
        
    # Case pop
    elif(Data[0] == "pop"):
        L.pop()
        
    # Case index
    elif(Data[0] == "index"):
        print "Index"
        
    # Case count
    elif(Data[0] == "count"):
        print "Count"
        
    # Case sort
    elif(Data[0] == "sort"):
        L.sort()
    # Case reverse
    elif(Data[0] == "reverse"):
        L.reverse()
        
    try:
        rawInput = raw_input()
        Data = rawInput.split(" ")
    except (EOFError):
        break #end of file reached
    

 