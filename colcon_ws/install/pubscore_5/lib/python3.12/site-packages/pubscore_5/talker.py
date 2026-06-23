import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, '/demo_topic', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        elapsed_time = int(time.time() - self.start_time)
        msg = String()
        msg.data = f"Hello World: {elapsed_time} seconds"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main():
    rclpy.init()
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
