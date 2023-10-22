import sys
import time

import pythoncom
import pyvisa
import asg_cw_odmr_ui
import pandas as pd
import numpy as np
import pyqtgraph as pg
from threading import Thread
from ctypes import *
from ASG8005_PythonSDK import * 
from PyQt5.QtGui import QIcon, QPixmap, QCursor, QColor
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect, QFileDialog, QDesktopWidget, QVBoxLayout

class MyWindow(asg_cw_odmr_ui.Ui_Form, QWidget):

    rf_info_msg = pyqtSignal(str)
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
        RF init
        '''
        # Init RF combobox ui
        self.rf_cbx_test()
        
        # Init RF setup info ui
        self.rf_info_ui()

        # Init RF signal
        self.my_rf_signal()

        '''
        ASG init
        '''
        self.asg_singal_init()
        self.asg_info_ui()
        self.asg_info_msg.connect(self.asg_slot)
        self.m_CountCount = 1
        self.cw_odmr_data = []
        


        '''
        Data processing init
        '''
        self.plot_ui_init()
        self.data_processing_signal()
        self.data_processing_info_ui()
        
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
        self.repeat_count_num.valueChanged.connect(self.plot_result)
        self.save_plot_data_btn.clicked.connect(self.save_plot_data)
        # clear all signal
        self.clear_repeat_count_btn.clicked.connect(self.clear_repeat_count)
    def clear_all(self):
        self.repeat_count_num.setValue(0)
    def save_plot_data(self):
        
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, 'Choose Data File Path', r"d:", 'CSV Files (*.csv);;All Files (*)', options=options)
        startFreq = int(self.start_freq_spbx.value())
        stopFreq = int(self.stop_freq_spbx.value())
        stepFreq = int(self.step_freq_spbx.value())
        intensity_data = self.intensity_data
        
        frequency_data = range(startFreq,stopFreq+stepFreq,stepFreq)
        df = pd.DataFrame({'Frequency': frequency_data, 'Intensity': intensity_data})
        df.to_csv(file_path, index=False, header=True)
    def plot_result(self):
        self.cw_odmr_plot.clear()
        startFreq = int(self.start_freq_spbx.value())
        stopFreq = int(self.stop_freq_spbx.value())
        stepFreq = int(self.step_freq_spbx.value())
        num_points = int((stopFreq - startFreq)/stepFreq) + 1
        freq_data = range(startFreq,stopFreq+stepFreq,stepFreq)
        curve = self.cw_odmr_plot.plot(pen=pg.mkPen(color=(255,85,48), width=2))
        
        self.intensity_data += np.array(self.cw_odmr_data[0:num_points])
        self.intensity_data = list(self.intensity_data)
        
        curve.setData(freq_data, self.intensity_data)       
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
        self.cw_odmr_plot.getPlotItem().enableAutoRange()

    def plot_ui_init(self):

        # Add pyqtGraph plot widget        
        self.cw_odmr_plot = pg.PlotWidget(enableAutoRange=True)
        graph_widget_layout = QVBoxLayout()
        graph_widget_layout.addWidget(self.cw_odmr_plot)
        self.graph_frame.setLayout(graph_widget_layout)
        self.cw_odmr_plot.setLabel("left","Intensity (Counts)")
        self.cw_odmr_plot.setLabel("bottom","RF Frequency (MHz)")
        self.cw_odmr_plot.setTitle('CW-ODMR', color='k')
        self.cw_odmr_plot.setBackground(background=None)
        self.cw_odmr_plot.getAxis('left').setPen('k')
        self.cw_odmr_plot.getAxis('left').setTextPen('k')
        self.cw_odmr_plot.getAxis('bottom').setPen('k')
        self.cw_odmr_plot.getAxis('bottom').setTextPen('k')
        self.cw_odmr_plot.getAxis('top').setPen('k')
        self.cw_odmr_plot.getAxis('right').setPen('k')
        self.cw_odmr_plot.showAxes(True)
        self.cw_odmr_plot.showGrid(x=True, y=True)

    def asg_singal_init(self):
        self.asg_connect_btn.clicked.connect(self.asg_connect)  
        self.asg_close_btn.clicked.connect(self.asg_close) 
        # ASG scroll area scrollbar signal
        self.asg_scroll.verticalScrollBar().rangeChanged.connect(
            lambda: self.asg_scroll.verticalScrollBar().setValue(
                self.asg_scroll.verticalScrollBar().maximum()
            )
        )
        self.mw_time_spbx.editingFinished.connect(self.acq_time_calc)
        self.asg_set_btn.clicked.connect(self.set_pulse_and_count)
        self.asg_start_btn.clicked.connect(self.asg_start)
        self.asg_stop_btn.clicked.connect(self.asg_stop)
    def asg_stop(self):
        rtn = self.asg.stop()
        if rtn == 1:
            self.asg_info_msg.emit('Stop success: {}'.format(rtn))
        self.__stopConstant = True
        self.cw_odmr_data = []
    def asg_start(self):
        rtn = self.asg.start()
        if rtn == 1:
            self.asg_info_msg.emit('Start success: {}'.format(rtn))
        # Start daq in thread
        thread = Thread(
            target=self.count_data_thread_func
        )
        thread.start()
    def set_pulse_and_count(self):
        # dwell_time = int(self.dwell_time_spbx.value())
        mw_time = int(self.mw_time_spbx.value())*1000000
        acq_time = int(self.acq_time_spbx.value())*1000000
        #ASG
        ch1 = [0,20+10000000+mw_time+20,1000,20]
        ch2 = [0, 20+10000000, mw_time, 1000+20+20]
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
        asg_length = [len(seq) for seq in asg_data]
        rtn = self.asg.download_ASG_pulse_data(asg_data, asg_length)
        if rtn == 1:
            self.asg_info_msg.emit('ASG pulse data download success: {}'.format(rtn))
        #配置asg和count功能 有两个参数第一个是开启count功能，第二个是开启asg功能，第二个默认asg全开
        rtn = self.asg.ASG_countConfig(1)
        if rtn == 1:
            self.asg_info_msg.emit('Count configured: {}'.format(rtn))

        # Download count data
        count_data = [20,10000000, mw_time, 1000+20+20]
        self.asg_info_msg.emit('Count: ' + str(count_data))
        self.asg_info_msg.emit('Count SUM: ' + str(sum(count_data)))
        length_count=len(count_data)
        self.m_CountCount = length_count/2
        rtn = self.asg.ASG_counter_download(count_data,length_count)
        if rtn == 1:
            self.asg_info_msg.emit('Count data download success: {}'.format(rtn))
        
        startFreq = int(self.start_freq_spbx.value())
        stopFreq = int(self.stop_freq_spbx.value())
        stepFreq = int(self.step_freq_spbx.value())
        num_points = int((stopFreq - startFreq)/stepFreq) + 1
        self.intensity_data = np.zeros(num_points)
    def count_data_thread_func(self):
        pythoncom.CoInitialize()
        startFreq = int(self.start_freq_spbx.value())
        stopFreq = int(self.stop_freq_spbx.value())
        stepFreq = int(self.step_freq_spbx.value())

        num_points = int((stopFreq - startFreq)/stepFreq) + 1 
        repeat_num = int(self.repeat_spbx.value())
        i_count = int(self.repeat_count_num.value())
        
        self.__stopConstant = False
        while True:
            print(1)
            
            if self.__stopConstant == True:
                break
            if 1 == (len(self.cw_odmr_data) // num_points):                
                self.repeat_count_num.setValue(i_count+1)
            if i_count >= repeat_num:
                break
            time.sleep(1)
        pythoncom.CoUninitialize()
    
    def acq_time_calc(self):
        dwell_time = int(self.dwell_time_spbx.value())
        mw_time = int(self.mw_time_spbx.value())
        acq_time = mw_time
        if mw_time > 0 and mw_time <= dwell_time:
            self.acq_time_spbx.setValue(acq_time)
        else:
            self.asg_info_msg.emit('MWTime should be smaller than DwellTime')
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
        self.cw_odmr_data.append(datList[1])

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

    '''
    RF CONTROL
    '''
    def rf_info_ui(self):

        self.rf_msg.setWordWrap(True)  # 自动换行
        self.rf_msg.setAlignment(Qt.AlignTop)  # 靠上
        self.rf_msg_history = []

    def rf_slot(self, msg):

        # print(msg)
        self.rf_msg_history.append(msg)
        self.rf_msg.setText("<br>".join(self.rf_msg_history))
        self.rf_msg.resize(700, self.rf_msg.frameSize().height() + 20)
        self.rf_msg.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def my_rf_signal(self):

        #open button signal
        self.rf_connect_btn.clicked.connect(self.boot_rf)

        #message signal
        self.rf_info_msg.connect(self.rf_slot)

        # RF scroll area scrollbar signal
        self.rf_scroll.verticalScrollBar().rangeChanged.connect(
            lambda: self.rf_scroll.verticalScrollBar().setValue(
                self.rf_scroll.verticalScrollBar().maximum()
            )
        )

        # combobox restore signal
        self.rf_visa_rst_btn.clicked.connect(self.rf_cbx_test)

        # RF load sample button signal
        self.rf_load_btn.clicked.connect(self.rf_spl_ld)

        # RF On button signal
        self.rf_ply_stp_btn.clicked.connect(self.rf_ply_stp)

    def rf_cbx_test(self):
        
        self.rf_cbx.clear()
        self.rm = pyvisa.ResourceManager()
        self.ls = self.rm.list_resources()
        self.rf_cbx.addItems(self.ls)

    def boot_rf(self):
        
        # Boot RF generator
        self.rf_port = self.rf_cbx.currentText()
        # print(self.rf_port)
        self.my_instrument = self.rm.open_resource(self.rf_port)
        self.my_instrument.write_termination = '\n'
        self.instrument_info = self.my_instrument.query('*IDN?')
        
        # 恢复出厂设置
        self.fac = self.my_instrument.write(':SYST:PRES:TYPE FAC')
        
        self.preset = self.my_instrument.write(':SYST:PRES')
        
        if self.fac != 0 and self.preset != 0:
            self.rf_info_msg.emit('Restored factory settings succeeded: {}, {}'.format(self.fac, self.preset))
        else:
            self.rf_info_msg.emit('Restoring factory settings failed')
            sys.emit()

        self.rf_info_msg.emit(self.instrument_info)
        
        '''
        This part defines some initial settings of RF generator suited to CW-ODMR measurement
        '''
        # time.sleep(5)

        # setting sweep type to list
        sweep_type = self.my_instrument.write(":SWE:TYPE LIST")
        if sweep_type != 0:
            self.rf_info_msg.emit('Setting sweep type to "LIST" succeeded: {}'.format(sweep_type))
        else:
            self.rf_info_msg.emit('Setting sweep type "LIST" failed')
            sys.emit()

        # setting file type to sweep csv
        file_type = self.my_instrument.write(":MMEM:FILE SWPCsv")
        if file_type != 0:
            self.rf_info_msg.emit('Setting file type to "SWPCsv" succeeded: {}'.format(file_type))
        else:
            self.rf_info_msg.emit('Setting file type "SWPCsv" failed')
            sys.emit()
        
        # setting sweep mode to continue
        sweep_mode = self.my_instrument.write(":SWE:MODE CONT")
        if sweep_mode != 0:
            self.rf_info_msg.emit('Setting sweep mode to "CONTinue" succeeded: {}'.format(sweep_mode))
        else:
            self.rf_info_msg.emit('Setting sweep mode to "CONTinue"failed')
            sys.emit()
        
        # setting period trigger type to auto
        pe_sweep_trig = self.my_instrument.write(":SWE:SWE:TRIG:TYPE AUTO")
        if pe_sweep_trig != 0:
            self.rf_info_msg.emit('Setting period trigger type TO "AUTO" succeeded: {}'.format(pe_sweep_trig))
        else:
            self.rf_info_msg.emit('Setting period trigger type "AUTO" failed')
            sys.emit()

        #setting poit trigger type to external
        pt_sweep_trig = self.my_instrument.write(":SWE:POIN:TRIG:TYPE EXT")
        if pt_sweep_trig != 0:
            self.rf_info_msg.emit('Setting point trigger type to "EXT" succeeded: {}'.format(pt_sweep_trig))
        else:
            self.rf_info_msg.emit('Setting point trigger type "EXT" failed')
            sys.emit()

        # setting triger_slope to positive
        trig_slope = self.my_instrument.write(":INP:TRIG:SLOP POS ")
        if trig_slope != 0:
            self.rf_info_msg.emit('Setting trigger slope to "Positive" succeeded: {}'.format(trig_slope))
        else:
            self.rf_info_msg.emit('Setting trigger slope to "Positive" failed')
            sys.emit()

        # setting sweep state to level and frequency
        sweep_state = self.my_instrument.write(":SWE:STAT LEV,FREQ")
        if sweep_state != 0:
            self.rf_info_msg.emit('Setting sweep state to "Level and Frequency" succeeded: {}'.format(sweep_state))
        else:
            self.rf_info_msg.emit('Setting sweep state to "Level and Frequency" failed')
            sys.emit()

    def rf_spl_ld(self):

        sample = self.rf_sample_ledit.text()
        load_status = self.my_instrument.write(':MMEMory:LOAD E:\RF_freqSW_list\cw_odmr\{}.csv'.format(sample))
        if load_status != 0:
            self.rf_info_msg.emit('Loading SWPcsv list sample succeeded: {}'.format(load_status))
        else:
            self.rf_info_msg.emit('Loading SWPcsv list sample failed')

    def rf_ply_stp(self):
        output_status = self.my_instrument.query(':OUTP?')
        if output_status == '0\n':
            
            self.rf_ply_stp_btn.setText('RF OFF')
            self.off_icon = QIcon()
            self.off_icon.addPixmap(QPixmap(":/my_icons/images/icons/stop.svg"), QIcon.Normal, QIcon.Off)
            self.rf_ply_stp_btn.setIcon(self.off_icon)
            rtn = self.my_instrument.write(":OUTP ON")
            if rtn != 0:
                self.rf_info_msg.emit('RF ON succeeded: {}'.format(rtn))
            else:
                self.rf_info_msg.emit('RF ON failed')
                sys.emit()
        elif output_status == '1\n':
            self.rf_ply_stp_btn.setText('RF ON  ')
            self.on_icon = QIcon()
            self.on_icon.addPixmap(QPixmap(":/my_icons/images/icons/play.svg"), QIcon.Normal, QIcon.Off)
            self.rf_ply_stp_btn.setIcon(self.on_icon)
            rtn = self.my_instrument.write(":OUTP OFF")
            if rtn != 0:
                self.rf_info_msg.emit('RF OFF succeeded: {}'.format(rtn))
            else:
                self.rf_info_msg.emit('RF OFF failed')
                sys.emit()
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
