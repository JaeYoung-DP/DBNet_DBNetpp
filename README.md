# DBNet_ship-Text-Detection

#### Train
```
CUDA_VISIBLE_DEVICES=0 python tools/train.py configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py
```
### Test

```
CUDA_VISIBLE_DEVICES=0 python tools/test.py configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py dbnetpp.pth --work-dir () --show-dir ()
```

#### Introduction

해당 모델은 opentoolkit인 mmocr-DBNet,DBNet++ / github-DBNet 을 활용하여 한국 선박 문자열 검출 시스템에 적용하였습니다.

### DBNet
||Precision|Recall|H-mean|
|:-----:|:----:|:---:|:---:|
|한국어|0.9790|0.8750|0.9241|
|영어|0.9000|0.7397|0.8120|
|숫자|0.9050|0.7902|0.8438|

### DBNet++
||Precision|Recall|H-mean|
|:-----:|:----:|:---:|:---:|
|한국어|0.9405|0.9875|0.9634|
|영어|0.9381|0.7982|0.8626|
|숫자|0.9745|0.7688|0.8596|


출처: 

https://mmocr.readthedocs.io/en/dev-1.x/user_guides/train_test.html

https://github.com/open-mmlab/mmocr

https://github.com/MhLiao/DB

