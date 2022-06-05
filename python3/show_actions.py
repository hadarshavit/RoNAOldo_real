from distutils.util import split_quoted
from time import sleep
import stk.python27bridge
import stk.events
import stk.services
from PIL import Image
import pandas as pd
import os
import numpy as np
import cv2
import subprocess
from stable_baselines3 import PPO


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
		s.ALMotion.setAngles(names, angels, 0.1)


def get_ball_position():
	stdout = subprocess.run([r'C:\\Python2732\\python.exe', r'C:\\Users\\Hadar\\Downloads\\robot-jumpstarter-python3-master\\robot-jumpstarter-python3-master\\get_image.py'], check=False, capture_output=True, text=True).stdout
	print(stdout.split('\n')[-2])
	coords = stdout.split('\n')[-2]
	print(coords, coords[1:-1].split(','))
	splitted = coords[1:-1].split(',')
	x = int(splitted[0])
	y = int(splitted[1])
	w = int(splitted[2])
	h = int(splitted[3])
	print(x, y, w, h)

	return x, y, w, h
class Python3NaoExample:
	def __init__(self):
		self.python27bridge = stk.python27bridge.Python27Bridge()
		self.events = stk.events.EventHelper(self.python27bridge)
		self.s = stk.services.ServiceCache(self.python27bridge)
		print('hello')

		actions = [0, 2, 3, 4, 5, 6, 7, 1]
		import numpy as np
		for action in actions:
			print(action)
			if action == 0:
				self.s.ALMotion.moveTo(0.05, 0, 0)
			elif action == 1:
				forward_csv = pd.read_csv(os.path.join('motions', 'Shoot.csv'))
				animate(forward_csv, self.s)
				break
			elif action == 2:
				forward_csv = pd.read_csv(os.path.join('motions', 'SideStepLeft.csv'))
				animate(forward_csv, self.s)
			elif action == 3:
				forward_csv = pd.read_csv(os.path.join('motions', 'SideStepRight.csv'))
				animate(forward_csv, self.s)
			elif action == 4:
				forward_csv = pd.read_csv(os.path.join('motions', 'TurnLeft40.csv'))
				animate(forward_csv, self.s)
			elif action == 5:
				forward_csv = pd.read_csv(os.path.join('motions', 'TurnLeft60.csv'))
				animate(forward_csv, self.s)
			elif action == 6:
				forward_csv = pd.read_csv(os.path.join('motions', 'TurnRight40.csv'))
				animate(forward_csv, self.s)
			elif action == 7:
				forward_csv = pd.read_csv(os.path.join('motions', 'TurnRight60.csv'))
				animate(forward_csv, self.s)
		exit(0)
		

if __name__ == "__main__":
    Python3NaoExample()
