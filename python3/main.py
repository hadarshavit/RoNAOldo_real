from time import sleep
import stk.python27bridge
import stk.events
import stk.services
from PIL import Image
import pandas as pd
import os
def _read_csv(df):
    num_poses = df.count()[0]
    cols = df.columns
    num_cols = len(cols)

    # Determine number of joints
    num_joints = num_cols - 2

    joint_names = cols[2:]

    return num_poses, num_joints, joint_names, df
def animate(moves, s):
	num_poses, num_joints, joint_names, df = _read_csv(moves)
	for pose in range(num_poses):
		names = []
		angels = []
		for j in range(num_joints):
			name = joint_names[j]
			angle = float(df[name][pose])
			names.append(name)
			angels.append(angle)
			# print(pose, angle, name, robot.getAnglesPosition('LHipPitch'))
			# robot.setAngles(name, angle, 1.0)
		s.ALMotion.setAngles(names, angels, 1)
		print(names, angels)
		sleep(0.01)	# 0.1
class Python3NaoExample:
	def __init__(self):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		print('hello')
		video_service = self.s.ALVideoDevice
		# import IPython; IPython.embed()
		
		forward_csv = pd.read_csv(os.path.join('motions', 'Forwards.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'SideStepLeft.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'SideStepRight.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'TurnLeft40.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'TurnLeft60.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'TurnRight60.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'TurnRight40.csv'))
		animate(forward_csv, self.s)
		forward_csv = pd.read_csv(os.path.join('motions', 'Shoot.csv'))
		animate(forward_csv, self.s)
		exit(0)
		
    	# Register a Generic Video Module
		# resolution = 2
		# colorSpace = 1
		# fps = 20

		# nameId = video_service.subscribe("python_GVM", resolution, colorSpace, fps)

		# print('subs')
		# import time
		# # print 'getting images in remote'
		# for i in range(0, 20):
		# 	print('getting')
		# 	video_service.getImageRemote(nameId)
		# 	time.sleep(0.05)

		# video_service.unsubscribe(nameId)
		resolution = 2    # VGA
		colorSpace = 11   # RGB

		# videoClient = video_service.subscribe("python_client", resolution, colorSpace, 5)
		# print(videoClient)
		# import time
		# time.sleep(10)
		# t0 = time.time()

		# Get a camera image.
		# image[6] contains the image data passed as an array of ASCII chars.
		# naoImage = video_service.getImageRemote(videoClient)
		# print(naoImage)
		# t1 = time.time()

		# Time the image transfer.
		# print "acquisition delay ", t1 - t0

		# video_service.unsubscribe(videoClient)


		# Now we work with the image returned and save it as a PNG  using ImageDraw
		# package.

		# Get the image size and pixel array.
		# imageWidth = naoImage[0]
		# imageHeight = naoImage[1]
		# array = naoImage[6]
		# image_string = str(bytearray(array))

		# Create a PIL Image from our pixel array.
		# im = Image.fromstring("RGB", (imageWidth, imageHeight), image_string)

		# Save the image.
		# im.save("camImage.png", "PNG")

		# im.show()

		# self.s.ALPhotoCapture.setResolution(2)
		# self.s.ALPhotoCapture.setPictureFormat("jpg")
		# self.s.ALPhotoCapture.takePictures(3, "/home/nao/recordings/cameras/", "image")
	# 	self.events.connect("ALAnimatedSpeech/EndOfAnimatedSpeech", self.animated_speech_end)
	# 	self.s.ALAnimatedSpeech.say("This is a test!")
	# 	self.events.wait_for("Jantest/Test")
	# 	self.s.ALAnimatedSpeech.say("And this won't trigger until after a JanTest/Test event is fired (e.g. from Choregraphe)")

	# 	# Choregraphe bezier export in Python.
	# 	names = list()
	# 	times = list()
	# 	keys = list()

	# 	names.append("HeadPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.0134902, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.0134902, [3, -0.8, 0], [3, 0.76, 0]], [-0.0134902, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("HeadYaw")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.110904, [3, -0.0133333, 0], [3, 0.8, 0]], [0.110904, [3, -0.8, 0], [3, 0.76, 0]], [0.110904, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LAnklePitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [0.09, [3, -0.8, 0], [3, 0.76, 0]], [0.09, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LAnkleRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.13, [3, -0.8, 0], [3, 0.76, 0]], [-0.13, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LElbowRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.410388, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.410388, [3, -0.8, 0], [3, 0.76, 0]], [-0.410388, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LElbowYaw")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-1.1937, [3, -0.0133333, 0], [3, 0.8, 0]], [-1.1937, [3, -0.8, 0], [3, 0.76, 0]], [-1.1937, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LHand")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.3, [3, -0.0133333, 0], [3, 0.8, 0]], [0.3, [3, -0.8, 0], [3, 0.76, 0]], [0.3, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LHipPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LHipRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LHipYawPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.17, [3, -0.8, 0], [3, 0.76, 0]], [-0.17, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LKneePitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.09, [3, -0.8, 0], [3, 0.76, 0]], [-0.09, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LShoulderPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[1.47236, [3, -0.0133333, 0], [3, 0.8, 0]], [1.47236, [3, -0.8, 0], [3, 0.76, 0]], [1.47236, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LShoulderRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.185419, [3, -0.0133333, 0], [3, 0.8, 0]], [0.185419, [3, -0.8, 0], [3, 0.76, 0]], [0.185419, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("LWristYaw")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RAnklePitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [0.09, [3, -0.8, 0], [3, 0.76, 0]], [0.09, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RAnkleRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RElbowRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.410388, [3, -0.0133333, 0], [3, 0.8, 0]], [0.39831, [3, -0.8, 0.0062628], [3, 0.76, -0.00594966]], [0.37375, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RElbowYaw")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[1.1937, [3, -0.0133333, 0], [3, 0.8, 0]], [1.17088, [3, -0.8, 0], [3, 0.76, 0]], [1.19705, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RHand")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.3, [3, -0.0133333, 0], [3, 0.8, 0]], [0.3, [3, -0.8, 0], [3, 0.76, 0]], [0.3, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RHipPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.13, [3, -0.0133333, 0], [3, 0.8, 0]], [0.13, [3, -0.8, 0], [3, 0.76, 0]], [0.13, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RHipRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.1, [3, -0.8, 0], [3, 0.76, 0]], [-0.1, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RHipYawPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.17, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.17, [3, -0.8, 0], [3, 0.76, 0]], [-0.17, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RKneePitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.09, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.09, [3, -0.8, 0], [3, 0.76, 0]], [-0.09, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RShoulderPitch")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[1.47236, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.9518, [3, -0.8, 0], [3, 0.76, 0]], [2.08567, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RShoulderRoll")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[-0.185419, [3, -0.0133333, 0], [3, 0.8, 0]], [-0.122768, [3, -0.8, 0], [3, 0.76, 0]], [-0.189514, [3, -0.76, 0], [3, 0, 0]]])

	# 	names.append("RWristYaw")
	# 	times.append([0.04, 2.44, 4.72])
	# 	keys.append([[0.1, [3, -0.0133333, 0], [3, 0.8, 0]], [0.1, [3, -0.8, 0], [3, 0.76, 0]], [0.1, [3, -0.76, 0], [3, 0, 0]]])

	# 	self.s.ALMotion.angleInterpolationBezier(names, times, keys)
	# 	exit(0)

	def ball_position(self, args):
		print(args)
	# def animated_speech_end(self, args):
	# 	print("Animated speech ended..")

	# 	if args:
	# 		print(args)

	# 	self.events.disconnect("ALAnimatedSpeech/EndOfAnimatedSpeech")
	# 	self.s.ALAnimatedSpeech.say("This is another test!")



if __name__ == "__main__":
    Python3NaoExample()
