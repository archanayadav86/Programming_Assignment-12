#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to Extract Unique values dictionary values?

# In[35]:


dict_1={'d':[1,2,3,4], 'e':[3,7,9,6,4], 'f':[9,8,0,6,4]}


# In[36]:


for i in dict_1.values():
    print(i)


# In[44]:


temp = [i for ele in dict_1.values() for i in ele]
l = []
for key, vals in dict_1.items():
    for val in vals:
        if temp.count(val) == 1:
            l.append(key)
            break


# In[45]:


temp


# In[46]:


set(temp)


# In[ ]:


2.	Write a Python program to find the sum of all items in a dictionary


# In[48]:


dict_2={'d':[1,2,3,4], 'e':[3,7,9,6,4], 'f':[9,8,0,6,4]}


# In[96]:


l1=[]
for i in dict_2.values():
    l1=l1+i
    
        
      


# In[97]:


l1


# In[98]:


sum(l1)


# 3.	Write a Python program to Merging two Dictionaries?

# In[16]:


dict_3={'d':[1,2,3,4], 'e':[3,7,9,6,4]} 
dict_4={'d':[9,8,0,6,4],'e':[5,7,9,55,44]}
d3={}
for i,j in dict_3.items():
    for k,v in dict_4.items():
        if i== k:
            d3[i]=(j+v)
            print(d3)
    


# In[17]:


d3


# In[31]:


dict_3={'d':[1,2,3,4], 'e':[3,7,9,6,4]} 
dict_4={'f':[9,8,0,6,4],'g':[5,7,9,55,44]}
d3= Merge(dict_3,dict_4)
d3


# In[32]:


d3


# In[23]:


def Merge(dict1,dict2):
    return(dict2.update(dict1))

dict1={'d':[1,2,3,4], 'e':[3,7,9,6,4]} 
dict2={'f':[9,8,0,6,4],'g':[5,7,9,55,44]}

print(Merge(dict1,dict2))
print(dict2)


# 4.	Write a Python program to convert key-values list to flat dictionary?

# In[27]:


dict4={'d':[1,2,3,4], 'e':[3,7,9,6,4],'g':[5,3,5]} 
l=[]
for i in dict4.keys():
    l.append(i)
print(l)
    


# 5.	Write a Python program to insertion at the beginning in OrderedDict?

# In[34]:


from collections import OrderedDict
 
orderd_dict = OrderedDict([('a', '1'), ('b', '2')])
 

orderd_dict.update({'c':'3'})
orderd_dict.move_to_end('c', last = False)
 
# print result
print ("Updated Dictionary : "+str(orderd_dict))


# 6.	Write a Python program to check order of character in string using OrderedDict()?

# In[69]:


from collections import OrderedDict 
def checkOrder(string, pattern): 
    dic = OrderedDict.fromkeys(string) 
    str = 0
    for key,value in dic.items(): 
        if (key == pattern[str]): 
            str = str + 1
        if (str == (len(pattern))): 
            return 'True'
    return 'False'

string = 'Electronics'
pattern = 'lec'
print (checkOrder(string,pattern))

string2= 'Engineering'
pattern2= 'rng'
print (checkOrder(string2,pattern2)) 


# 7.	Write a Python program to sort Python Dictionaries by Key or Value?

# In[51]:


dic5={'f':[9,8,0,6,4],'g':[5,7,9,55,44]}
i=dic5.keys()
i


# In[52]:


dic5={'f':[9,8,0,6,4],'g':[5,7,9,55,44]}
j=dic5.values()
j


# In[60]:


print(("The keys of dictionary:", i) +  ("The values of dictionary:", j))


# In[ ]:




