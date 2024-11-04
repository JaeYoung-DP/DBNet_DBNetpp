import cv2
import os
import shutil
import random


image_folder_path = "./data../ship_fixed_2200/test_i"
label_folder_path = "./data../ship_fixed_2200/test_g"
output_image_folder_path = "./data../ship_fixed_2200/ship_aug_i"
output_label_folder_path = "./data../ship_fixed_2200/ship_aug_g"

def augment_image(image_path, output_image_folder, output_label_folder):

    image = cv2.imread(image_path)
   
    blur_probability = 1.0  
    if random.random() < blur_probability:
        blurred_image = cv2.GaussianBlur(image, (5, 5), 2)
        output_image_name = os.path.splitext(os.path.basename(image_path))[0] + "_blurred"
    else:
        blurred_image = image
        output_image_name = os.path.splitext(os.path.basename(image_path))[0]
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image_extension = os.path.splitext(os.path.basename(image_path))[1]
   
    # 이미지 파일 저장 경로
    blurred_image_path = os.path.join(output_image_folder, output_image_name + image_extension)
    gray_image_path = os.path.join(output_image_folder, image_name + "_gray" + image_extension)
   
    # 이미지 파일 저장
    cv2.imwrite(blurred_image_path, blurred_image)
    cv2.imwrite(gray_image_path, gray_image)
   
    # 원본 이미지의 라벨 파일 경로
    label_file_path = os.path.join(label_folder_path, image_name + ".txt")
   
    # 라벨 파일이 존재하는 경우 결과 폴더에 복사
    if os.path.exists(label_file_path):
        # 첫 번째 라벨 파일 경로
        first_label_output_path = os.path.join(output_label_folder, image_name + "_label1.txt")
        shutil.copy(label_file_path, first_label_output_path)
       
        # 두 번째 라벨 파일 경로
        second_label_output_path = os.path.join(output_label_folder, image_name + "_label2.txt")
        shutil.copy(label_file_path, second_label_output_path)

# 원본 이미지를 증강하여 결과 이미지와 라벨 생성
for image_file in os.listdir(image_folder_path):
    image_path = os.path.join(image_folder_path, image_file)
    augment_image(image_path, output_image_folder_path, output_label_folder_path)