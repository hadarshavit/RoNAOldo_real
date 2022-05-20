import sys
print(sys.path)
# sys.path = sys.path[2: ]
sys.path.remove('C:\\Users\\Hadar\\Downloads\\pynaoqi-python2.7-2.8.7.4-win64-vs2015-20210818_210634\\pynaoqi-python2.7-2.8.7.4-win64-vs2015-20210818_210634\\lib')
sys.path.append('C:\Users\Hadar\Downloads\pynaoqi-python2.7-2.1.4.13-win32-vs2010\pynaoqi-python2.7-2.1.4.13-win32-vs2010')
sys.path.append(' ')
sys.path.append(r'C:\Users\Hadar\Downloads\robot-jumpstarter-python3-master\robot-jumpstarter-python3-master\python27\stk')
print(sys.path)
import naoqi
from naoqi import ALProxy
import vision_definitions
import time
from PIL import Image
import cv2
import numpy as np
####
# Create proxy on ALVideoDevice
from naoqi import ALProxy

def detectball(image):
	blurred = cv2.GaussianBlur(image, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask_l = np.array([0, 100, 100]) #pink
	mask_h = np.array([50, 255, 255])
	mask = cv2.inRange(hsv, mask_l, mask_h)
	kernel = np.ones((5, 5))
	mask = cv2.erode(mask, kernel, iterations=1)
	contours0, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE, offset=(0, 0))
  # cv2.drawContours(image, cont)
	if len(contours0) == 0:
		return 0, 0, 0, 0
	c = max(contours0, key=cv2.contourArea)
	x, y, w, h = cv2.boundingRect(c)
	if w < 20 or w > 300:
		return 0, 0, 0, 0
	return x, y, w, h

def showNaoImage(IP, PORT):
  """
  First get an image from Nao, then show it on the screen with PIL.
  """

  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 2    # VGA
  colorSpace = 11   # RGB
  camProxy.setActiveCamera(1)
  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()
  time.sleep(0.5)
  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  # while True:
  naoImage = camProxy.getImageRemote(videoClient)
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array, 'raw')
  im.save("imageBottom" + ".png", "PNG")  
  opencvImage = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
  out = detectball(opencvImage)
  print out
  # time.sleep(1)
  t1 = time.time()

  # Time the image transfer.
  # print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  # imageWidth = naoImage[0]
  # imageHeight = naoImage[1]
  # array = naoImage[6]

  # Create a PIL Image from our pixel array.
  # im = Image.frombytes("RGB", (imageWidth, imageHeight), array, 'raw')

  # Save the image.
  # im.save("camImage.png", "PNG")

  # im.show()



if __name__ == '__main__':
  IP = "169.254.139.196"  # Replace here with your NaoQi's IP address.
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]

  naoImage = showNaoImage(IP, PORT)