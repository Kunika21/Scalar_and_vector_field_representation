import numpy as np
import glob
import sys
import cv2
import os

img_array = []
img_dir = sys.argv[1] + "*.png"
for filename in sorted(glob.glob(img_dir)):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
print(len(img_array))
if os.path.exists(sys.argv[1] + '../../resultant_video'):
	pass
else:
	os.makedirs(sys.argv[1] + '../../resultant_video')
vid_save_path = os.path.join(os.path.dirname(img_dir), '../../resultant_video')
filename = sys.argv[2]

out = cv2.VideoWriter(os.path.join(vid_save_path, filename),cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 3, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()