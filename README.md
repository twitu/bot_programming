## Path finding is a metaphor
This repository documents our, that's [twitu](https://github.com/twitu), [arkonaire](https://github.com/arkonaire) and [lsampras](https://github.com/lsampras), experiments with bot programming, from the mundane path finding to the abstract state management.

To setup the environment, clone the repository and then run the following commands
```bash
cd path/to/bot_programming
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install python3-tk
```

## Cool results
Finding bottlenecks in a randomly generated map  
![bottlenecks](../assets/bottlenecks.jpg?raw=true)

A* path finding with way points  
![waypoints](../assets/waypoints.png?raw=true)

Dynamic squad movement based on obstacles  
![swarm](../assets/swarm.gif?raw=true)

Enemy pheromones based on last known position  
![pheromones](../assets/pheromones.gif?raw=true)

## Reference material
We refer to a lot of existing work including blogs, videos, research papers and books. A good reference ideally opens up a new avenue for experimenting.

### General Principles
[AI Game Programming Wisdom](https://drive.google.com/open?id=1zQ0Cm7DoT7rmo8Y9w4P0LAWYKY9HXZq9) - Touches on all concepts related to AI game programming, while also covering code opitmizations for practical performance.

### Map intelligence
[Voronoi based choke points](https://drive.google.com/open?id=1Tf41Yi77pA7Neay5EWu_PJChCow1l0Gw) - Identifying choke points in the map.  
[Flood fill to identify choke points](https://drive.google.com/open?id=1Gt7yd1y8lKUhlhV54y9M6b5ApfZSC6Pt) - Explains efficient technique to identify choke points in common maps.  

### Path finding and map representations
[Amit P blog](http://theory.stanford.edu/~amitp/GameProgramming/) - Extensive resource on path finding algorithms and implementations.  
[JPS and RSR optimization](https://harablog.wordpress.com/2011/08/26/fast-pathfinding-via-symmetry-breaking/) - Discussion on optimization techniques  
[Potential field based navigation](https://drive.google.com/open?id=1lW9zldi-tU46gca_OQ2OBeeFpWjJh0VB) - Discussion around techniques for potential field based navigation  
[Adaptive potential fields](https://drive.google.com/open?id=1I5ZZJJPl0h8WRBpAk9--KQUMNkdMPlbN) - Suggests potential fields that can be used for navigation  

### Squad tactics and formations
[Dynamic formations](https://drive.google.com/open?id=1aSlsK2X3IXli16IOhduAAX-XkciGpLYP) - Gives a generic framework to build squad formations.  
[Real world squads](https://youtu.be/-rKRt5zVZgw) - Inspiration from historical squad formations.  
[Formation controls](https://www.mdpi.com/2218-6581/7/4/67/htm) Review paper for formation control.  

### Enemy intelligence and prediction
[Pheromones for tracking and prediction](https://drive.google.com/open?id=1ykFoo6yHyXDLIp0Uf3Quu2GSBWiZJ31r) - Concept for using pheromones to track enemy units

### Decision making
[Game trees](https://drive.google.com/open?id=1ZEjRgJ6d2dAKhxyUgO6T58KRATf_4zNy) - Trees for decision making.  
[Resource management](https://drive.google.com/open?id=159NNyEcaQbe9by84EiogYNMinCOJuhPW) - Framework for managing resources.  

### Tools
[Map Generation](http://devmag.org.za/2009/04/25/perlin-noise/) - Using perlin noise for random maps
