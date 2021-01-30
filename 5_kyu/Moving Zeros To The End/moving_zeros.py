"""
Task
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""
def move_zeros(array):
    temp=[]
    l=len(array)
    zeros=0
    for i in range(0,l):
        if array[i] == False and type(array[i]) is bool:
            temp.append(False)
        elif array[i] == 0:
            zeros+=1
        else:
            temp.append(array[i])
    for j in range(0,zeros):
        temp.append(0)
    return(temp)
    