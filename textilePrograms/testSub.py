import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Import the String message type
from pick_goal import move_to_pose
from place_cotton import move_to_place_cotton
from place_mix import move_to_place_mix
from place_wool import move_to_place_wool
import threading  # Import the threading module


class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            String,  # Specify the message type
            'my_topic',  # Specify the topic
            self.listener_callback,  # Specify the callback
            10)  # Specify the queue size

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)  # Log the received message
        if msg.data == 'Hello, world! 10':
            try:
                # Start a new thread to run the move_to_place_cotton function
                threading.Thread(target=self.run_tasks).start()
            except Exception as e:
                print(f"An error occurred: {e}")

    def run_tasks(self):
        # move_to_pose(-0.55, False)
        # move_to_place_cotton(False)
        move_to_place_mix(False)
        # move_to_place_wool(False)
        print("Program finished")


def main(args=None):
    rclpy.init(args=args)  # Initialize the default context
    try:
        node = MySubscriber()
        rclpy.spin(node)  # Spin the node so it can process callbacks
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if rclpy.ok():  # Check if the context is still valid
            rclpy.shutdown()  # Shutdown the default context

if __name__ == '__main__':
    main()