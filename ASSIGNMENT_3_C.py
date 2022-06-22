#!/usr/bin/env python
# coding: utf-8

# In[113]:


def get_no_of_elements(numbers):
    n = 0
    for element in list:
        n += 1
    return n

input_data = input("Enter the numbers separated by space:-")
list  = input_data.split()
for numbers in list:
    numbers    
print("Number of elements in the list:- ", get_no_of_elements(list))


# In[114]:


def mymax():    
    mylist = []
    size = int(input('How many elements you want to enter:-'))
    print('Enter',str(size),'numbers')

    for i in range(size):
        data = int(input())
        mylist.append(data)

    larg = 0
    for data in mylist:
        if data > larg:
            larg = data

    print('The largest number in list is', larg)    
mymax()


# In[117]:


def reverse():
    numbers_in = input("Enter the numbers separated by space:- ")
    rev = numbers_in[::-1]
    print('Reversed List:- ', rev)
reverse()


# In[118]:


def sum_of_list(numlist):
    total = 0
    for x in range(number):
        total = total + numlist[x]
    return total


numlist = []
number = int(input("Please enter the Total Number of List Elements:- "))
for i in range(1, number + 1):
    value = int(input("Please enter the Value of %d Element :-" %i))
    numlist.append(value)

total = sum_of_list(numlist)
print("\n The Sum of All Element in this List is :-", total)

