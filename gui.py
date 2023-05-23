# -*- coding: UTF-8 –*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
from PIL import Image
import numpy as np
import shutil
from yolo import YOLO
import time
from numpy import *


class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle('药物-靶标结合亲和力预测')
        self.to_predict_name = "img/oringinal.png"
        self.result_name  = "img/result.png"
        self.class_names_dic = {
            'A0': "包", 'A1': "除草器容器", 'A2': "茶叶渣", 'A3': "贝壳",
            'B0': "玻璃瓶罐", 'B1': "电池+干电池", 'B2': "大骨头", 'B3': "化妆品瓶",
            'C0': "插头电线", 'C1': "废弃水银温度计", 'C2': "蛋壳", 'C3': "破碎花盆及碗碟",
            'D0': "充电宝", 'D1': "软膏", 'D2': "果壳瓜皮+水果果皮+水果果肉", 'D3': "卫生纸",
            'E0': "锅", 'E1': "杀虫剂容器", 'E2': "西餐糕点", 'E3': "污损塑料",
            'F0': "金属食品罐", 'F2': "鱼骨", 'F3': "牙签",
            'G0': "快递纸袋", 'G3': "烟蒂",
            'H0': "毛绒玩具", 'H3': "一次性餐具",
            'I0': "牛奶盒等利乐包装",'I3': "纸杯",
            'J0': "泡沫塑料",
            'K0': "皮鞋",
            'L0': "塑料玩具+塑料碗盆+塑料衣架",
            'M0': "调料瓶",
            'N0': "洗发水瓶",
            'O0': "易拉罐",
            'P0': "饮料瓶",
            'Q0': "砧板",
            'R0': "纸板箱"}
        self.big_class = {'0': "可回收垃圾", '1': "有害垃圾", '2': "厨余垃圾", '3': "其他垃圾"}
        self.resize(1500, 700)
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()  # 水平布局
        font = QFont('楷体', 15)

        pic_widget = QWidget()
        pic_layout = QHBoxLayout()
        pic_widget.resize(900, 600)
        print(pic_widget.size())

        left_widget_oringinal = QWidget()
        left_layout_oringinal = QVBoxLayout()  # 垂直布局
        img_title_oringinal = QLabel("原图")
        img_title_oringinal.setFont(font)
        img_title_oringinal.setAlignment(Qt.AlignCenter)
        self.img_label_oringinal = QLabel()
        img_init_oringinal = cv2.imread(self.to_predict_name)
        print(img_init_oringinal.shape)
        h, w, c = img_init_oringinal.shape
        scale = 400 / h
        img_show_oringinal = cv2.resize(img_init_oringinal, (0, 0), fx=scale, fy=scale)
        cv2.imwrite("img/show_oringinal.png", img_show_oringinal)
        img_init_oringinal = cv2.resize(img_init_oringinal, (500, 500))
        print(img_init_oringinal.shape)
        cv2.imwrite('img/target_oringinal.png', img_init_oringinal)
        print(img_init_oringinal.shape)
        self.img_label_oringinal.setPixmap(QPixmap("img/target_oringinal.png"))
        left_layout_oringinal.addWidget(img_title_oringinal)
        left_layout_oringinal.addWidget(self.img_label_oringinal, 1, Qt.AlignLeft)
        left_widget_oringinal.setLayout(left_layout_oringinal)


        left_widget_result = QWidget()
        left_layout_result = QVBoxLayout()  # 垂直布局
        img_title_result = QLabel("结果图")
        img_title_result.setFont(font)
        img_title_result.setAlignment(Qt.AlignCenter)
        self.img_label_result = QLabel()
        img_init_result = cv2.imread(self.result_name)
        h, w, c = img_init_result.shape
        scale = 400 / h
        img_show_result = cv2.resize(img_init_result, (0, 0), fx=scale, fy=scale)
        cv2.imwrite("img/show_result.png", img_show_result)
        img_init_result = cv2.resize(img_init_result, (500, 500))
        cv2.imwrite('img/target_result.png', img_init_result)
        self.img_label_result.setPixmap(QPixmap("img/target_result.png"))
        left_layout_result.addWidget(img_title_result)
        left_layout_result.addWidget(self.img_label_result, 1, Qt.AlignRight)
        left_widget_result.setLayout(left_layout_result)

        right_widget = QWidget()
        right_layout = QVBoxLayout()
        btn_change = QPushButton(" 上传图片 ")
        btn_change.clicked.connect(self.change_img)
        btn_change.setFont(font)
        btn_predict = QPushButton(" 开始识别 ")
        print(btn_predict)
        btn_predict.setFont(font)
        btn_predict.clicked.connect(self.predict_img)
        btn_predict_dir = QPushButton(" 批量识别图片 ")
        btn_predict_dir.setFont(font)
        btn_predict_dir.clicked.connect(self.predict_img_dir)


        label_result = QLabel(' 垃圾种类 ')
        self.result = QLabel("等待识别")
        label_result.setFont(QFont('楷体', 16))
        self.result.setFont(QFont('楷体', 24))

        label_result_f = QLabel(' 物品名称 ')
        self.result_f = QLabel("等待识别")

        self.label_info = QTextEdit()
        self.label_info.setFont(QFont('楷体', 12))

        label_result_f.setFont(QFont('楷体', 16))
        self.result_f.setFont(QFont('楷体', 24))

        right_layout.addStretch(2)
        right_layout.addWidget(label_result, 0, Qt.AlignCenter)
        right_layout.addStretch(2)
        right_layout.addWidget(self.result, 0, Qt.AlignCenter)
        right_layout.addStretch(2)
        right_layout.addWidget(label_result_f, 0, Qt.AlignCenter)
        right_layout.addStretch(2)
        right_layout.addWidget(self.result_f, 0, Qt.AlignCenter)
        right_layout.addStretch(2)
        right_layout.addWidget(self.label_info, 0, Qt.AlignCenter)
        right_layout.addStretch(2)
        right_layout.addWidget(btn_change)
        right_layout.addWidget(btn_predict)
        right_layout.addWidget(btn_predict_dir)
        right_layout.addStretch(2)
        right_widget.setLayout(right_layout)

        video_widget = QWidget()
        video_layout = QVBoxLayout()
        video_title = QLabel('欢迎使用视频检测功能!')
        video_title.setFont(QFont('楷体', 18))
        video_title.setAlignment(Qt.AlignCenter)
        video_detect_widget = QWidget()
        video_detect_layout = QHBoxLayout()
        btn_predict_video = QPushButton(" 视频检测 ")
        btn_predict_video.setFont(font)
        btn_predict_video.clicked.connect(self.predict_img_video)
        btn_predict_camera = QPushButton(" 摄像头监测 ")
        btn_predict_camera.setFont(font)
        btn_predict_camera.clicked.connect(self.predict_img_camera)
        video_detect_layout.addWidget(btn_predict_video)
        video_detect_layout.addWidget(btn_predict_camera)
        video_detect_widget.setLayout(video_detect_layout)
        video_layout.addWidget(video_title)
        video_layout.addWidget(video_detect_widget)
        video_widget.setLayout(video_layout)

        pic_layout.addWidget(left_widget_oringinal)
        pic_layout.addWidget(left_widget_result)
        pic_widget.setLayout(pic_layout)
        main_layout.addWidget(pic_widget)
        main_layout.addWidget(right_widget)
        main_widget.setLayout(main_layout)
        self.addTab(main_widget, '主页')
        self.addTab(video_widget, '视频检测功能')
        self.setTabIcon(0, QIcon('img/主页面.png'))
        self.setTabIcon(1, QIcon('img/关于.png'))

    # 上传图片
    def change_img(self):
        openfile_name = QFileDialog.getOpenFileName(self, 'chose files', '', 'Image files(*.jpg *.png *.bmp *.dib *.png *.jpg *.jpeg *.pbm *.pgm *.ppm *.tif *.tiff)')
        img_name = openfile_name[0]
        if img_name == '':
            pass
        else:
            target_image_name = "img/tmp_single." + img_name.split(".")[-1]
            print(target_image_name)
            shutil.copy(img_name, target_image_name)
            self.to_predict_name = target_image_name

            img_init_oringinal = cv2.imread(self.to_predict_name)
            h, w, c = img_init_oringinal.shape
            scale = 400 / h
            img_show_oringinal = cv2.resize(img_init_oringinal, (0, 0), fx=scale, fy=scale)
            cv2.imwrite("img/show.png", img_show_oringinal)
            img_init_oringinal = cv2.resize(img_init_oringinal, (500, 500))
            cv2.imwrite('img/target.png', img_init_oringinal)
            self.img_label_oringinal.setPixmap(QPixmap("img/target.png"))
    # 预测图片
    def predict_img(self):
        crop = False
        while True:
            img = 'img/target.png'
            try:
                image = Image.open(img)
            except:
                print('Open Error! Try again!')
                continue
            else:
                r_image, predicted_class, score, top, left, bottom, right = yolo.detect_image(image, self.class_names_dic, crop=crop)
                break
        r_image.save("./img_out/result.jpg")
        if predicted_class in self.class_names_dic:
            small_class_name = self.class_names_dic[predicted_class]
            big_class = predicted_class[-1]
            big_class_name = self.big_class[big_class]
        else:
            small_class_name = "识别失败，请重新摆放！"
            big_class_name = "识别失败，请重新摆放！"
        if big_class_name == "厨余垃圾":
            self.label_info.setText(
                "厨余垃圾是指居民日常生活及食品加工、饮食服务、单位供餐等活动中产生的垃圾，包括丢弃不用的菜叶、剩菜、剩饭、果皮、蛋壳、茶渣、骨头等。由于厨余垃圾含有极高的水分与有机物，很容易腐坏，产生恶臭。经过妥善处理和加工，可转化为新的资源，高有机物含量的特点使其经过严格处理后可作为肥料、饲料，也可产生沼气用作燃料或发电，油脂部分则可用于制备生物燃料。")
        elif big_class_name == "有害垃圾":
            self.label_info.setText(
                "有害垃圾指对人体健康或者自然环境造成直接或者潜在危害的生活废弃物。常见的有害垃圾包括废灯管、废油漆、杀虫剂、废弃化妆品、过期药品、废电池、废灯泡、废水银温度计等，有害垃圾需按照特殊正确的方法安全处理，一般需要经过特殊的处理之后才可以进行焚烧，堆肥，填埋处理")
        elif big_class_name == "可回收垃圾":
            self.label_info.setText(
                " 根据《城市生活垃圾分类及其评价标准》行业标准以及参考德国垃圾分类法，可回收物是指适宜回收循环使用和资源利用的废物。主要包括：纸类，塑料，金属，玻璃，织物等。主要的处理方式有：1.垃圾再生法；2.垃圾焚烧法；3.垃圾堆肥法；4.垃圾生物降解法。")
        elif big_class_name == "其他垃圾":
            self.label_info.setText(
                "其他垃圾指危害比较小，没有再次利用的价值的垃圾，其他垃圾包括砖瓦陶瓷、渣土、卫生间废纸、瓷器碎片、动物排泄物、一次性用品等难以回收的废弃物。一般都采取填埋、焚烧、卫生分解等方法处理，部分还可以使用生物分解的方法解决")
        else:
            self.label_info.setText(
                "识别垃圾失败，请将物品重新摆放！")
        self.result.setText(big_class_name)
        self.result_f.setText(small_class_name)
        img_init_result = cv2.imread("img_out/result.jpg")
        h, w, c = img_init_result.shape
        scale = 400 / h
        img_show_result = cv2.resize(img_init_result, (0, 0), fx=scale, fy=scale)
        cv2.imwrite("img_out/show.png", img_show_result)
        img_init_result = cv2.resize(img_init_result, (400, 400))
        cv2.imwrite('img_out/result.png', img_init_result)
        self.img_label_result.setPixmap(QPixmap("img_out/result.jpg"))

    def predict_img_dir(self):
        import os
        from tqdm import tqdm
        predicted_class = [ ]
        score_dir = [ ]
        top_dir = []
        left_dir = []
        bottom_dir = []
        right_dir = []
        openfile_name = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        dir_origin_path = openfile_name
        dir_save_path = "img_out/"
        if openfile_name == '':
            pass
        else:
            img_names = os.listdir(dir_origin_path)
            for img_name in tqdm(img_names, desc="Processing Rubbish Picture", total=len(img_names), ncols=100, position=0):
                if img_name.lower().endswith(
                        ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                    image_path = os.path.join(dir_origin_path, img_name)
                    image = Image.open(image_path)
                    r_image, predicted_class, is_rubbish, score, top, left, bottom, right = yolo.detect_image_dir(image, predicted_class, self.class_names_dic)
                    score_dir.append(score)
                    top_dir.append(top)
                    left_dir.append(left)
                    bottom_dir.append(bottom)
                    right_dir.append(right)
                    if is_rubbish == 0:
                        score_dir.append(score)
                        top_dir.append(top)
                        left_dir.append(left)
                        bottom_dir.append(bottom)
                        right_dir.append(right)
                        predicted_class.append('unknown')
                    if not os.path.exists(dir_save_path):
                        os.makedirs(dir_save_path)
                    r_image.save(os.path.join(dir_save_path, img_name.replace(".jpg", ".png")), quality=95, subsampling=0)
            print("文件夹图片处理完成!")
            import copy
            dir_class = {'picture_name': '', 'predicted_class': '', 'score': '', 'top': '', 'left': '', 'bottom': '', 'right': ''}
            dir_class_dic = {}
            dir_class_list = []
            for i in range(len(img_names)):
                dir_class_dic[i] = copy.deepcopy(dir_class)
            for j in range(len(img_names)):
                dir_class_dic[j]['picture_name'] = img_names[j]
                dir_class_dic[j]['predicted_class'] = self.class_names_dic[predicted_class[j]]
                dir_class_dic[j]['score'] = score_dir[j]
                dir_class_dic[j]['top'] = top_dir[j]
                dir_class_dic[j]['left'] = left_dir[j]
                dir_class_dic[j]['bottom'] = bottom_dir[j]
                dir_class_dic[j]['right'] = right_dir[j]
            for i in range(len(img_names)):
                dir_class_list.append(dir_class_dic[i])
            dir_class_along = list(set(predicted_class))
            for i in range(len(dir_class_along)):
                score_dir_small_class = []
                for j in range(len(dir_class_list)):
                    if dir_class_list[j]['predicted_class'] == self.class_names_dic[dir_class_along[i]]:
                        score_dir_small_class.append(dir_class_list[j]['score'])
                print("共有{}类垃圾图片共{}张, 检测得分均值为:{}".format(self.class_names_dic[dir_class_along[i]], len(score_dir_small_class), mean(score_dir_small_class)))
            openfile_name_result = QFileDialog.getExistingDirectory(self, '选择保存文件夹', './')
            if openfile_name_result == '':
                pass
            else:
                openfile_name = openfile_name.split('/')[-1] + '.csv'
                image_path = os.path.join(openfile_name_result, openfile_name)
                import csv
                header = ['picture_name', 'predicted_class', 'score', 'top', 'left', 'bottom', 'right']
                with open(image_path, 'w', newline='', encoding='utf-8-sig') as f:
                    writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
                    writer.writeheader()  # 写入列名
                    writer.writerows(dir_class_list)  # 写入数据
                    print("写入已完成")

    def predict_img_video(self):
        import os
        video_path = QFileDialog.getOpenFileName(self, 'chose files', './', 'Video files(*.avi *.wmv *.mov *.mp4)')
        video_name = video_path[0]
        if video_name == '':
            pass
        else:
            video_name_save = video_path[0].split('/')
            video_name_save = video_name_save[-1].split('.')
            video_save_path = "./video_out"
            video_save_path = os.path.join(video_save_path, video_name_save[0] + '.avi')
            video_fps = 50
            capture = cv2.VideoCapture(video_name)
            ref, frame = capture.read()
            if not ref:
                raise ValueError("未能正确读取视频，请注意是否正确填写视频路径。")
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)
            fps = 1.0
            while (True):
                t1 = time.time()
                # 读取某一帧
                ref, frame = capture.read()
                out.write(frame)
                if not ref:
                    break
                # 格式转变，BGRtoRGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 转变成Image
                frame = Image.fromarray(np.uint8(frame))
                # 进行检测
                frame = np.array(yolo.detect_image_video(frame, self.class_names_dic))
                # RGBtoBGR满足opencv显示格式
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                fps = (fps + (1. / ((time.time() - t1))) / 2)
                frame = cv2.putText(frame, "Press Q to save and quit", (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("video", frame)
                out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    capture.release()
                    out.release()
                    break
            print("Video Detection Done!")
            capture.release()
            out.release()
            print("Saved done!")
            cv2.destroyAllWindows()

    def predict_img_camera(self):
        import os
        video_path = 0
        video_save_path = "./video_out"
        video_name_save = "camera"
        video_save_path = os.path.join(video_save_path, video_name_save + '.avi')
        video_fps = 50
        capture = cv2.VideoCapture(video_path)
        ref, frame = capture.read()
        if not ref:
            raise ValueError("未能正确读取摄像头，请注意是否正确安装摄像头。")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)
        fps = 1.0
        while (True):
            t1 = time.time()
            # 读取某一帧
            ref, frame = capture.read()
            out.write(frame)
            if not ref:
                break
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
            # 进行检测
            frame = np.array(yolo.detect_image_video(frame, self.class_names_dic))
            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            fps = (fps + (1. / (time.time() - t1))) / 2
            frame = cv2.putText(frame, "Press Q to save and quit", (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("video", frame)
            out.write(frame)
            if cv2.waitKey(0.1) & 0xFF == ord('q'):
                capture.release()
                out.release()
                break
        print("Video Detection Done!")
        capture.release()
        out.release()
        print("Saved done!")
        cv2.destroyAllWindows()
    # 窗口关闭事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     '退出',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    yolo = YOLO()
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()
    sys.exit(app.exec_())
