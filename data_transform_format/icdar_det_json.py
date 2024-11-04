import json
import os
import io
import cv2
import readline
from tqdm import tqdm
import time
import natsort

def polygon2bbx(polygone):
  Polygon = polygone
  bbx = [polygon[0] for polygon in Polygon]
  bbx1 = [polygon[1] for polygon in Polygon]
  max_x = float(max(bbx))
  min_x = float(min(bbx))
  max_y = float(max(bbx1))
  min_y = float(min(bbx1))
  b_box = []
  b_box.append(min_x)
  b_box.append(min_y)
  b_box.append(max_x)
  b_box.append(max_y)

  return b_box

data_list = []

img_path_list = []

for img_path in natsort.natsorted(os.listdir('./data/capstone/kr_imgs')):  # img_path
  img_path_list.append(img_path)

i = 0

for path in tqdm(natsort.natsorted(os.listdir('./data/capstone/kr_gt'))):   # gt_path
  time.sleep(0.01)

  data_dict = {}

  data_dict["instances"] = []

  img = cv2.imread('./data/capstone/kr_imgs/{}'.format(img_path_list[i]))
  height, width = img.shape[:2]

  data_dict["img_path"] = ('kr_imgs/{}'.format(img_path_list[i]))
  data_dict["height"] = height
  data_dict["width"] = width
  data_dict["seg_map"] = ('kr_gt/{}'.format(path))

  with open('./data/capstone/kr_gt/{}'.format(path), 'r') as f:
    while True:
      line = f.readline()
      if not line:
        break

      split_line = line.split(',')

      x1 = (split_line[0])
      y1 = (split_line[1])
      x2 = (split_line[2])
      y2 = (split_line[3])
      x3 = (split_line[4])
      y3 = (split_line[5])
      x4 = (split_line[6])
      y4 = (split_line[7])

      polygon = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
      polygon1 = [x1, y1, x2, y2, x3, y3, x4, y4]

      dummy_dict = {}
      dummy_dict['polygon'] = polygon1
      dummy_dict['bbox'] = polygon2bbx(polygon)
      dummy_dict['bbox_label']  = 0


      if split_line[-1].replace('\n','')=="###":
        dummy_dict['ignore'] = True
        #print(split_line[9], dummy_dict['ignore'])
      else:
        dummy_dict['ignore'] = False
        dummy_dict['character'] = split_line[-1].replace('\n','')
        #print(split_line[9], dummy_dict['ignore'])

      data_dict['instances'].append(dummy_dict)

  data_list.append(data_dict)

  i = i + 1

tqdm(natsort.natsorted(os.listdir('./data/capstone/kr_gt'))).close()


textdet_test_dict = {"metainfo": {"dataset_type":"TextDetDataset", "task_name":"textdet", "category":[{"id":0, "name":"text"}]}, "data_list": data_list} # data_list -> polygon, bbox, bbox_label, ignore
#print(textdet_train_dict)


with open('./data/capstone/textdet_test.json', 'w') as json_file:
  json.dump(textdet_test_dict, json_file)