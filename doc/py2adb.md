# py2adb
---
简易的python操作安卓手机的api
## 用法示例
```python
import py2adb as adb
phone=adb.Phone()
```
### 点击
```python
phone.touch([0,0])
```
### 划手指 0,0 到 100,100
```python
phone.wipe([0, 0, 100, 100])
```
### 截图
```python
phone.screen(fileName="文件名")
```
## 数据方法
类 Phone  
    方法:  
        touch(list)   
        输入：list 长度2 类型 int  
        wipe(list)  
        输入：list 长度4 类型 int  
        scree(fileName='screen_cache')  
        输入：str    
## TODO
- [.] debug
