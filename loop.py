#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Display numbers from a list using loop
l=[6,2,8,4,9,5,1,7]
for x in range(len(l)):
    print(l[x])


# In[18]:


#Count the total number of digits in a number
a=123456789
print(len(str(a)))


# In[16]:


#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
s=int(input("Enter your salary: "))
y=int(input("Enter year of service: "))
if(y==5):
    net_bonus=5*s
    print("Net bonus: ",net_bonus)
else:
    print("no bonus")


# In[19]:


#Take values of length and breadth of a rectangle from user and check if it is square or not.
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
if(l==b):
    print("It is square")
else:
    print("It is not a square")


# In[21]:


marks=int(input("Enter marks: "))
if(marks<25):
    print("F")
elif(marks>=25 and marks<45):
    print("E")
elif(marks>=45 and marks<50):
    print("D")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=60 and marks<80):
    print("B")
else:
    print("A")


# In[25]:


#Find max. & min of 3 numbers.
n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
n3=int(input("Enter third number :"))
l=[n1,n2,n3]
print(l)
l.sort()
print(l)
print("max: ",l.pop())
l.reverse()
print("min: ",l.pop())


# In[27]:


#Swap 2 numbers without using temp. variable.
n1=int(input("Enter first number :"))
n2=int(input("Enter second number :"))
print("Before Swapping: ",n1,n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After Swapping: ",n1,n2)


# In[28]:


#Take input of age of 3 people by user and determine oldest and youngest among them.
a=int(input("Enter age of 1st people: "))
b=int(input("Enter age of 2nd people: "))
c=int(input("Enter age of 3rd people: "))
l=[a,b,c]
print(l)
l.sort()
print(l)
print("oldest: ",l.pop())
l.reverse()
print("Youngest: ",l.pop())


# In[32]:


a=int(input("Number of classes held: "))
b=int(input("Number of classes attended: "))
attendence=b*100/a
print(attendence)
if(attendence>75):
    print("Allowed")
else:
    print("Not Allowed")


# In[ ]:





# In[ ]:




