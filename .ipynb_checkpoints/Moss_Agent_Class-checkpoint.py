import random 
import numpy as np
import math
import matplotlib.pyplot as plt
import itertools

# +
class Moss_Agent():

    '''
    A Moss_Agent class. 
    '''
    # Changed default age limit to random integer between 8 and 10
    def __init__(self,xmax=100,ymax=100,sex="M",shape="o",color="y"):
        '''
        Initaliazes an animal agent object, an autonomous agent that can interact with other agents. Specifically, predators can hunt prey,
        prey can procreate, and both predator and prey can move around and age. 

        xmax (int): The (x) size of the habitat
        ymax (int): The (y) size of the habitat
        age_limit (int): Sets the age at which the animal dies of old age
        shape (string): Specifies the marker to use when visualizing the animal
        color (string): Specifies the color to use when visualizing the animal
        '''
        self.x = random.randint(0, xmax)
        self.y = random.randint(0, ymax)
        self.age = 0 
        self.age_limit = random.randint(8,10)
        self.xmax = xmax
        self.ymax = ymax
        self.last_litter_time = 1
        self.color = color
        self.shape = shape
        
    def draw(self,ax):
        '''
        Method to draw the animal agent using an axis object ax.
        '''
        ax.scatter(self.x, self.y, s=24.0, c=self.color, marker=self.shape)   
    
    def aging(self):
        '''
        Method to increase the age of the animal agent by one.
        '''
        self.age += 1

    def check_if_dead(self):
        '''
        Method to check whether the animal agent has died of old age.
        '''
        if self.age > self.age_limit:
            return True
        else:
            return False
    
#     def onBoard(self,environment):
#         if (self.x <= environment.shape[0]-1 and self.x >= 0
#             and self.y <= environment.shape[1]-1 and self.y >=0):
#             return True
#         else:
#             return False
        
    
#     def get_neighbors(self):
#         neighborhood = [(self.x-1,self.y),
#                         (self.x,self.y-1),
#                         (self.x+1,self.y),
#                         (self.x,self.y+1)]
#         neighborhood_values = []
#         for neighbor in neighborhood:
#             if onBoard(neighbor[0],neighbor[1],environment):
#                 neighbor_values.append(pass)
#             return neighbor_values
            
    
    
#     def procreate(self,all_agents,time):
#         '''
#         Method to create new agents (procreate). There are three barriers to procreation:
#         1. Has it been enough time between the last procreation? (I.e., more than the gestation time.)
#         2. Is there a (male) agent within range?
#         3. Is the population below the saturation point? This is modeled as a logistic function.
#         If all of these conditions are met, then a new litter is created. Every member of the new litter is 
#         randomly assigned genes from their parents. The last litter time is set to the current time and the
#         list of children is returned. 

#         all_agents (list): A list of all of the animal agent objects 
#         time (int): The current time, used to determine if the Animal Agent has passed the gestation period.
#         '''
        
#         child_list = []
#         val = random.random()
#         if (self.sex == 'F') and (np.mod(abs(int(time)-int(self.last_litter_time)),self.gestation) == 0):
#             for agent in all_agents:
#                 if (agent.ptype=="Prey") and (agent.sex == "M") and (self.get_distance(agent) <= self.mate_range) and (val > (1.0/(1.0+np.exp(-len(all_agents)/self.saturation_pop)))):
#                     child_num = int(np.random.normal(7,1))
#                     for jj in range(child_num):
#                         mom_a = self.alle_d
#                         if np.random.randint(0,2) == 1:
#                             mom_a = self.alle_m
#                         dad_a = agent.alle_d
#                         if np.random.randint(0,2) == 1:
#                             dad_a = agent.alle_m               
#                         child = Animal_Agent(sex="F")
#                         if np.random.randint(0,2) == 1:
#                             child = Animal_Agent(sex="M")
#                         child.set_allele(dad_a,mom_a)
#                         child_list.append(child)
#                     self.last_litter_time = time
#                     break

#         return child_list
# -


