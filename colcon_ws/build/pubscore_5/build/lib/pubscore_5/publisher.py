import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DirectionPublisher(Node):
    def __init__(self):
        super().__init__('get_dir')
        self.pub = self.create_publisher(String, '/direction', 10)
        self.timer = self.create_timer(0.1, self.publish_random_direction)
        self.directions = ['w', 's', 'a', 'd']

    def publish_random_direction(self):
        direction = random.choice(self.directions)
        msg = String()
        msg.data = direction
        self.pub.publish(msg)
        self.get_logger().info(f'Published direction: {direction}')

    def run(self):
        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)
    direction_publisher = DirectionPublisher()
    direction_publisher.run()
    direction_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()