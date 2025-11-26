import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from perception.msg import BlockDetection

import cv2
import numpy as np
from cv_bridge import CvBridge
import yaml
import os

class ColorDetector(Node):
    def __init__(self):
        super().__init__('color_detector')

        # Load thresholds
        config_path = os.path.join(
            os.path.dirname(__file__), '..', 'config', 'color_thresholds.yaml'
        )
        with open(config_path, 'r') as f:
            self.color_thresholds = yaml.safe_load(f)

        self.bridge = CvBridge()

        # Subscribers
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        # Publishers
        self.pub = self.create_publisher(BlockDetection, '/block_detection', 10)

        self.get_logger().info("Color detector node started.")

    def image_callback(self, msg):
        # Convert image
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Loop over all defined colors
        for color_name, vals in self.color_thresholds.items():
            lower = np.array(vals['lower'])
            upper = np.array(vals['upper'])

            mask = cv2.inRange(hsv, lower, upper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(cnts) == 0:
                continue

            # Largest contour = block
            c = max(cnts, key=cv2.contourArea)
            area = cv2.contourArea(c)

            if area < 300:
                continue  # ignore noise

            M = cv2.moments(c)
            if M['m00'] == 0:
                continue

            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            x, y, w, h = cv2.boundingRect(c)

            # Publish
            det = BlockDetection()
            det.color = color_name
            det.pixel_x = cx
            det.pixel_y = cy
            det.width = w
            det.height = h
            det.confidence = 1.0  # HSV always returns full confidence

            self.pub.publish(det)
            self.get_logger().info(f"Detected {color_name} at ({cx}, {cy})")

def main(args=None):
    rclpy.init(args=args)
    node = ColorDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
