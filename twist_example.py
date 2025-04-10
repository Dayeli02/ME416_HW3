""" Example of how to set attributes in ROS messages """
from geometry_msgs.msg import Twist


def twist_fill():
    '''
    Fill a twist message with non-zero values
    '''
    # This is a stub. Substitute with your own code
    msg = Twist()
    # Populate linear velocities (Vector3)
    msg.linear.x = 1.0
    msg.linear.y = 2.0
    msg.linear.z = 3.0
    # Populate angular velocities (Vector3)
    msg.angular.x = 0.5
    msg.angular.y = 1.5
    msg.angular.z = 2.5
    return msg
