from csv2mask import mask
from bobl_analysis import find_rect
import cv2 as cv
if __name__ == '__main__':
    cvs_path = r"C:\Data_set\test_img\Kaggle钢铁数据集\train.csv"
    img_path = r"C:\Data_set\test_img\Kaggle钢铁数据集\train_images"
    save_path = r"C:\Data_set\test_img\mask"
    save_dir_path =r"C:\Data_set\test_img\mask_rect\image"
    save_txt_path = r"C:\Data_set\test_img\mask_rect\rect.txt"
    file = open(save_txt_path, "w")
    for mask,defect_type,img_name in mask(cvs_path,img_path,save_path):
        #if defect_type == "1":
        mask,rect_list = find_rect(mask)
        rect_str = str(rect_list)
        file.write(img_name + " " + rect_str + "\n")
        cv.imwrite(save_dir_path + "\\" + img_name, mask)
        continue
        # elif defect_type == 2:
        # elif defect_type == 3:
        # elif defect_type == 4:
    file.close()