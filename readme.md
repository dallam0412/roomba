# Roomba
## A roomba robot which avoids ostacle with the help of a laser 
# Author
## Dhanush Babu Allam (119390320)

# running

create a ros2_ws then create a src folder with it and clone the following link

```
https://github.com/dallam0412/roomba.git
```

now clone the dolly package using

```
https://github.com/chapulina/dolly.git
```
and add gazebo_ros_pkgs which is dependency

now source ros2 galactic using

```
source /opt/ros/galactic/setup.bash
```

now build using in the ros2_ws: -

```
colcon build
```
now source the packages

```
. install/setup.bash
```

to run the simulation first run

```
ros2 launch roomba obstacle_avoidance.launch.py
```
the to open in gazebo run 

```
. /usr/share/gazebo/setup.sh
ros2 launch roomba dolly.launch.py
```
now place an obstacle in front of the roomba and we can see it avoid

# dependencies
* dolly package
* ros2 galactic
* gazebo_ros_pkgs

