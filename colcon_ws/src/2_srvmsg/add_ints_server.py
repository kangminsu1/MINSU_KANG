#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts


def compute_lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return math.lcm(a, b)


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('srv_server')

        self.srv = self.create_service(AddTwoInts, '/add_two_ints', self.srv_callback)
        self.get_logger().info('Srv Server Ready.')

    def srv_callback(self, request, response):
        response.sum.num = compute_lcm(request.a.num, request.b.num)
        
        self.get_logger().info(f'Incoming request\na: {request.a.num}, b: {request.b.num}')
        self.get_logger().info(f'Sending back response: [{response.sum.num}]')
        
        return response


def main():
    rclpy.init()
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
