# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rabi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1419, 1017)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget#Form{\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QWidget#mainwidget{\n"
"    background-color: rgba(239, 244, 249, 0);\n"
"    border-radius:10px;\n"
"}\n"
"QFrame#mainframe{\n"
"    background-color: rgba(239, 244, 249, 255);\n"
"    border-radius:10px;\n"
"}\n"
"QGroupBox{\n"
"    border-width: 2px;\n"
"    \n"
"    font: 25 9pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 2px;\n"
"    border: 1px groove gray;\n"
"    font: 63 9pt \"Nunito Sans SemiBold\";\n"
"}\n"
"QTabWidget{\n"
"    font: 63 9pt \"Nunito Sans SemiBold\";\n"
"}\n"
"QLabel{\n"
"    font: 9pt \"Microsoft YaHei UI\";\n"
"}\n"
"QComboBox{\n"
"    \n"
"    font: 9pt \"Menlo for Powerline\";\n"
"}\n"
"")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.mainwidget = QtWidgets.QWidget(Form)
        self.mainwidget.setStyleSheet("")
        self.mainwidget.setObjectName("mainwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mainframe = QtWidgets.QFrame(self.mainwidget)
        self.mainframe.setStyleSheet("")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainframe)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.mainframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(5, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/my_icons/images/icons/window_title_icon.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.min_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy)
        self.min_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.min_btn.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgba(239, 244, 249, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(160, 160, 160,100);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"}\n"
"")
        self.min_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/min.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_btn.setIcon(icon)
        self.min_btn.setObjectName("min_btn")
        self.horizontalLayout_2.addWidget(self.min_btn)
        self.max_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy)
        self.max_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.max_btn.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgba(239, 244, 249, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(160, 160, 160,100);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"}")
        self.max_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/max.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_btn.setIcon(icon1)
        self.max_btn.setIconSize(QtCore.QSize(20, 20))
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout_2.addWidget(self.max_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMaximumSize(QtCore.QSize(60, 30))
        self.close_btn.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgba(239, 244, 249, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(196, 43, 28,200);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"}")
        self.close_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/close_btn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.horizontalLayout_2.setStretch(3, 80)
        self.horizontalLayout_2.setStretch(4, 3)
        self.horizontalLayout_2.setStretch(5, 3)
        self.horizontalLayout_2.setStretch(6, 3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.mainframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(160, 160, 160,100);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: transparent;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 501, 421))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.asg_start_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.asg_start_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.asg_start_btn.setIcon(icon3)
        self.asg_start_btn.setIconSize(QtCore.QSize(20, 25))
        self.asg_start_btn.setObjectName("asg_start_btn")
        self.horizontalLayout_3.addWidget(self.asg_start_btn)
        self.asg_stop_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.asg_stop_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.asg_stop_btn.setIcon(icon4)
        self.asg_stop_btn.setIconSize(QtCore.QSize(20, 25))
        self.asg_stop_btn.setObjectName("asg_stop_btn")
        self.horizontalLayout_3.addWidget(self.asg_stop_btn)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 2, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.asg_connect_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.asg_connect_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/connect.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.asg_connect_btn.setIcon(icon5)
        self.asg_connect_btn.setIconSize(QtCore.QSize(20, 25))
        self.asg_connect_btn.setObjectName("asg_connect_btn")
        self.gridLayout.addWidget(self.asg_connect_btn, 0, 0, 1, 1)
        self.asg_close_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.asg_close_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        self.asg_close_btn.setIcon(icon5)
        self.asg_close_btn.setIconSize(QtCore.QSize(20, 25))
        self.asg_close_btn.setObjectName("asg_close_btn")
        self.gridLayout.addWidget(self.asg_close_btn, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.asg_scroll = QtWidgets.QScrollArea(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asg_scroll.sizePolicy().hasHeightForWidth())
        self.asg_scroll.setSizePolicy(sizePolicy)
        self.asg_scroll.setWidgetResizable(True)
        self.asg_scroll.setObjectName("asg_scroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 463, 85))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.asg_msg = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.asg_msg.setText("")
        self.asg_msg.setObjectName("asg_msg")
        self.verticalLayout_8.addWidget(self.asg_msg)
        self.asg_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.asg_scroll, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 3, 0, 1, 4)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 4, 2, 1, 1)
        self.rabi_start_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.rabi_start_spbx.setMaximum(3000)
        self.rabi_start_spbx.setProperty("value", 50)
        self.rabi_start_spbx.setObjectName("rabi_start_spbx")
        self.gridLayout_6.addWidget(self.rabi_start_spbx, 1, 1, 1, 1)
        self.init_time_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.init_time_spbx.setMaximum(100)
        self.init_time_spbx.setProperty("value", 5)
        self.init_time_spbx.setObjectName("init_time_spbx")
        self.gridLayout_6.addWidget(self.init_time_spbx, 0, 1, 1, 1)
        self.fore_time_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.fore_time_spbx.setMaximum(5000)
        self.fore_time_spbx.setProperty("value", 1000)
        self.fore_time_spbx.setObjectName("fore_time_spbx")
        self.gridLayout_6.addWidget(self.fore_time_spbx, 4, 1, 1, 1)
        self.acq_time_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.acq_time_spbx.setMaximum(5000)
        self.acq_time_spbx.setProperty("value", 1000)
        self.acq_time_spbx.setObjectName("acq_time_spbx")
        self.gridLayout_6.addWidget(self.acq_time_spbx, 0, 3, 1, 1)
        self.rabi_step_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.rabi_step_spbx.setMaximum(3000)
        self.rabi_step_spbx.setProperty("value", 10)
        self.rabi_step_spbx.setObjectName("rabi_step_spbx")
        self.gridLayout_6.addWidget(self.rabi_step_spbx, 2, 1, 1, 1)
        self.back_time_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.back_time_spbx.setMinimum(-5000)
        self.back_time_spbx.setMaximum(5000)
        self.back_time_spbx.setProperty("value", 100)
        self.back_time_spbx.setObjectName("back_time_spbx")
        self.gridLayout_6.addWidget(self.back_time_spbx, 4, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_8)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_8)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)
        self.repeat_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.repeat_spbx.setMaximum(1000000)
        self.repeat_spbx.setProperty("value", 5000)
        self.repeat_spbx.setObjectName("repeat_spbx")
        self.gridLayout_6.addWidget(self.repeat_spbx, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 2, 2, 1, 1)
        self.rabi_stop_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.rabi_stop_spbx.setMaximum(5000)
        self.rabi_stop_spbx.setProperty("value", 2000)
        self.rabi_stop_spbx.setObjectName("rabi_stop_spbx")
        self.gridLayout_6.addWidget(self.rabi_stop_spbx, 1, 3, 1, 1)
        self.asg_set_btn = QtWidgets.QPushButton(self.groupBox_8)
        self.asg_set_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.asg_set_btn.setIcon(icon6)
        self.asg_set_btn.setIconSize(QtCore.QSize(20, 25))
        self.asg_set_btn.setObjectName("asg_set_btn")
        self.gridLayout_6.addWidget(self.asg_set_btn, 5, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 5, 0, 1, 1)
        self.laser_diff_time_spbx = QtWidgets.QSpinBox(self.groupBox_8)
        self.laser_diff_time_spbx.setMinimum(-5000)
        self.laser_diff_time_spbx.setMaximum(5000)
        self.laser_diff_time_spbx.setProperty("value", 0)
        self.laser_diff_time_spbx.setObjectName("laser_diff_time_spbx")
        self.gridLayout_6.addWidget(self.laser_diff_time_spbx, 5, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_8, 1, 0, 1, 4)
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_9.setGeometry(QtCore.QRect(520, 20, 861, 921))
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.groupBox_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.restore_view_btn = QtWidgets.QPushButton(self.groupBox_5)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/init.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_view_btn.setIcon(icon7)
        self.restore_view_btn.setIconSize(QtCore.QSize(20, 25))
        self.restore_view_btn.setObjectName("restore_view_btn")
        self.horizontalLayout_10.addWidget(self.restore_view_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.plot_data_btn = QtWidgets.QPushButton(self.groupBox_5)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/plot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_data_btn.setIcon(icon8)
        self.plot_data_btn.setIconSize(QtCore.QSize(20, 25))
        self.plot_data_btn.setObjectName("plot_data_btn")
        self.horizontalLayout_10.addWidget(self.plot_data_btn)
        self.save_plot_data_btn = QtWidgets.QPushButton(self.groupBox_5)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_plot_data_btn.setIcon(icon9)
        self.save_plot_data_btn.setIconSize(QtCore.QSize(20, 25))
        self.save_plot_data_btn.setObjectName("save_plot_data_btn")
        self.horizontalLayout_10.addWidget(self.save_plot_data_btn)
        self.save_plot_btn = QtWidgets.QPushButton(self.groupBox_5)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/picture.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_plot_btn.setIcon(icon10)
        self.save_plot_btn.setIconSize(QtCore.QSize(20, 25))
        self.save_plot_btn.setObjectName("save_plot_btn")
        self.horizontalLayout_10.addWidget(self.save_plot_btn)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_10)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.current_rabi_time_spbx = QtWidgets.QSpinBox(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_rabi_time_spbx.sizePolicy().hasHeightForWidth())
        self.current_rabi_time_spbx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_rabi_time_spbx.setFont(font)
        self.current_rabi_time_spbx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_rabi_time_spbx.setReadOnly(True)
        self.current_rabi_time_spbx.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.current_rabi_time_spbx.setMaximum(100000)
        self.current_rabi_time_spbx.setProperty("value", 0)
        self.current_rabi_time_spbx.setObjectName("current_rabi_time_spbx")
        self.horizontalLayout_4.addWidget(self.current_rabi_time_spbx)
        self.horizontalLayout_10.addWidget(self.groupBox_10)
        self.horizontalLayout_10.setStretch(1, 3)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 1)
        self.horizontalLayout_10.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.line = QtWidgets.QFrame(self.groupBox_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.graph_frame = QtWidgets.QFrame(self.groupBox_5)
        self.graph_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.graph_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graph_frame.setLineWidth(3)
        self.graph_frame.setMidLineWidth(3)
        self.graph_frame.setObjectName("graph_frame")
        self.verticalLayout_2.addWidget(self.graph_frame)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.data_processing_scroll = QtWidgets.QScrollArea(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_processing_scroll.sizePolicy().hasHeightForWidth())
        self.data_processing_scroll.setSizePolicy(sizePolicy)
        self.data_processing_scroll.setWidgetResizable(True)
        self.data_processing_scroll.setObjectName("data_processing_scroll")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 823, 111))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.data_processing_msg = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.data_processing_msg.setText("")
        self.data_processing_msg.setObjectName("data_processing_msg")
        self.verticalLayout_24.addWidget(self.data_processing_msg)
        self.data_processing_scroll.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.addWidget(self.data_processing_scroll, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_11)
        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 840, 211, 91))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_repeat_count_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.clear_repeat_count_btn.setStyleSheet("QPushButton{\n"
"    font: 10pt \"Yu Gothic UI\";    \n"
"\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/my_icons/images/icons/restore.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_repeat_count_btn.setIcon(icon11)
        self.clear_repeat_count_btn.setIconSize(QtCore.QSize(20, 25))
        self.clear_repeat_count_btn.setObjectName("clear_repeat_count_btn")
        self.horizontalLayout.addWidget(self.clear_repeat_count_btn)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 450, 501, 301))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.mainframe)
        self.verticalLayout_19.addWidget(self.mainwidget)
        self.verticalLayout_19.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Rabi"))
        self.label_6.setText(_translate("Form", "----Version 1.0"))
        self.groupBox.setTitle(_translate("Form", "ASG8005 Control Panel"))
        self.groupBox_4.setTitle(_translate("Form", "Play"))
        self.asg_start_btn.setText(_translate("Form", "Start"))
        self.asg_stop_btn.setText(_translate("Form", "Stop"))
        self.groupBox_2.setTitle(_translate("Form", "Device"))
        self.asg_connect_btn.setText(_translate("Form", "Connect"))
        self.asg_close_btn.setText(_translate("Form", "Close"))
        self.groupBox_7.setTitle(_translate("Form", "ASG8005 Setup Info"))
        self.groupBox_8.setTitle(_translate("Form", "Pulse Sequence"))
        self.label_12.setText(_translate("Form", "RabiStop(ns):"))
        self.label_10.setText(_translate("Form", "RabiStep(ns):"))
        self.label_15.setText(_translate("Form", "BackTime(ns):"))
        self.label_14.setText(_translate("Form", "ForeTime(ns):"))
        self.label_8.setText(_translate("Form", "AcqTime(ns):"))
        self.label_3.setText(_translate("Form", "InitTime(μs):"))
        self.label_11.setText(_translate("Form", "RabiStart(ns):"))
        self.label_9.setText(_translate("Form", "Repeat:"))
        self.asg_set_btn.setText(_translate("Form", "Set"))
        self.label_16.setText(_translate("Form", "LaserDiff(ns):"))
        self.groupBox_9.setTitle(_translate("Form", "Data Processing"))
        self.groupBox_5.setTitle(_translate("Form", "DAQ Plot"))
        self.restore_view_btn.setText(_translate("Form", "Restore"))
        self.plot_data_btn.setText(_translate("Form", "Plot Data"))
        self.save_plot_data_btn.setText(_translate("Form", "Save Plot Data"))
        self.save_plot_btn.setText(_translate("Form", "Save Plot"))
        self.groupBox_10.setTitle(_translate("Form", "CurrentProcess"))
        self.label_13.setText(_translate("Form", "Rabi Time:"))
        self.groupBox_11.setTitle(_translate("Form", "Data Processing Info"))
        self.groupBox_3.setTitle(_translate("Form", "Clear"))
        self.clear_repeat_count_btn.setText(_translate("Form", "ClearRepeatCount"))
        self.groupBox_6.setTitle(_translate("Form", "Check Laser Synchronization"))
import resources_rc
