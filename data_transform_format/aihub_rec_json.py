'''AI허브 인쇄체 데이터 mmocr Rec용 변환'''

import io
import os
from PIL import Image, ImageFile, ImageDraw
import json
import natsort
from glob import glob
from tqdm import tqdm
import time

output_path = 'textrec_test.json'
json_path = '02.인쇄체_230721_add/printed_data_info.json'
data_dict = {}
data_list = []
i = 0
with open(json_path,"r") as file:
	data = json.load(file)

	for p,q in enumerate(data["annotations"]):
		image_id = q["image_id"]
		text = q["text"]
		#print(image_id)
		#print(text)

		text_dict = {}
		text_list = []
		path_dict = {}
		da_dict = {}
		dum_dict = {}

		text_dict['text'] = text
		#print(text_dict['text'])
		dum_dict['instances'] = [text_dict]
		imgpath = 'word/' + image_id + '.png'

		path_dict['img_path'] = imgpath
		dum_dict['img_path'] = imgpath

		data_dict['in']=text_dict
		da_dict['instances'] = [data_dict['in']]
		#print(da_dict)

		data_list.append(dum_dict)
		i = i + 1
		if i == 300:
			print('300 done')
			break

#print(data_list)
textdet_test_dict = {"metainfo": {"dataset_type":"TextRecogDataset", "task_name":"textrecog"}, "data_list":data_list}

with open(output_path, 'w', encoding='utf-8') as json_file:
  json.dump(textdet_test_dict, json_file, ensure_ascii=False)