import rclpy
from rclpy.node import Node
from ur_msgs.srv import SetIO

class IOToggleClient(Node):
    def __init__(self):
        super().__init__('io_toggle_client')
        self.client = self.create_client(SetIO, '/io_and_status_controller/set_io')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetIO.Request()

    def send_request(self, pin_state_pairs):
        for pin, state in pin_state_pairs:
            self.req.fun = 1  # 1 is for digital output
            self.req.pin = pin
            self.req.state = state
            self.future = self.client.call_async(self.req)
            while rclpy.ok():
                rclpy.spin_once(self)
                if self.future.done():
                    break

def main(args=None):
    rclpy.init(args=args)
    io_toggle_client = IOToggleClient()
    io_toggle_client.send_request([(0, 1.0), (1, 0.0)])  # Set pin 17 to 1.0 and pin 18 to 0.0
    io_toggle_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()