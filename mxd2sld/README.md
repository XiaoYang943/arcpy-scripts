## 源码
- https://github.com/arashmad/mxd2sld

## 调试代码、搭建环境
### arcgis desktop
- 设置pycharm的python解释器: `C:\Python27\ArcGIS10.8\python.exe`
### arcgis pro(代码暂不支持，arcmap用的是python2，pro用的是python3，且arcpy这两个版本接口不一样)
- [参考](https://blog.csdn.net/xza13155/article/details/124004121)

## 执行
### 方法一: 命令行执行
#### 生成依赖列表文件
- cd到该文件夹下
- 执行 `pip freeze >requirements.txt`
#### 安装相关依赖
- cd到arcgis的python路径下，例如(C:\Python27\ArcGIS10.8)
- 执行 `pip install -r 替换为requirements文件路径`
#### 执行脚本
- cd到arcgis的python路径下，例如(C:\Python27\ArcGIS10.8)
- 执行 `python 替换为main.py文件路径 -input 替换为mxd文件路径 -output 替换为输出文件夹路径`
### 方法二: 本地调试
#### 生成依赖列表文件
- cd到该文件夹下
- 执行 `pip freeze >requirements.txt`
#### 安装相关依赖
- cd到arcgis的python路径下，例如(C:\Python27\ArcGIS10.8)
- 执行 `pip install -r 替换为requirements文件路径`
#### 执行脚本
- 替换main.py主方法中的input和output参数
- 执行主方法

## 服务器离线环境安装依赖
- cd到mxd2sld文件夹下
- pip freeze >requirements.txt
- pip download -d packages -r requirements.txt
- 将mxd2sld文件夹拷贝到离线机器上的arcgis-python文件夹下，例如：C:\Python27\ArcGIS10.8
- cd到C:\Python27\ArcGIS10.8文件夹下
- pip install --no-index --find-links=C:\Python27\ArcGIS10.8\mxd2sld\packages -r C:\Python27\ArcGIS10.8\mxd2sld\requirements.txt

## 目前支持的symbol类型
### 点
- Character Marker Symbol(文本型标记)
- Simple Marker Symbol(纯色)
### 线
- Simple Line Symbol(纯色)
### 面
- Picture Fill Symbol(图片型面状纹理)
- Simple Fill Symbol(纯色)