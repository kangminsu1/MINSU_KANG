#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('srv_client')
        self.cli = self.create_client(AddTwoInts, '/add_two_ints')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
            
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a.num = int(a)
        self.req.b.num = int(b)
        
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()
    client = AddTwoIntsClient()

    if len(sys.argv) != 3:
        client.get_logger().info('Usage: ros2 run srvmsg add_ints_client.py <a> <b>')
        client.get_logger().info('Defaulting to 1 and 2')
        a, b = 1, 2
    else:
        a, b = sys.argv[1], sys.argv[2]

    response = client.send_request(a, b)
    client.get_logger().info(f'LCM: {response.sum.num}')
    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
