# ROS 2 Turtlesim – Square Movement

## Overview
This project implements a simple autonomous movement system using ROS 2 and the Turtlesim simulator. A turtle is programmed to move forward and rotate, following a square-like path using its position and orientation data.

The project demonstrates the use of ROS 2 publishers, subscribers, timers, and velocity commands.

## Technologies Used
- ROS 2 (Humble)
- Python
- Turtlesim
- `rclpy`
- `geometry_msgs`
- `turtlesim`

## How It Works

The program uses a ROS 2 node named `turtle_square` to control the movement of the turtle.

1. **Publisher:** Publishes velocity commands to `/turtle1/cmd_vel` using the `Twist` message type.
2. **Subscriber:** Subscribes to `/turtle1/pose` to receive the turtle's current position (`x`, `y`) and orientation (`theta`).
3. **Initial Position:** Stores the turtle's starting coordinates to calculate the distance travelled.
4. **Forward Movement:** The turtle moves forward with a linear velocity of `2.0` until it has travelled a distance of approximately 2 units.
5. **Rotation:** Once the target distance is reached, the turtle stops moving forward and rotates until it has turned approximately 90 degrees.
6. **Timer Callback:** A timer periodically checks the turtle's position and orientation and publishes the appropriate velocity commands.

## ROS 2 Concepts Implemented
- Creating a custom ROS 2 node using `rclpy`
- Publishing velocity commands using `Twist`
- Subscribing to position data using `Pose`
- Using callbacks to process incoming messages
- Implementing timer-based control
- Calculating distance using Euclidean distance
- Using angular displacement to control rotation

## How to Run

### 1. Source ROS 2
```bash
source /opt/ros/humble/setup.bash
```

### 2. Start Turtlesim
Open a terminal and run:
```bash
ros2 run turtlesim turtlesim_node
```

### 3. Run the Python Script
Open another terminal, navigate to the directory containing the script, and run:
```bash
python3 square.py
```

## Learning Outcomes
Through this project, I gained practical experience with ROS 2 communication mechanisms, node creation, message handling, and basic robot movement control using position and orientation feedback.

## Future Improvements
- Implement four complete sides with controlled 90-degree turns.
- Improve angle handling to account for orientation wraparound.
- Introduce more precise movement control using tolerances.
- Implement a state-based movement sequence for smoother square trajectories.
