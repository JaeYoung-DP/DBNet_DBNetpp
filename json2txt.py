import json
import os
from pathlib import Path

def convert_bbox_to_polygon(bbox):
    x, y, w, h = bbox
    return [
        x, y,
        x + w, y,
        x + w, y + h,
        x, y + h
    ]

def process_json_file(json_path, output_folder):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    output_lines = []
    for annotation in data.get('annotations', []):
        bbox = annotation.get('annotation.bbox')
        text = annotation.get('annotation.text')
        
        if bbox and text:
            polygon = convert_bbox_to_polygon(bbox)
            line = ', '.join(map(str, polygon)) + f', {text}'
            output_lines.append(line)
    
    output_filename = Path(json_path).stem + '.txt'
    output_path = os.path.join(output_folder, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

def main():
    input_folder = input("JSON 파일이 있는 폴더 경로를 입력하세요: ")
    output_folder = input("결과 TXT 파일을 저장할 폴더 경로를 입력하세요: ")
    
    # 출력 폴더가 존재하지 않으면 생성
    os.makedirs(output_folder, exist_ok=True)
    
    # 입력 폴더 내의 모든 JSON 파일 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            json_path = os.path.join(input_folder, filename)
            process_json_file(json_path, output_folder)
            print(f"처리 완료: {filename}")

if __name__ == "__main__":
    main()