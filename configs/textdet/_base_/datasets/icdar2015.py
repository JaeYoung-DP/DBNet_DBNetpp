icdar2015_textdet_data_root = 'data/ship_data'
#train_data_root = 'data/capstone_data/train'
#test_data_root = 'data/capstone_data/test'

icdar2015_textdet_train = dict(
    type='OCRDataset',
    data_root=icdar2015_textdet_data_root,
    #data_root = train_data_root,
    ann_file='textdet_train.json',
    filter_cfg=dict(filter_empty_gt=True, min_size=32),
    pipeline=None)

icdar2015_textdet_test = dict(
    type='OCRDataset',
    data_root=icdar2015_textdet_data_root,
    #data_root = test_data_root,
    ann_file='textdet_test.json',
    test_mode=True,
    pipeline=None)

