import json
import os
import io
import cv2
import readline
from tqdm import tqdm
import time
import natsort
import numpy as np

data_list = []

data_dict = {}



with open('./book/gt.txt', 'r',encoding='utf-8') as f:
  while True:
    line = f.readline()

    if not line:
      break

    split_line = line.split('\t')[-1]
    text = split_line.split('\n')[0]
    img_path = line.split('\t')[0]
    

    text_dict = {}
    text_list = []
    path_dict = {}
    da_dict = {}
    dum_dict = {}

    text_dict['text'] = text
    dum_dict['instances'] = [text_dict]


    imgpath = 'book/img/'+img_path

    path_dict['img_path'] = imgpath
    dum_dict['img_path'] = imgpath

    data_dict['in']=text_dict
    da_dict['instances'] = [data_dict['in']]
    a = path_dict.items()

    data_list.append(dum_dict)
    #data_list.append(path_dict)



#textdet_train_dict = {"metainfo": {"dataset_type":"TextRecogDataset", "task_name":"textrecog", "data_list": data_list}}
textdet_train_dict = {"metainfo": {"dataset_type":"TextRecogDataset", "task_name":"textrecog"}, "data_list":data_list}
# data_list [{"instances":[{"text": "CHARACTER"}],"img_path": "path"}]
#print(textdet_train_dict)
#{"metainfo":{"dataset_type": "TextRecogDataset","task_name":"textrecog"},"data_list": [{"instances": [{"text": split_line}], "img_path": "img_path_list"}]}


with open('textrec_test.json', 'w', encoding='utf-8') as json_file:
  json.dump(textdet_train_dict, json_file, ensure_ascii=False)