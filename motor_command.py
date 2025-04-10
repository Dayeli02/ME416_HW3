#!/usr/bin/env python3
"""
Simple demo that listens to std_msgs/Strings published
to the 'chatter' topic
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MotorCommand(Node):
    """
    A Node class to listen to the 'cmd_vel' topic and process velocity commands.
    """
    def __init__(self):
        super().__init__('motor_command')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )

    def cmd_vel_callback(self, msg):
        """
        Callback to process incoming Twist messages.
        """
        speed_linear = msg.linear.x
        speed_angular = msg.angular.z

        # Log the extracted velocities
        self.get_logger().info(f'Speed Linear: {speed_linear}, Speed Angular: {speed_angular}')


def main(args=None):
    """
    Initialize ROS, start the node, spin, and clean up resources.
    """
    rclpy.init(args=args)
    motor_command_node = MotorCommand()
    rclpy.spin(motor_command_node)

    motor_command_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
