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

####
# Create proxy on ALVideoDevice
from naoqi import ALProxy


def showNaoImage(IP, PORT):
  """
  First get an image from Nao, then show it on the screen with PIL.
  """

  camProxy = ALProxy("ALVideoDevice", IP, PORT)
  resolution = 2    # VGA
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  while True:
    naoImage = camProxy.getImageRemote(videoClient)
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    im = Image.frombytes("RGB", (imageWidth, imageHeight), array, 'raw')
    im.save("imageBottom" + ".png", "PNG")  
  t1 = time.time()

  # Time the image transfer.
  print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Create a PIL Image from our pixel array.
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array, 'raw')

  # Save the image.
  im.save("camImage.png", "PNG")

  im.show()



if __name__ == '__main__':
  IP = "169.254.139.196"  # Replace here with your NaoQi's IP address.
  PORT = 9559

  # Read IP address from first argument if any.
  if len(sys.argv) > 1:
    IP = sys.argv[1]

  naoImage = showNaoImage(IP, PORT)