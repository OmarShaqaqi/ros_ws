import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSaver(Node):
    def __init__(self):
        super().__init__('image_saver')
        self.bridge = CvBridge()
        self.saved = False
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',   # change if needed
            self.callback,
            10
        )

    def callback(self, msg):
        if self.saved:
            return  # only save once

        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imwrite('robomaster_frame.jpg', frame)
        self.get_logger().info("Saved image as robomaster_frame.jpg")
        self.saved = True

def main():
    rclpy.init()
    saver = ImageSaver()
    rclpy.spin(saver)
    saver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
