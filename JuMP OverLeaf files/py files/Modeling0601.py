#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# ### Kristina Wilson and Noah Dahle 
# 
# ### Modeling Travel Times to Determine Shortest Path
# 
# Experimenting with a potential model.  
# 
# Implementing functions that have stored in the google maps traffic simulation data.  
# 
# This is an elementary model. Hopefully I can develop one with more variables later on!

# In[5]:


#car.update({'color': 'white'})
#car


# Maybe make a dictionary defining the times and nodes, then create a list with all info. (Times in 24HR)

# ## Times List

# In[6]:


times = []
val = 600
for i in range(0, 17): 
    if (val % 100) == 60: 
        val += 40
    times.append((i, val))
    val += 15
times


# In[36]:


times = []
val = 600
for i in range(0, 17): 
    if (val % 100) == 60: 
        val += 40
    times.append(val)
    val += 15
times


# We need to account for one ways. So those would not need to be in the dictionary. (Later)

# ## Edges List

# In[8]:


input1 = [('1', 'A', 'B'), ('2', 'B', 'D'), ('3', 'B', 'E'), ('4', 'A', 'C'), ('5', 'D', 'M'), ('6', 'C', 'F'), ('7', 'F', 'G'), ('8', 'G', 'H'), ('9', 'H', 'I'), ('10', 'I', 'J'), ('11', 'I', 'K'), ('12', 'J', 'L'), ('13', 'D', 'K'), ('14', 'K', 'L'), ('15', 'L', 'M'), ('16', 'M', 'N'), ('17', 'E', 'N'), ('18', 'N', 'O'), ('19', 'D', 'F'), ('20', 'G', 'K')]


# In[9]:


def edgeslist(input):
    output=[]
    length = len(input)
    for i in range(0, 2*length):
        output.append(input[math.floor(i/2)][0]+input[math.floor(i/2)][(i%2) + 1])
    return output


# In[20]:


edges = edgeslist(input1)


# In[35]:


len(edges)


# In[31]:


def traffic(times, edges):
    output = []
    for j in range(len(times)):
        print('You are entering conditions for', times[j])
        for i in range(len(edges)):
            condition = input("Enter the traffic condition for edge "+ edges[i]+ ": ")
            element = [600, edges[i], condition]
            output.append(element)
    return output


# In[33]:


HodgesNeyland = traffic(times, edges)


# In[48]:


j = 0
i = 0
while i!= len(HodgesNeyland):
    if i % 40 == 0 and i != 0: 
        j += 1
    HodgesNeyland[i][0] = times[j]
    i+= 1


# In[49]:


HodgesNeyland


# In[59]:


HodgesNeyland[500][2] = 'G'


# In[4]:


