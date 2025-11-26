import cv2
import numpy as np

# ====== 1. Load the test image ======
img = cv2.imread("test_images/red_image.png")
if img is None:
    raise ValueError("Image not found!")

# ====== 2. Convert to HSV ======
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ====== 3. Define color ranges ======
# Red in HSV has 2 ranges due to wrap-around
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# ====== 4. Threshold to get red mask ======
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 | mask2

# ====== 5. Clean mask ======
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

# ====== 6. Find contours ======
cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cnts) == 0:
    print("No red block detected.")
    exit()

# largest contour = block
c = max(cnts, key=cv2.contourArea)

# ====== 7. Compute centroid ======
M = cv2.moments(c)
cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])

# ====== 8. Bounding box ======
x, y, w, h = cv2.boundingRect(c)

print(f"Red block detected at pixel = ({cx}, {cy}) with size {w}x{h}")

# ====== 9. Visualize ======
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
cv2.circle(img, (cx, cy), 6, (0, 255, 0), -1)

cv2.imshow("Red Block Detection", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
