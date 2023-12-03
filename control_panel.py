import sys
import time
import pythoncom
import rabi_ui
import pandas as pd
import numpy as np
import gc
import pyqtgraph as pg
from threading import Thread
from ctypes import *
from ASG8005_PythonSDK import * 
from PyQt5.QtGui import QIcon, QPixmap, QCursor, QColor
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect, QFileDialog, QDesktopWidget, QVBoxLayout

class MyWindow(rabi_ui.Ui_Form, QWidget):

    asg_info_msg = pyqtSignal(str)
    data_processing_info_msg = pyqtSignal(str)


    def __init__(self):

        super().__init__()

        # init UI
        self.setupUi(self)
        self.ui_width = int(QDesktopWidget().availableGeometry().size().width()*0.75)
        self.ui_height = int(QDesktopWidget().availableGeometry().size().height()*0.88)
        self.resize(self.ui_width, self.ui_height)
        center_pointer = QDesktopWidget().availableGeometry().center()
        x = center_pointer.x()
        y = center_pointer.y()
        old_x, old_y, width, height = self.frameGeometry().getRect()
        self.move(int(x - width / 2), int(y - height / 2))

        # set flag off and widget translucent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # set window blur
        self.render_shadow()
        
        # init window button signal
        self.window_btn_signal()

        '''
        ASG init
        '''
        self.asg_singal_init()
        self.asg_info_ui()
        self.asg_info_msg.connect(self.asg_slot)
        self.m_CountCount = 1
        


        '''
        Data processing init
        '''
        self.plot_ui_init()
        self.data_processing_signal()
        self.data_processing_info_ui()
        self._intensityData = []
        
    def data_processing_signal(self):
        self.restore_view_btn.clicked.connect(self.restore_view)
        # Message signal
        self.data_processing_info_msg.connect(self.data_processing_slot)
        # Scroll area updating signal
        self.data_processing_scroll.verticalScrollBar().rangeChanged.connect(
            lambda: self.data_processing_scroll.verticalScrollBar().setValue(
                self.data_processing_scroll.verticalScrollBar().maximum()
            )
        )
        # plot signal
        self.plot_data_btn.clicked.connect(self.plot_result)
        self.rabi_count_spbx.valueChanged.connect(self.plot_result)
        self.save_plot_data_btn.clicked.connect(self.save_plot_data)

        # clear all signal
        self.clear_repeat_count_btn.clicked.connect(self.clear_repeat_count)
    def clear_repeat_count(self):
        self.rabi_count_spbx.setValue(0)
    def save_plot_data(self):
        
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, 'Choose Data File Path', r"d:", 'CSV Files (*.csv);;All Files (*)', options=options)
        rabiStart = int(self.rabi_start_spbx.value())

        rabiStep = int(self.rabi_step_spbx.value())
        count = int(self.rabi_count_spbx.value())
        
        time_span = range(rabiStart,rabiStart+count*rabiStep,rabiStep)      

        df = pd.DataFrame({'Time': time_span, 'Intensity': self.intensity_data})
        df.to_csv(file_path, index=False, header=True)
    def plot_result(self):
        self.rabi_plot.clear()
        rabiStart = int(self.rabi_start_spbx.value())
        rabiStop = int(self.rabi_stop_spbx.value())
        rabiStep = int(self.rabi_step_spbx.value())
        count = int(self.rabi_count_spbx.value())

        time_span = range(rabiStart,rabiStart+count*rabiStep,rabiStep)
        curve = self.rabi_plot.plot(pen=pg.mkPen(color=(255,85,48), width=2))

        self.intensity_data = self._intensityData
      
        curve.setData(time_span, self.intensity_data)       
        self.intensity_data = np.array(self.intensity_data)
    def data_processing_info_ui(self):

        self.data_processing_msg.setWordWrap(True)  # 自动换行
        self.data_processing_msg.setAlignment(Qt.AlignTop)  # 靠上

        # # 用于存放消息
        self.data_processing_msg_history = []

    def data_processing_slot(self, msg):

        # print(msg)
        self.data_processing_msg_history.append(msg)
        self.data_processing_msg.setText("<br>".join(self.data_processing_msg_history))
        self.data_processing_msg.resize(700, self.data_processing_msg.frameSize().height() + 20)
        self.data_processing_msg.repaint()  # 更新内容，如果不更新可能没有显示新内容
        
    def restore_view(self):
        # self.data_processing_info_msg.emit('View restored')
        self.rabi_plot.getPlotItem().enableAutoRange()

    def plot_ui_init(self):

        # Add pyqtGraph plot widget        
        self.rabi_plot = pg.PlotWidget(enableAutoRange=True)
        graph_widget_layout = QVBoxLayout()
        graph_widget_layout.addWidget(self.rabi_plot)
        self.graph_frame.setLayout(graph_widget_layout)
        self.rabi_plot.setLabel("left","Intensity (Counts)")
        self.rabi_plot.setLabel("bottom","Time (ns)")
        self.rabi_plot.setTitle('Rabi', color='k')
        self.rabi_plot.setBackground(background=None)
        self.rabi_plot.getAxis('left').setPen('k')
        self.rabi_plot.getAxis('left').setTextPen('k')
        self.rabi_plot.getAxis('bottom').setPen('k')
        self.rabi_plot.getAxis('bottom').setTextPen('k')
        self.rabi_plot.getAxis('top').setPen('k')
        self.rabi_plot.getAxis('right').setPen('k')
        self.rabi_plot.showAxes(True)
        self.rabi_plot.showGrid(x=True, y=True)

    def asg_singal_init(self):
        self.asg_connect_btn.clicked.connect(self.asg_connect)  
        self.asg_close_btn.clicked.connect(self.asg_close) 
        # ASG scroll area scrollbar signal
        self.asg_scroll.verticalScrollBar().rangeChanged.connect(
            lambda: self.asg_scroll.verticalScrollBar().setValue(
                self.asg_scroll.verticalScrollBar().maximum()
            )
        )
        # self.mw_time_spbx.editingFinished.connect(self.acq_time_calc)
        self.asg_set_btn.clicked.connect(self.set_pulse_and_count)
        self.asg_start_btn.clicked.connect(self.asg_start)
        self.asg_stop_btn.clicked.connect(self.asg_stop)
    def asg_stop(self):
        rtn = self.asg.stop()
        if rtn == 1:
            self.asg_info_msg.emit('Stop success: {}'.format(rtn))
        self.__stopConstant = True
    def asg_start(self):
        rtn = self.asg.start()
        if rtn == 1:
            self.asg_info_msg.emit('Start success: {}'.format(rtn))
        time.sleep(1)
        # print(len(self.rabi_data))
        # print(self.rabi_data)
        # Start daq in thread
        thread = Thread(
            target=self.count_data_thread_func
        )
        thread.start()
    def set_pulse_and_count(self):
        
        rabiStart = int(self.rabi_start_spbx.value())
        
        rabiStop = int(self.rabi_stop_spbx.value())
        rabiStep = int(self.rabi_step_spbx.value())
        
        num_points = int((rabiStop-rabiStart)/rabiStep)+1
        count = int(self.current_rabi_time_spbx.value())

        mw_time = rabiStart + count*rabiStep

        init_time = int(self.init_time_spbx.value())*1000
        acq_time = int(self.acq_time_spbx.value())
        fore_time = int(self.fore_time_spbx.value())
        back_time = int(self.back_time_spbx.value())
        laser_diff = int(self.laser_diff_time_spbx.value)
        self.rabi_data = []
        #ASG
        ch1 = [init_time, fore_time+mw_time+back_time, acq_time, laser_diff+20]
        ch2 = [0, init_time+fore_time, mw_time, back_time+laser_diff+acq_time+20]
        count = [20, init_time+fore_time+mw_time+back_time+laser_diff-20, acq_time, 20]


        # print(sum(ch1))
        # print(sum(ch2))
        # print(sum(count))
        # print(ch1)
        # print(ch2)
        ch3 = [0,0]
        ch4 = [0,0]
        ch5 = [0,0]
        ch6 = [0,0]
        ch7 = [0,0]
        ch8 = [0,0]

        asg_data = [ch1,
                ch2,
                ch3,
                ch4,
                ch5,
                ch6,
                ch7,
                ch8
                ]
        self.asg_info_msg.emit('CH1: '+ str(ch1))
        self.asg_info_msg.emit('CH2: '+ str(ch2))
        self.asg_info_msg.emit('CH1 SUM: ' + str(sum(ch1)))
        self.asg_info_msg.emit('CH2 SUM: ' + str(sum(ch2)))
        self.asg_info_msg.emit('CH1 LEN: ' + str(len(ch1)))
        self.asg_info_msg.emit('CH2 LEN: ' + str(len(ch2)))
        # print(len(ch1))
        # print(len(ch2))
        # print(ch1)
        # print(ch2)
        # print(count)
        asg_length = [len(seq) for seq in asg_data]
        rtn = self.asg.download_ASG_pulse_data(asg_data, asg_length)
        if rtn == 1:
            self.asg_info_msg.emit('ASG pulse data download success: {}'.format(rtn))
        #配置asg和count功能 有两个参数第一个是开启count功能，第二个是开启asg功能，第二个默认asg全开
        rtn = self.asg.ASG_countConfig(1)
        if rtn == 1:
            self.asg_info_msg.emit('Count configured: {}'.format(rtn))

        # Download count data
        count_data = count
        self.asg_info_msg.emit('Count: ' + str(count_data))
        self.asg_info_msg.emit('Count SUM: ' + str(sum(count_data)))
        length_count=len(count_data)
        self.m_CountCount = length_count/2
        rtn = self.asg.ASG_counter_download(count_data,length_count)
        if rtn == 1:
            self.asg_info_msg.emit('Count data download success: {}'.format(rtn))
        
        
    def count_data_thread_func(self):
        pythoncom.CoInitialize()
        rabiStart = int(self.rabi_start_spbx.value())
        rabiStop = int(self.rabi_stop_spbx.value())
        rabiStep = int(self.rabi_step_spbx.value())
        
        num_points = int((rabiStop-rabiStart)/rabiStep)+1
        time_span = np.arrange(rabiStart,rabiStop+rabiStep,rabiStep)
        
        repeat_num = int(self.repeat_spbx.value())
        rabi_count = int(self.rabi_count_spbx.value())
        while True:
            # print(1)
            rabi_data = self.rabi_data #防止在给i_count赋值的时候self.rabi_data变了

            if len(rabi_data) >= repeat_num:     
                sum = sum(rabi_data[0, repeat_num])    
                self._intensityData.append(sum)       

                self.current_rabi_time_spbx.setValue(rabi_count+1)
                del rabi_data, self.rabi_data, sum
                gc.collect()
                self.asg_stop()
                break
            time.sleep(0.5)
        pythoncom.CoUninitialize()
    
    def asg_connect(self):
        #实例化asg对象
        self.asg = ASG8005()

        #设置回调函数
        status_callback_type = CFUNCTYPE(None, c_int, c_char_p)
        self.status_callback_func = status_callback_type(self.status_callback)

        self.asg.set_callback(self.status_callback_func)
        count_callback_type = CFUNCTYPE(None, c_int, c_int, POINTER(c_uint32))
        self.count_callback_func = count_callback_type(self.count_callback)
        self.asg.set_callback_count(self.count_callback_func)
        
        rtn = self.asg.connect()
        if rtn == 1:
            self.asg_info_msg.emit('Connection success: {}'.format(rtn))
    def asg_close(self):
        rtn = self.asg.close_device()
        if rtn == 1:
            self.asg_info_msg.emit('Close success: {}'.format(rtn))
    def asg_info_ui(self):

        self.asg_msg.setWordWrap(True)  # 自动换行
        self.asg_msg.setAlignment(Qt.AlignTop)  # 靠上
        self.asg_msg_history = []

    def asg_slot(self, msg):

        # print(msg)
        self.asg_msg_history.append(msg)
        self.asg_msg.setText("<br>".join(self.asg_msg_history))
        self.asg_msg.resize(700, self.asg_msg.frameSize().height() + 20)
        self.asg_msg.repaint()  # 更新内容，如果不更新可能没有显示新内容


    def status_callback(self, type, c_char_buff): 
        self.asg_info_msg.emit(str(type))
        self.asg_info_msg.emit(str(c_char_buff))
        return

    def count_callback(self, type, len, c_int_buff): 
        datList = [] 
        for i in range(len): 
            datList.append(c_int_buff[i]) 
        typestr:str 
        if type == 0: 
            if self.m_CountCount != len: 
                self.asg_info_msg.emit("数据错误") 
            typestr = 'count 计数：' 
        elif type == 3: 
            typestr = '连续计数 : ' 
        # self.asg_info_msg.emit(typestr + "datList :" + str(datList)) 
        # print(typestr + "datList :" + str(datList))
        self.rabi_data.append(datList[1])
        
        

        return
    '''Set window ui'''
    def window_btn_signal(self):
        # window button sigmal
        self.close_btn.clicked.connect(self.close)
        self.max_btn.clicked.connect(self.maxornorm)
        self.min_btn.clicked.connect(self.showMinimized)
        
    #create window blur
    def render_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)  # 偏移
        self.shadow.setBlurRadius(30)  # 阴影半径
        self.shadow.setColor(QColor(128, 128, 255))  # 阴影颜色
        self.mainwidget.setGraphicsEffect(self.shadow)  # 将设置套用到widget窗口中

    def maxornorm(self):
        if self.isMaximized():
            self.showNormal()
            self.norm_icon = QIcon()
            self.norm_icon.addPixmap(QPixmap(":/my_icons/images/icons/max.svg"), QIcon.Normal, QIcon.Off)
            self.max_btn.setIcon(self.norm_icon)
        else:
            self.showMaximized()
            self.max_icon = QIcon()
            self.max_icon.addPixmap(QPixmap(":/my_icons/images/icons/norm.svg"), QIcon.Normal, QIcon.Off)
            self.max_btn.setIcon(self.max_icon)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QPoint
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        
    def mouseMoveEvent(self, QMouseEvent):
        m_position = QPoint
        m_position = QMouseEvent.globalPos() - self.pos()
        width = QDesktopWidget().availableGeometry().size().width()
        height = QDesktopWidget().availableGeometry().size().height()
        if m_position.x() < width*0.7 and m_position.y() < height*0.06:
            self.m_flag = True
            if Qt.LeftButton and self.m_flag:                
                pos_x = int(self.m_Position.x())
                pos_y = int(self.m_Position.y())
                if pos_x < width*0.7 and pos_y < height*0.06:           
                    self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                    QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
