# 文件夹说明

img：GUI界面运行图片

img_out：检测结果图片保存文件夹

imgs：测试图片集

logs：权重文件

map_out：模型评估结果

model_data：预训练模型

nets：YOLOX-CBAM网络结构

utils：分析数据集工具

venv：虚拟环境文件

video_out：视频检测结果保存文件夹

VOCdevkit：数据集文件

# py文件说明：

get_map.py：获取模型评估结果

gui.py：GUI界面

summary.py：查看网络结构

train.py：训练数据集代码

voc_annotation.py：数据集划分

yolo.py：检测器

# 其他文件说明：

2007_train.txt：划分数据集后得到的训练图片文件名

2007_val.txt：划分数据集后得到的验证图片文件名

requirements.txt：系统运行所需库名

video_test.mp4：测试视频

# 划分数据集：

运行VOCdevkit\VOC2007中的voc_get_main.py文件获取trainval.txt、test.txt、train.txt、val.txt文件。

```python
python .\VOCdevkit\VOC2007\voc_get_main.py
```

运行主目录下的voc_annotation.py得到2007_train.txt和2007_val.txt。

```python
python .\voc_annotation.py
```

# 训练数据集：

运行train.py文件对数据集进行训练

```python
python .\train.py
```

# 获取模型评估结果：

运行get_map.py文件对数据集进行训练

```python
python .\get_map.py
```

# 运行GUI界面：

运行gui.py文件对数据集进行训练

```python
python .\gui.py
```

# 使用教程：

见使用说明文档。