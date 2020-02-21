# PathFinder Game
**Reinforcement Learning Maze Runner**

Hello Reader! I want this project to serve as a platform for simulation-based reinforcement learning. In other words, this repository should be a platform for studying how actors can learn to overcome challenges without explicit instructions. 

___

_How does this project approach complex learning?_

An actor that can optimize its own "path" from Point A to Point B is undoubtedly useful. Machines that can take sensor input and develop idealized solutions to problems will find themselves replacing human actors in many career fields. Until recently, machine-based automation was limited to simple, repetitive tasks; programming involved series of "if-then" conditions. As our computing resources advance, we are refining mathematics with the understanding that we can realize significantly more complex methods of automation.

Such mathematics emphasize the importance of dynamic input from complex environments.  

This project will host lightweight simulation environments so that a user can experiment with reinforcement learning (RL) schemas under minimal load. 

<br />

_What happens after the framework is established?_

After the PathFinder framework is viable, I will develop various simulations to experiment with various RL schemas. As experiments continue, I will update the PathFinder repository to accommodate increasingly complex simulations that better replicate real-world stimulus.

<br />

_Overall, what can I expect to find in this repository?_

- PathFinder schema
  - Emphasizes actors finding their way through two-dimensional environments given a variety of stimulus and challenges
- PathFinder-based experiments
  - [Single-actor maze games](https://github.com/evangibson/pathfinder_game/tree/master/games/random_maze_single_actor.py)
  - Multi-actor communication challenges
  - Adversarial "capture-the-flag" games
- PathFinder GUI (optional)
  - For visualizing/playing games using the same parameters as a machine-actor

___
### Project Status

The [first maze game]((https://github.com/evangibson/pathfinder_game/tree/master/games/random_maze_single_actor.py)) is simple. An actor starts in a random position after he/she determines the initial maze parameters (length of maze, height of maze, proportion of walls to "empty spaces", and the maximum number of turns before game over): 

```
Enter a positive, whole number for the length of the maze: 4
Enter a positive, whole number for the height of the maze: 4
Enter a number between 0 and 1 for the proportion of walls to blank spaces: .1
Max Number of Turns: 10
```
The length, height, and maximum number of turns should be entered as positive, whole numbers. The proportion should be a number between 0 and 1.  

After these prompts are filled, the user is given a view of the maze's state space:
```
Current Turn:  0
Distance to Target:  1.4142135623730951
Penalty Score:  0
Score:  -1.4142135623730951
[[  0   0   0   0]
 [  0  -2   0   0]
 [101   0   0  -1]
 [  0   0   0   0]]
Move Direction:
```
Legend (using defaults):
- 0: Empty Space
- -1: Wall
- -2: Goal
- 101: Player position

___

### Goals

- ~~Create maze environment~~
- ~~Create players~~
- Create self training schema (without visualization)
- Create GUI for human play

___

### Inspiration
- [OpenAI](https://www.youtube.com/watch?v=kopoLzvh5jY)