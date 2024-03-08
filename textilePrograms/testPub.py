import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Import the String message type

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(String, 'my_robot_topic', 10)

    def publish_message(self, message):
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    while rclpy.ok():
        message = input("Enter a new string to publish (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        node.publish_message(message)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()