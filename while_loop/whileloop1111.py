squares=["orange","orange","orange","yellow","green","orange","red","orange"]
Newsquare=[]
Othersquare=[]
i=0
while(i<len(squares)):
    if(squares[i]=="orange"):
        Newsquare.append(squares[i])
        i=i+1
    else:
        Othersquare.append(squares[i])
        i=i+1
print("Only orange extracted: ",Newsquare)
print("Except orange: ",Othersquare)
