# import cv2
#
# # cap = cv2.VideoCapture('action.mp4') #读取指定视频
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # fps = cap.get(cv2.CAP_PROP_FPS)
# # 保证摄像头的输出与保存的视频尺寸大小相同
# size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# out = cv2.VideoWriter('camera_test.avi', fourcc, 10.0, size)
# while True:
#     ret, frame = cap.read()
#
#     # 在图像上显示 Press Q to save and quit
#     # cv2.putText(frame, "Press Q to save and quit",
#     #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
#     # cv2.putText(frame, "Press Q to save",
#     #             (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
#     frame = cv2.putText(frame, "Press Q to save and quit", (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     frame = cv2.putText(frame, "Press Q to save and quit", (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     # frame = cv2.putText(frame, "Press Q to save and quit", (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
#     cv2.imshow('frame', frame)
#     out.write(frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# # from openpyxl import Workbook
# # from openpyxl.utils import get_column_letter
# # import csv
# # import pandas as pd
# # head_row_list = ['picture name', 'rubbish class']
# # picture_dictionary = {'A0_1.jpg': 'A0', 'A0_17.jpg': 'unknown', 'A0_18.jpg': 'A0', 'A0_19.jpg': 'unknown', 'A0_2.jpg': 'A0', 'A0_20.jpg': 'A0', 'A0_3.jpg': 'A0', 'A0_33.jpg': 'C0', 'A0_34.jpg': 'A0', 'A0_35.jpg': 'A0', 'A0_36.jpg': 'A0', 'A0_4.jpg': 'A0'}
# # # for h_col in range(1, len(head_row_list)+1):
# # # df = pd.DataFrame(data = head_row_list, index=[0])
# # # df = (df.T)
# # # print (df)
# # # df.to_excel('dict1.xlsx')
# #
# # import csv
# # with open('img_dir_results.csv', 'w', newline='') as output:
# #     writer = csv.DictWriter(output, fieldnames = head_row_list)
# #     # writer = csv.writer(output)
# #     for key, value in picture_dictionary.items():
# #         writer.writerows(picture_dictionary)
# #
# # import copy
# # dir_class = {'preclass': '', 'score': ''}
# # dir_class_dic = {}
# # dir_class_list = []
# # preclass = ['A0', 'unknown', 'A0', 'unknown', 'A0', 'A0', 'A0', 'C0', 'A0', 'A0', 'A0', 'A0', 'A0']
# # score = [0.8780811, 0, 0, 0.9600148, 0, 0, 0.94893557, 0.8978014, 0.5481093, 0.94997203, 0.9581111, 0.9068205, 0.9595386, 0.93299454]
# # for i in range(len(preclass)):
# #         dir_class_dic[i] = copy.deepcopy(dir_class)
# # for j in range(len(preclass)):
# #         dir_class_dic[j]['preclass'] = preclass[j]
# #         dir_class_dic[j]['score'] = score[j]
# # for i in range(len(preclass)):
# #         dir_class_list.append(dir_class_dic[i])
# # print(dir_class_dic[0])
# # print(dir_class_list)
# # l1 = ['b','c','d','b','c','a','a']
# # l2 = list(set(l1))
# # print(l2)
#
# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#
# # [{'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386},
# #  {'preclass': 'A0', 'score': 0.9595386}]

# -*- coding: UTF-8 –*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
QMessageBox.information(self,"消息框标题","这是一条消息。",QMessageBox.Yes | QMessageBox.No)
