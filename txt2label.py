import os
txt_path = r"C:\Data_set\test_img\mask_rect\rect.txt"
if os.path.exists(txt_path):
    with open(txt_path) as file:
        for line in file:
            line = line.strip()
            line_list = line.split(" ",1)
            img_name = line_list[0]#图片名称
            try:
                label = line_list[1].strip().split(" ")
            except:
                print(img_name+"文件解析错误")
            label_list = []#坐标列表
            for i in label:
                label_list.append(int(i))
exit()