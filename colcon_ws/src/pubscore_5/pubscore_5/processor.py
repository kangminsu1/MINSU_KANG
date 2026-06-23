import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16MultiArray
from matplotlib import pyplot as plt
from collections import deque

# X, Y  
current_position = [0.0, 0.0]
list_pos = deque(maxlen=20)

class DirectionProcessor(Node):
    def __init__(self):
        super().__init__('set_dir')
        self.sub = self.create_subscription(String, '/direction', self.direction_callback, 10)
        self.sub  # prevent unused variable warning

    def direction_callback(self, msg):
        direction = msg.data
        # self.get_logger().info(f'Received direction: {direction}')

        if direction == 'w':
            current_position[1] += 1.0
        elif direction == 's':
            current_position[1] -= 1.0
        elif direction == 'a':
            current_position[0] -= 1.0
        elif direction == 'd':
            current_position[0] += 1.0
        else:
            self.get_logger().warn(f'Invalid direction: {direction}')
            return

        self.get_logger().info(f'Updated position: X={current_position[0]}, Y={current_position[1]}')
        list_pos.append(tuple(current_position))

        if len(list_pos) > 10:
            list_pos.popleft()

        plot_position(current_position)

def plot_position(position):
    plt.clf()

    for pos in list_pos:
        plt.plot(pos[0], pos[1], 'bo')
    plt.xlim(position[0] - 10, position[0] + 10)
    plt.ylim(position[1] - 10, position[1] + 10)
    plt.grid(False)
    plt.pause(0.01)

def main(args=None):
    rclpy.init(args=args)
    direction_processor = DirectionProcessor()
    rclpy.spin(direction_processor)
    direction_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()