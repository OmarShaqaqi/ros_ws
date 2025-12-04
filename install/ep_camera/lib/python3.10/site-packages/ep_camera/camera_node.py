import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from robomaster import robot
import cv2

class EPCameraNode(Node):
    def __init__(self):
        super().__init__('ep_camera_node')

        self.bridge = CvBridge()
        self.publisher = self.create_publisher(Image, 'camera/image_raw', 10)

        self.get_logger().info("Connecting to RoboMaster EP...")
        self.ep = robot.Robot()
        self.ep.initialize(conn_type="sta")

        self.ep.camera.start_video_stream(display=False, resolution='720p')

        self.timer = self.create_timer(0.05, self.publish_frame)
        self.get_logger().info("EP Camera Node Started.")

    def publish_frame(self):
        frame = self.ep.camera.read_cv2_image(strategy="newest")
        if frame is None:
            return
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        msg.header.stamp = self.get_clock().now().to_msg()
        self.publisher.publish(msg)

    def destroy_node(self):
        self.ep.camera.stop_video_stream()
        self.ep.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = EPCameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
