import os
import cv2
import albumentations as A
import numpy as np

image_folder = './data../ship_fixed_2200/test_i'
label_folder = './data../ship_fixed_2200/test_g'
output_image_folder = './data../ship_fixed_2200/ship_aug_i'
output_label_folder = './data../ship_fixed_2200/ship_aug_g'

image_list = []
label_list = []

for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    label_path = os.path.join(label_folder, filename.replace('.JPG', '.txt'))

    image = cv2.imread(image_path)
    image_list.append(image)

    label = []
    with open(label_path, 'r') as f:
        for line in f:
            bbox = []
            for coord in line.strip().split(','):
                try:
                    bbox.append(float(coord))
                except ValueError:
                    bbox.append(coord)
            label.append(bbox)

    label_list.append(label)

transform = A.Compose([
    A.Blur(blur_limit=(3,7), p=1.0)], bbox_params=A.BboxParams(format='pascal_voc'))

augmented_images = []
augmented_labels = []

for index in range(len(image_list)):
    image = image_list[index]
    label = label_list[index]

    augmented_data = transform(image=image, bboxes=label)
    augmented_image = augmented_data['image']
    augmented_label = augmented_data['bboxes']

    augmented_images.append(augmented_image)
    augmented_labels.append(augmented_label)

for i in range(len(augmented_images)):
    augmented_image = augmented_images[i]
    augmented_label = augmented_labels[i]

    image_name = f'augmented_image_{i}.JPG'
    image_path = os.path.join(output_image_folder, image_name)
    cv2.imwrite(image_path, augmented_image)

    label_name = f'augmented_label_{i}.txt'
    label_path = os.path.join(output_label_folder, label_name)
    with open(label_path, 'w') as f:
        for bbox in augmented_label:
            try:
                if bbox[3] < bbox[1] or bbox[4] < bbox[2]:
                    print(f"Invalid bounding box: {bbox}")
                    continue
                bbox_str = ",".join(str(coord) for coord in bbox)
                f.write(bbox_str + "\n")
                if isinstance(bbox[-1], str):
                    print(f"Found string value: {bbox[-1]}")
            except IndexError:
                print(f"Invalid bounding box format: {bbox}")

    print(f'Saved augmented image: {image_path}')
    print(f'Saved augmented label: {label_path}')