#!/usr/bin/env python
# coding: utf-8

# In[15]:


def countOddEven(tu):
    countO=0
    countE=0
    for i in tu:
        if(i%2==0):
            countE+=1
        else:
            countO+=1
    print("Total number of even number: ",countE)
    print("Total numbar of odd number: ",countO) 
t=[1,2,3,4,5,6,7,8,9]
print("All element in the tuple: ",t)
countOddEven(t)

