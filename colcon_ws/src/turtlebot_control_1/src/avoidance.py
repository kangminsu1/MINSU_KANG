#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, TwistStamped

class AvoidanceNode(Node):
    def __init__(self):
        super().__init__('avoidance_node')
        self.get_logger().info('Avoidance Node has been started.')

        self.min_distance = 0.5
        self.scan_subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.cmd_publisher = self.create_publisher(TwistStamped, '/cmd_vel', 10)

        # self.linear_vel_subscription = self.create_subscription(
        #     TwistStamped,
        #     '/cmd_vel',
        #     self.linear_vel_callback,
        #     10)
        
    def scan_callback(self, msg: LaserScan):
        twist = TwistStamped()
        # print(msg.ranges)  # Debug: Print the ranges to see the data structure
        print(f"First range value: {msg.ranges[0]}")  # Debug: Print the first range value
        # print(f"Linear x value: {twist.twist.linear.x}")  # Debug: Print the linear x value of ce twist message
        if msg.ranges and msg.ranges[0] is not None and msg.ranges[0] < self.min_distance:
            self.get_logger().info('Obstacle detected! Stopping.')
            twist.twist.angular.z = 0.0
            twist.twist.linear.x = 0.0
        else:
            twist.twist.linear.x = 0.0
            twist.twist.angular.z = 0.1

        self.cmd_publisher.publish(twist)

    # def linear_vel_callback(self, msg: TwistStamped):
    #     self.get_logger().info(f"Received linear velocity command: {msg.twist.linear.x}")
        # Here you can add logic to handle the received linear velocity command if needed

def main():
    rclpy.init()
    node = AvoidanceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
