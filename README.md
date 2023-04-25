### CMSE 202 Semester Project: Modelling Moss Growth
#### Ben Laubach, Sanskriti Verma, Ella Kovach, Tori Fallon, Jason Williams, Carrie Nielsen
#### CMSE 202, Spring 2023
#### Michigan State University
============

**Title**: Modelling Moss Growth

**Description**: This project simulates the growth and spread of moss and weeds in a two-dimensional environment. The simulation is based on a grid, where each cell in the grid can be either empty, occupied by a moss agent, occupied by a weed agent, occupied by a tree, or occupied by a dead moss or weed agent.

*place_trees*: places trees randomly in the environment based on the values assigned to `n_trees` and `tree_radius`.

*get_neighborhood*: returns a list of cells around an agent's position, up to a certain radius.

*plot_environment*: creates a plot of the environment and its agents.

*simulate*: It updates the environment array and the list of agents based on the new agents and dead agents. It then calls `plot_environment` to display the updated environment. The simulation runs for a fixed number of time steps, during which agents move, age, and replicate. Agents have a limited lifespan, after which they die.

The `Moss_Agent` and `Weed_Agent` classes inherit from the `Environment` class. They represent agents in the simulation that are placed in the environment array. `Moss_Agent` and `Weed_Agent` are identical except for their replicate method.

Moss and weed agents can move to an adjacent empty cell, and can replicate to an adjacent cell occupied by a plant of their same species or an empty cell. The probability of replication is controlled by a growth rate parameter, which is higher for weeds than for moss.


**Running the code**: In the main section of the code, adjust the parameters of the simulation as desired (Preset parameters can also be retained). For example, you can change the size of the environment or the number of trees. When you run the simulation, a window will appear showing the environment. You can also adjust the timestep depending on how long you want the simulation to run.
You can adjust the parameters of the simulation by changing the values in the `Moss_Agent` and `Weed_Agent` classes. For example, change the maximum age of the agents, the growth rate, and the shape of the agents.
The size of the environment and the number of trees can be adjusted by changing the parameters in the `Environment` class.

**Note**: If you wish to make changes to the initial configuration of the environment, you can modify the `create_environment` function located in the Environment class. This function takes in two arguments: `n_trees` and `tree_radius`. `n_trees` determines the number of trees that will be randomly placed in the environment, and `tree_radius` determines the radius of the trees.


Contents
===========
This repository contains the following:
1. `README_CMSE.md`: This document. 
2. `Project_Script.ipynb`: Main notebook where all the code is being run
3. `CMSE_202_Moss`: PowerPoint Presentation that highlights the motivation, results, future scope etc.
4. `To_Dos`: List of tasks group members need to do to address bugs in the code, make changes to it, and add parameters.
5. `Writeup`: In-depth project description 


Report/closeout
---------------
Everything that needs to be run is in `Project_Script.ipynb`.
