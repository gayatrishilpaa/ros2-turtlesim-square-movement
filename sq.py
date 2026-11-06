#importing 
import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose 
import math
import time

class Square(Node):
    def __init__(self):
        super().__init__("turtle_square")

        #declaring publishers and subscribers 
        self.publisher_=self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_=self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer=self.create_timer(0.5,self.timer_callback)
        self.count_=0

        #initialising the very initial positions of the turtle before any movement 
        self.x0 = None
        self.y0 = None
        self.theta_start= None

    def pose_callback(self, pose):
        self.pose=pose

        #this is standard. no one can change x0 and y0 posn. all dist should and will be calculated wrt these corrdinates
        if self.x0 is None:
            self.x0 = pose.x
            self.y0 = pose.y

    def timer_callback(self):

            msg = Twist()

            if self.theta_start is None:
                self.theta_start=self.pose.theta

            x = self.pose.x
            y = self.pose.y

            dist = math.sqrt((x - self.x0)**2 + (y - self.y0)**2)

            if dist < 2.0:

                # MOVE STRAIGHT
                msg.linear.x = 2.0
                msg.angular.z = 0.0

            else:
                angle_turned = self.pose.theta - self.theta_start
                # We have reached 2 m
                msg.linear.x = 0.0
                if abs(angle_turned) < math.pi / 2:
                    # Keep rotating
                    msg.angular.z = 1.0
                else:
                    msg.angular.z = 0.0

            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    sq=Square()
    rclpy.spin(sq)
    sq.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
    