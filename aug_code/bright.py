import cv2
import os
import shutil
import random

image_folder_path = "./data/fixed_i"
label_folder_path = "./data/fixed_g"
output_image_folder_path = "./data/aug_i"
output_label_folder_path = "./data/aug_g"

def augment_image(image_path, output_image_folder, output_label_folder):
    image = cv2.imread(image_path)

    # 원본 이미지 저장
    output_image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_image_path = os.path.join(output_image_folder, output_image_name + ".JPG")
    cv2.imwrite(output_image_path, image)

    # 블러 이미지 저장
    blur_probability = 1.0
    if random.random() < blur_probability:
        blurred_image = cv2.GaussianBlur(image, (5, 5), 2)
        output_image_name = os.path.splitext(os.path.basename(image_path))[0] + "_blurred"
        output_image_path = os.path.join(output_image_folder, output_image_name + ".JPG")
        cv2.imwrite(output_image_path, blurred_image)

    # 조도 증가 이미지 저장
    brightness = 60  # 밝기 증가량 (0-255 범위)
    brightened_image = cv2.addWeighted(image, 1, image, 0, brightness)
    brightened_image_name = os.path.splitext(os.path.basename(image_path))[0] + "_brightened"
    brightened_image_path = os.path.join(output_image_folder, brightened_image_name + ".JPG")
    cv2.imwrite(brightened_image_path, brightened_image)

    # 그레이스케일 이미지 저장
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image_name = os.path.splitext(os.path.basename(image_path))[0] + "_gray"
    gray_image_path = os.path.join(output_image_folder, gray_image_name + ".JPG")
    cv2.imwrite(gray_image_path, gray_image)

    # 원본 이미지의 라벨 파일 경로
    label_file_path = os.path.join(label_folder_path, os.path.splitext(os.path.basename(image_path))[0] + ".txt")

    # 라벨 파일이 존재하는 경우 결과 폴더에 복사
    if os.path.exists(label_file_path):
        # 원본 라벨 파일 경로
        original_label_output_path = os.path.join(output_label_folder, os.path.splitext(os.path.basename(image_path))[0] + ".txt")
        shutil.copy(label_file_path, original_label_output_path)

        # 첫 번째 라벨 파일 경로
        first_label_output_path = os.path.join(output_label_folder, os.path.splitext(os.path.basename(image_path))[0] + "_label1.txt")
        shutil.copy(label_file_path, first_label_output_path)

        # 두 번째 라벨 파일 경로
        second_label_output_path = os.path.join(output_label_folder, os.path.splitext(os.path.basename(image_path))[0] + "_label2.txt")
        shutil.copy(label_file_path, second_label_output_path)

        # 세 번째 라벨 파일 경로
        third_label_output_path = os.path.join(output_label_folder, os.path.splitext(os.path.basename(image_path))[0] + "_label3.txt")
        shutil.copy(label_file_path, third_label_output_path)

# 원본 이미지를 증강하여 결과 이미지와 라벨 생성
for image_file in os.listdir(image_folder_path):
    image_path = os.path.join(image_folder_path, image_file)
    augment_image(image_path, output_image_folder_path, output_label_folder_path)