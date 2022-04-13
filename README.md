# 方法
## 公式
![image](https://github.com/earthpopo/Decode_cvs/blob/master/mathpix.png)
按照上述公式对CSV文件进行解析，并找出每个连通域的矩形框坐标，写入txt文件中
## 找框
```python
# elif defect_type == 2:
# elif defect_type == 3:
# elif defect_type == 4:
```        
寻找矩形框可以按类别用不同的方法，现在默认均使用[默认方法](https://github.com/earthpopo/Decode_cvs/blob/4bf8d46062456da1dc6f012ce0af590f5a62393f/csv2mask.py)
## 默认方法
```python
mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(cont)
```
使用开运算将粘连的缺陷分开，再找到连通域，最后找坐标
# 结果
正常结果：![image](https://github.com/earthpopo/Decode_cvs/blob/a218b09e2a4ffb970a9ebfa7655b396d6c748cd0/00f6e702c.jpg)
异常：![image](https://github.com/earthpopo/Decode_cvs/blob/a218b09e2a4ffb970a9ebfa7655b396d6c748cd0/mask_rect.jpg)