# ROS 2 Turtlesim – Square Movement

A basic ROS 2 project demonstrating autonomous turtle movement using position and orientation feedback in the Turtlesim simulator.

The project consists of a **Turtle Square Node** that publishes velocity commands and subscribes to the turtle's pose to control its forward movement and rotation.

**ROS 2 Version:** Humble

---

## Concepts Used

* Python
* `rclpy`
* `geometry_msgs/Twist`
* `turtlesim/Pose`
* Publishers
* Subscribers
* Topics
* Timers
* Euclidean Distance
* Angular Displacement

---

## Features

* The node publishes velocity commands to `/turtle1/cmd_vel`.
* Subscribes to `/turtle1/pose` to obtain the turtle's position and orientation.
* Stores the initial coordinates as a reference point.
* Calculates the distance travelled using Euclidean distance.
* Moves the turtle forward with a linear velocity of `2.0`.
* Stops forward movement after travelling approximately 2 units.
* Rotates the turtle until it reaches approximately 90 degrees of angular displacement.
* Uses a timer callback to continuously update and publish velocity commands.

---

## System Design

| Turtle Square Node | Topic | Turtlesim |
|---|---|---|
| Creates a Publisher | `/turtle1/cmd_vel` | Receives velocity commands |
| Creates a Subscription | `/turtle1/pose` | Publishes pose information |
| `timer_callback()` | → | Controls turtle movement |
| `pose_callback()` | ← | Updates position data |

---

## How to Run

1. Build the workspace.

```bash
colcon build
```

2. Source the workspace.

```bash
source install/setup.bash
```

3. Start the Turtlesim simulator.

```bash
ros2 run turtlesim turtlesim_node
```

4. Open a new terminal, source the workspace again, and run the node.

```bash
source install/setup.bash
ros2 run <package_name> <executable_name>
```

---

## Notes

* Ensure `package.xml` and `setup.py` are updated with the correct package and executable names before building the workspace.
* The current implementation performs one forward movement and one approximately 90-degree rotation. Repetition for all four sides is a future improvement.