HodgesNeyland610 = [[600, '1A', 'NA'],
 [600, '1B', 'NA'],
 [600, '2B', 'GREEN'],
 [600, '2D', 'ORANGE'],
 [600, '3B', 'ORANGE'],
 [600, '3E', 'ORANGE'],
 [600, '4A', 'NA'],
 [600, '4C', 'NA'],
 [600, '5D', 'GREEN'],
 [600, '5M', 'GREEN'],
 [600, '6C', 'ORANGE'],
 [600, '6F', 'GREEN'],
 [600, '7F', 'GREEN'],
 [600, '7G', 'GREEN'],
 [600, '8G', 'GREEN'],
 [600, '8H', 'GREEN'],
 [600, '9H', 'NA'],
 [600, '9I', 'NA'],
 [600, '10I', 'NA'],
 [600, '10J', 'NA'],
 [600, '11I', 'GREEN'],
 [600, '11K', 'ORANGE'],
 [600, '12J', 'ORANGE'],
 [600, '12L', 'NA'],
 [600, '13D', 'ORANGE'],
 [600, '13K', 'GREEN'],
 [600, '14K', 'ORANGE'],
 [600, '14L', 'NA'],
 [600, '15L', 'ORANGE'],
 [600, '15M', 'NA'],
 [600, '16M', 'GREEN'],
 [600, '16N', 'NA'],
 [600, '17E', 'NA'],
 [600, '17N', 'NA'],
 [600, '18N', 'GREEN'],
 [600, '18O', 'GREEN'],
 [600, '19D', 'GREEN'],
 [600, '19F', 'GREEN'],
 [600, '20G', 'ORANGE'],
 [600, '20K', 'NA'],
 [615, '1A', 'NA'],
 [615, '1B', 'NA'],
 [615, '2B', 'GREEN'],
 [615, '2D', 'ORANGE'],
 [615, '3B', 'ORANGE'],
 [615, '3E', 'GREEN'],
 [615, '4A', 'NA'],
 [615, '4C', 'NA'],
 [615, '5D', 'GREEN'],
 [615, '5M', 'GREEN'],
 [615, '6C', 'ORANGE'],
 [615, '6F', 'GREEN'],
 [615, '7F', 'GREEN'],
 [615, '7G', 'GREEN'],
 [615, '8G', 'GREEN'],
 [615, '8H', 'GREEN'],
 [615, '9H', 'NA'],
 [615, '9I', 'GREEN'],
 [615, '10I', 'NA'],
 [615, '10J', 'NA'],
 [615, '11I', 'GREEN'],
 [615, '11K', 'ORANGE'],
 [615, '12J', 'ORANGE'],
 [615, '12L', 'NA'],
 [615, '13D', 'ORANGE'],
 [615, '13K', 'GREEN'],
 [615, '14K', 'ORANGE'],
 [615, '14L', 'NA'],
 [615, '15L', 'ORANGE'],
 [615, '15M', 'NA'],
 [615, '16M', 'GREEN'],
 [615, '16N', 'NA'],
 [615, '17E', 'NA'],
 [615, '17N', 'NA'],
 [615, '18N', 'GREEN'],
 [615, '18O', 'GREEN'],
 [615, '19D', 'GREEN'],
 [615, '19F', 'GREEN'],
 [615, '20G', 'ORANGE'],
 [615, '20K', 'NA'],
 [630, '1A', 'NA'],
 [630, '1B', 'NA'],
 [630, '2B', 'GREEN'],
 [630, '2D', 'GREEN'],
 [630, '3B', 'ORANGE'],
 [630, '3E', 'GREEN'],
 [630, '4A', 'NA'],
 [630, '4C', 'NA'],
 [630, '5D', 'GREEN'],
 [630, '5M', 'GREEN'],
 [630, '6C', 'ORANGE'],
 [630, '6F', 'GREEN'],
 [630, '7F', 'GREEN'],
 [630, '7G', 'GREEN'],
 [630, '8G', 'GREEN'],
 [630, '8H', 'GREEN'],
 [630, '9H', 'GREEN'],
 [630, '9I', 'GRENN'],
 [630, '10I', 'NA '],
 [630, '10J', 'NA'],
 [630, '11I', 'GREEN'],
 [630, '11K', 'ORANGE'],
 [630, '12J', 'RED'],
 [630, '12L', 'NA'],
 [630, '13D', 'ORANGE'],
 [630, '13K', 'GREEN'],
 [630, '14K', 'GREEN'],
 [630, '14L', 'NA'],
 [630, '15L', 'ORANGE'],
 [630, '15M', 'NA'],
 [630, '16M', 'GREEN'],
 [630, '16N', 'NA'],
 [630, '17E', 'NA'],
 [630, '17N', 'NA'],
 [630, '18N', 'GREEN'],
 [630, '18O', 'GREEN'],
 [630, '19D', 'GREEN'],
 [630, '19F', 'GREEN'],
 [630, '20G', 'GREEN'],
 [630, '20K', 'NA'],
 [645, '1A', 'NA'],
 [645, '1B', 'NA'],
 [645, '2B', 'GREEN'],
 [645, '2D', 'GREEN'],
 [645, '3B', 'ORANGE'],
 [645, '3E', 'GREEN'],
 [645, '4A', 'NA'],
 [645, '4C', 'NA'],
 [645, '5D', 'GREEN'],
 [645, '5M', 'GREEN'],
 [645, '6C', 'ORANGE'],
 [645, '6F', 'GREEN'],
 [645, '7F', 'ORANGE'],
 [645, '7G', 'GREEN'],
 [645, '8G', 'GREEN'],
 [645, '8H', 'GREEN'],
 [645, '9H', 'GREEN'],
 [645, '9I', 'GREEN'],
 [645, '10I', 'GREEN'],
 [645, '10J', 'NA'],
 [645, '11I', 'GREEN'],
 [645, '11K', 'ORANGE'],
 [645, '12J', 'RED'],
 [645, '12L', 'NA'],
 [645, '13D', 'ORANGE'],
 [645, '13K', 'GREEN'],
 [645, '14K', 'GREEN'],
 [645, '14L', 'NA'],
 [645, '15L', 'ORANGE'],
 [645, '15M', 'NA'],
 [645, '16M', 'GREEN'],
 [645, '16N', 'NA'],
 [645, '17E', 'NA'],
 [645, '17N', 'NA'],
 [645, '18N', 'GREEN'],
 [645, '18O', 'GREEN'],
 [645, '19D', 'GREEN'],
 [645, '19F', 'GREEN'],
 [645, '20G', 'GREEN'],
 [645, '20K', 'NA'],
 [700, '1A', 'NA'],
 [700, '1B', 'NA'],
 [700, '2B', 'GREEN'],
 [700, '2D', 'RED'],
 [700, '3B', 'RED'],
 [700, '3E', 'GREEN'],
 [700, '4A', 'NA'],
 [700, '4C', 'NA'],
 [700, '5D', 'GREEN'],
 [700, '5M', 'GREEN'],
 [700, '6C', 'ORANGE'],
 [700, '6F', 'G'],
 [700, '7F', 'O'],
 [700, '7G', 'G'],
 [700, '8G', 'G'],
 [700, '8H', 'G'],
 [700, '9H', 'G'],
 [700, '9I', 'G'],
 [700, '10I', 'G'],
 [700, '10J', 'G'],
 [700, '11I', 'G'],
 [700, '11K', 'G'],
 [700, '12J', 'R'],
 [700, '12L', 'NA'],
 [700, '13D', 'G'],
 [700, '13K', 'G'],
 [700, '14K', 'NA'],
 [700, '14L', 'NA'],
 [700, '15L', 'O'],
 [700, '15M', 'G'],
 [700, '16M', 'O'],
 [700, '16N', 'G'],
 [700, '17E', 'NA'],
 [700, '17N', 'NA'],
 [700, '18N', 'R'],
 [700, '18O', 'NA'],
 [700, '19D', 'G'],
 [700, '19F', 'G'],
 [700, '20G', 'G'],
 [700, '20K', 'NA'],
 [715, '1A', 'NA'],
 [715, '1B', 'NA'],
 [715, '2B', 'G'],
 [715, '2D', 'R'],
 [715, '3B', 'O'],
 [715, '3E', 'G'],
 [715, '4A', 'NA'],
 [715, '4C', 'NA'],
 [715, '5D', 'G'],
 [715, '5M', 'G'],
 [715, '6C', 'O'],
 [715, '6F', 'O'],
 [715, '7F', 'G'],
 [715, '7G', 'G'],
 [715, '8G', 'G'],
 [715, '8H', 'G'],
 [715, '9H', 'G'],
 [715, '9I', 'G'],
 [715, '10I', 'G'],
 [715, '10J', 'G'],
 [715, '11I', 'G'],
 [715, '11K', 'G'],
 [715, '12J', 'R'],
 [715, '12L', 'NA'],
 [715, '13D', 'G'],
 [715, '13K', 'G'],
 [715, '14K', 'NA'],
 [715, '14L', 'NA'],
 [715, '15L', 'O'],
 [715, '15M', 'G'],
 [715, '16M', 'O'],
 [715, '16N', 'G'],
 [715, '17E', 'NA'],
 [715, '17N', 'NA'],
 [715, '18N', 'R'],
 [715, '18O', 'NA'],
 [715, '19D', 'G'],
 [715, '19F', 'G'],
 [715, '20G', 'G'],
 [715, '20K', 'NA'],
 [730, '1A', 'NA'],
 [730, '1B', 'NA'],
 [730, '2B', 'G'],
 [730, '2D', 'G'],
 [730, '3B', 'G'],
 [730, '3E', 'G'],
 [730, '4A', 'NA'],
 [730, '4C', 'NA'],
 [730, '5D', 'G'],
 [730, '5M', 'G'],
 [730, '6C', 'O'],
 [730, '6F', 'G'],
 [730, '7F', 'O'],
 [730, '7G', ''],
 [730, '8G', 'G'],
 [730, '8H', 'G'],
 [730, '9H', 'G'],
 [730, '9I', 'G'],
 [730, '10I', 'NA'],
 [730, '10J', 'G'],
 [730, '11I', 'G'],
 [730, '11K', 'G'],
 [730, '12J', 'O'],
 [730, '12L', 'NA'],
 [730, '13D', 'G'],
 [730, '13K', 'G'],
 [730, '14K', 'NA'],
 [730, '14L', 'NA'],
 [730, '15L', 'O'],
 [730, '15M', 'R'],
 [730, '16M', 'O'],
 [730, '16N', 'G'],
 [730, '17E', 'NA'],
 [730, '17N', 'G'],
 [730, '18N', 'R'],
 [730, '18O', 'G'],
 [730, '19D', 'G'],
 [730, '19F', 'G'],
 [730, '20G', 'G'],
 [730, '20K', 'NA'],
 [745, '1A', 'NA'],
 [745, '1B', 'NA'],
 [745, '2B', 'GREEN'],
 [745, '2D', 'GREEN'],
 [745, '3B', 'GREEN'],
 [745, '3E', 'GREEN'],
 [745, '4A', 'NA'],
 [745, '4C', 'NA'],
 [745, '5D', 'GREEN'],
 [745, '5M', 'GREEN'],
 [745, '6C', 'O'],
 [745, '6F', 'G'],
 [745, '7F', 'O'],
 [745, '7G', 'G'],
 [745, '8G', 'G'],
 [745, '8H', 'G'],
 [745, '9H', 'G'],
 [745, '9I', 'G'],
 [745, '10I', 'NA'],
 [745, '10J', 'G'],
 [745, '11I', 'G'],
 [745, '11K', 'G'],
 [745, '12J', 'O'],
 [745, '12L', 'NA'],
 [745, '13D', 'G'],
 [745, '13K', 'G'],
 [745, '14K', 'NA'],
 [745, '14L', 'NA'],
 [745, '15L', 'R'],
 [745, '15M', 'R'],
 [745, '16M', 'R'],
 [745, '16N', 'O'],
 [745, '17E', 'NA'],
 [745, '17N', 'G'],
 [745, '18N', 'R'],
 [745, '18O', 'G'],
 [745, '19D', 'G'],
 [745, '19F', 'G'],
 [745, '20G', 'NA'],
 [745, '20K', 'NA'],
 [800, '1A', 'NA'],
 [800, '1B', 'NA'],
 [800, '2B', 'O'],
 [800, '2D', 'G'],
 [800, '3B', 'G'],
 [800, '3E', 'G'],
 [800, '4A', 'NA'],
 [800, '4C', 'NA'],
 [800, '5D', 'G'],
 [800, '5M', 'G'],
 [800, '6C', 'O'],
 [800, '6F', 'G'],
 [800, '7F', 'O'],
 [800, '7G', 'O'],
 [800, '8G', 'G'],
 [800, '8H', 'G'],
 [800, '9H', 'G'],
 [800, '9I', 'O'],
 [800, '10I', 'G'],
 [800, '10J', 'G'],
 [800, '11I', 'G'],
 [800, '11K', 'O'],
 [800, '12J', 'R'],
 [800, '12L', 'NA'],
 [800, '13D', 'O'],
 [800, '13K', 'G'],
 [800, '14K', 'G'],
 [800, '14L', 'NA'],
 [800, '15L', 'R'],
 [800, '15M', 'G'],
 [800, '16M', 'R'],
 [800, '16N', 'G'],
 [800, '17E', 'G'],
 [800, '17N', 'G'],
 [800, '18N', 'R'],
 [800, '18O', 'G'],
 [800, '19D', 'G'],
 [800, '19F', 'G'],
 [800, '20G', 'G'],
 [800, '20K', 'NA'],
 [815, '1A', 'NA'],
 [815, '1B', 'NA'],
 [815, '2B', 'O'],
 [815, '2D', 'G'],
 [815, '3B', 'G'],
 [815, '3E', 'O'],
 [815, '4A', 'NA'],
 [815, '4C', 'NA'],
 [815, '5D', 'G'],
 [815, '5M', 'G'],
 [815, '6C', 'O'],
 [815, '6F', 'G'],
 [815, '7F', 'G'],
 [815, '7G', 'O'],
 [815, '8G', 'G'],
 [815, '8H', 'G'],
 [815, '9H', 'G'],
 [815, '9I', 'O'],
 [815, '10I', 'G'],
 [815, '10J', 'G'],
 [815, '11I', 'G'],
 [815, '11K', 'O'],
 [815, '12J', 'R'],
 [815, '12L', 'NA'],
 [815, '13D', 'O'],
 [815, '13K', 'G'],
 [815, '14K', 'G'],
 [815, '14L', 'NA'],
 [815, '15L', 'R'],
 [815, '15M', 'G'],
 [815, '16M', 'R'],
 [815, '16N', 'G'],
 [815, '17E', 'G'],
 [815, '17N', 'G'],
 [815, '18N', 'R'],
 [815, '18O', 'G'],
 [815, '19D', 'G'],
 [815, '19F', 'G'],
 [815, '20G', 'G'],
 [815, '20K', 'NA'],
 [830, '1A', 'NA'],
 [830, '1B', 'NA'],
 [830, '2B', 'O'],
 [830, '2D', 'G'],
 [830, '3B', 'G'],
 [830, '3E', 'O'],
 [830, '4A', 'O'],
 [830, '4C', 'NA'],
 [830, '5D', 'G'],
 [830, '5M', 'G'],
 [830, '6C', 'R'],
 [830, '6F', 'G'],
 [830, '7F', 'O'],
 [830, '7G', 'G'],
 [830, '8G', 'G'],
 [830, '8H', 'G'],
 [830, '9H', 'O'],
 [830, '9I', 'G'],
 [830, '10I', 'O'],
 [830, '10J', 'G'],
 [830, '11I', 'G'],
 [830, '11K', 'O'],
 [830, '12J', 'O'],
 [830, '12L', 'G'],
 [830, '13D', 'O'],
 [830, '13K', 'G'],
 [830, '14K', 'G'],
 [830, '14L', 'NA'],
 [830, '15L', 'G'],
 [830, '15M', 'G'],
 [830, '16M', 'G'],
 [830, '16N', 'G'],
 [830, '17E', 'NA'],
 [830, '17N', 'G'],
 [830, '18N', 'O'],
 [830, '18O', 'G'],
 [830, '19D', 'G'],
 [830, '19F', 'G'],
 [830, '20G', 'G'],
 [830, '20K', 'NA'],
 [845, '1A', 'NA'],
 [845, '1B', 'NA'],
 [845, '2B', 'R'],
 [845, '2D', 'G'],
 [845, '3B', 'G'],
 [845, '3E', 'R'],
 [845, '4A', 'O'],
 [845, '4C', 'NA'],
 [845, '5D', 'G'],
 [845, '5M', 'G'],
 [845, '6C', 'R'],
 [845, '6F', 'G'],
 [845, '7F', 'G'],
 [845, '7G', 'G'],
 [845, '8G', 'G'],
 [845, '8H', 'G'],
 [845, '9H', 'O'],
 [845, '9I', 'G'],
 [845, '10I', 'OG'],
 [845, '10J', 'G'],
 [845, '11I', 'G'],
 [845, '11K', 'O'],
 [845, '12J', 'O'],
 [845, '12L', 'G'],
 [845, '13D', 'O'],
 [845, '13K', 'G'],
 [845, '14K', 'G'],
 [845, '14L', 'NA'],
 [845, '15L', 'G'],
 [845, '15M', 'G'],
 [845, '16M', 'G'],
 [845, '16N', 'G'],
 [845, '17E', 'NA'],
 [845, '17N', 'G'],
 [845, '18N', 'O'],
 [845, '18O', 'G'],
 [845, '19D', 'G'],
 [845, '19F', 'G'],
 [845, '20G', 'G'],
 [845, '20K', 'NA'],
 [900, '1A', 'NA'],
 [900, '1B', 'NA'],
 [900, '2B', 'O'],
 [900, '2D', 'G'],
 [900, '3B', 'O'],
 [900, '3E', 'G'],
 [900, '4A', ''],
 [900, '4C', 'NA'],
 [900, '5D', 'G'],
 [900, '5M', 'G'],
 [900, '6C', 'O'],
 [900, '6F', 'G'],
 [900, '7F', 'O'],
 [900, '7G', 'G'],
 [900, '8G', 'G'],
 [900, '8H', 'G'],
 [900, '9H', 'O'],
 [900, '9I', 'G'],
 [900, '10I', 'O'],
 [900, '10J', 'G'],
 [900, '11I', 'O'],
 [900, '11K', 'O'],
 [900, '12J', 'O'],
 [900, '12L', 'G'],
 [900, '13D', 'O'],
 [900, '13K', 'G'],
 [900, '14K', 'O'],
 [900, '14L', 'NA'],
 [900, '15L', 'G'],
 [900, '15M', 'G'],
 [900, '16M', 'G'],
 [900, '16N', 'G'],
 [900, '17E', 'NA'],
 [900, '17N', 'G'],
 [900, '18N', 'O'],
 [900, '18O', 'G'],
 [900, '19D', 'G'],
 [900, '19F', 'G'],
 [900, '20G', 'O'],
 [900, '20K', 'NA'],
 [915, '1A', 'NA'],
 [915, '1B', 'NA'],
 [915, '2B', 'O'],
 [915, '2D', 'G'],
 [915, '3B', 'O'],
 [915, '3E', 'G'],
 [915, '4A', 'O'],
 [915, '4C', 'NA'],
 [915, '5D', 'G'],
 [915, '5M', 'G'],
 [915, '6C', 'O'],
 [915, '6F', 'G'],
 [915, '7F', 'O'],
 [915, '7G', 'G'],
 [915, '8G', 'G'],
 [915, '8H', 'G'],
 [915, '9H', 'O'],
 [915, '9I', 'G'],
 [915, '10I', 'O'],
 [915, '10J', 'G'],
 [915, '11I', 'O'],
 [915, '11K', 'G'],
 [915, '12J', 'O'],
 [915, '12L', 'G'],
 [915, '13D', 'G'],
 [915, '13K', 'O'],
 [915, '14K', 'O'],
 [915, '14L', 'NA'],
 [915, '15L', 'G'],
 [915, '15M', 'G'],
 [915, '16M', 'G'],
 [915, '16N', 'G'],
 [915, '17E', 'NA'],
 [915, '17N', 'G'],
 [915, '18N', 'G'],
 [915, '18O', 'G'],
 [915, '19D', 'G'],
 [915, '19F', 'G'],
 [915, '20G', 'O'],
 [915, '20K', 'NA'],
 [930, '1A', 'NA'],
 [930, '1B', 'NA'],
 [930, '2B', 'O'],
 [930, '2D', 'G'],
 [930, '3B', 'O'],
 [930, '3E', 'O'],
 [930, '4A', 'O'],
 [930, '4C', 'NA'],
 [930, '5D', 'G'],
 [930, '5M', 'G'],
 [930, '6C', 'O'],
 [930, '6F', 'G'],
 [930, '7F', 'O'],
 [930, '7G', 'O'],
 [930, '8G', 'G'],
 [930, '8H', 'G'],
 [930, '9H', 'O'],
 [930, '9I', 'G'],
 [930, '10I', 'O'],
 [930, '10J', 'G'],
 [930, '11I', 'G'],
 [930, '11K', 'O'],
 [930, '12J', 'O'],
 [930, '12L', 'G'],
 [930, '13D', 'O'],
 [930, '13K', 'G'],
 [930, '14K', 'O'],
 [930, '14L', 'NA'],
 [930, '15L', 'O'],
 [930, '15M', 'G'],
 [930, '16M', 'G'],
 [930, '16N', 'O'],
 [930, '17E', 'O'],
 [930, '17N', 'O'],
 [930, '18N', 'G'],
 [930, '18O', 'G'],
 [930, '19D', 'G'],
 [930, '19F', 'G'],
 [930, '20G', 'O'],
 [930, '20K', 'NA'],
 [945, '1A', 'NA'],
 [945, '1B', 'NA'],
 [945, '2B', 'O'],
 [945, '2D', 'G'],
 [945, '3B', 'O'],
 [945, '3E', 'O'],
 [945, '4A', 'O'],
 [945, '4C', 'NA'],
 [945, '5D', 'G'],
 [945, '5M', 'G'],
 [945, '6C', 'O'],
 [945, '6F', 'G'],
 [945, '7F', 'O'],
 [945, '7G', 'O'],
 [945, '8G', 'G'],
 [945, '8H', 'O'],
 [945, '9H', 'O'],
 [945, '9I', 'G'],
 [945, '10I', 'O'],
 [945, '10J', 'G'],
 [945, '11I', 'G'],
 [945, '11K', 'O'],
 [945, '12J', 'O'],
 [945, '12L', 'G'],
 [945, '13D', 'O'],
 [945, '13K', 'G'],
 [945, '14K', 'O'],
 [945, '14L', 'NA'],
 [945, '15L', 'O'],
 [945, '15M', 'G'],
 [945, '16M', 'G'],
 [945, '16N', 'O'],
 [945, '17E', 'O'],
 [945, '17N', 'O'],
 [945, '18N', 'G'],
 [945, '18O', 'G'],
 [945, '19D', 'G'],
 [945, '19F', 'G'],
 [945, '20G', 'O'],
 [945, '20K', 'NA'],
 [1000, '1A', 'NA'],
 [1000, '1B', 'NA'],
 [1000, '2B', 'O'],
 [1000, '2D', 'G'],
 [1000, '3B', 'G'],
 [1000, '3E', 'O'],
 [1000, '4A', 'O'],
 [1000, '4C', 'NA'],
 [1000, '5D', 'G'],
 [1000, '5M', 'G'],
 [1000, '6C', 'O'],
 [1000, '6F', 'G'],
 [1000, '7F', 'O'],
 [1000, '7G', 'O'],
 [1000, '8G', 'G'],
 [1000, '8H', 'G'],
 [1000, '9H', 'G'],
 [1000, '9I', 'G'],
 [1000, '10I', 'G'],
 [1000, '10J', 'G'],
 [1000, '11I', 'G'],
 [1000, '11K', 'O'],
 [1000, '12J', 'O'],
 [1000, '12L', 'G'],
 [1000, '13D', 'O'],
 [1000, '13K', 'G'],
 [1000, '14K', 'O'],
 [1000, '14L', 'NA'],
 [1000, '15L', 'O'],
 [1000, '15M', 'G'],
 [1000, '16M', 'G'],
 [1000, '16N', 'O'],
 [1000, '17E', 'O'],
 [1000, '17N', 'O'],
 [1000, '18N', 'G'],
 [1000, '18O', 'G'],
 [1000, '19D', 'G'],
 [1000, '19F', 'G'],
 [1000, '20G', 'O'],
 [1000, '20K', 'NA']]


# In[21]:


name = input("Enter your name: ")
print("Hello", name + "!")

