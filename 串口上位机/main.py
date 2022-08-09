# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw  # 导入PYQT库命名为ｑｗ
from ui import ui_test  # 导入PYQTUI目录的包
import PyQt5.QtCore as qc


class My_MainWindow(qw.QMainWindow, ui_test.Ui_MainWindow):  # 类调用
    def __init__(self):  # 初始化属性
        super().__init__()  # 调用父类属性
        self.setupUi(self)
        # 绑定信号与槽
        self.comboBox_btl.currentIndexChanged.connect(self.combobox_baud_cb)  # 波特率bobox下拉框
        self.pushButton_sinp.clicked.connect(self.pushButton_sinp_cb)  # 发送按钮
        self.action_start.triggered.connect(self.action_start_cb)  # 开始
        self.action_pause.triggered.connect(self.action_pause_cb)  # 暂停
        self.action_stop.triggered.connect(self.action_stop_cb)  # 停止
        self.action_clear.triggered.connect(self.action_clear_cb)  # 清除
        self.radioButton_T_ascii.toggled.connect(self.radioButton_T_ascii_cb)  # 单选框
        self.radioButton_T_hex.toggled.connect(self.radioButton_T_hex_cb)
        self.radioButton_R_ascii.toggled.connect(self.radioButton_R_ascii_cb)
        self.radioButton_R_hex.toggled.connect(self.radioButton_R_hex_cb)
        self.checkBox_zdhh.toggled.connect(self.checkBox_zdhh_cb)  # 复选框
        self.checkBox_xssj.toggled.connect(self.checkBox_xssj_cb)
        self.checkBox_xsfs.toggled.connect(self.checkBox_xsfs_cb)
        self.checkBox_cffs.toggled.connect(self.checkBox_cffs_cb)
        self.doubleSpinBox.valueChanged.connect(self.spinBox_cb)  # 重复发送时间

        # 初始化窗口
        self.ztl.showMessage("状态栏信息")  # 状态栏消息
        # 加载配置文件
        self.settings = qc.QSettings("config.ini", qc.QSettings.IniFormat)
        self.config_uart_baud = self.settings.value("SETUP/UART_BAUD")
        print("加载的配置%s" % self.config_uart_baud)
        # self.config_uart_baud = self.settings.value("UART_BAUD", 0, type=int)
        # print("加载的配置%d" % self.config_uart_baud)

        # 初始化界面

        self.radioButton_R_ascii.setChecked(True)  # 初始单选框为ASCII码
        self.radioButton_T_ascii.setChecked(True)
        self.checkBox_zdhh.setChecked(False)  # 复选框自动换行
        self.doubleSpinBox.setRange(100, 30000)
        self.doubleSpinBox.setValue(1000)
        self.doubleSpinBox.setSingleStep(100)
        self.doubleSpinBox.setDecimals(0)  # 小数位数
        self.doubleSpinBox.setWrapping(True)  # 循环显示
        self.comboBox_btl.setCurrentText(str(self.config_uart_baud))  # 初始波特率

    def combobox_baud_cb(self):  # 波特率下拉框

        content = self.comboBox_btl.currentText()  # 选中的内容
        print("combox is", content)
        self.settings.setValue("SETUP/UART_BAUD", content)  # 写入波特率到文件
        # text = "您当前选中了%s" % content
        # qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Ok | qw.QMessageBox.Cancel)  # 弹出消息框
        return ()  # 返回参数

    def pushButton_sinp_cb(self):  # 发送按钮
        print("您点击了发送")
        text = self.textEdit_get.toPlainText()
        print(" 文本内容是", text)
        self.comboBox_uart.addItem(text)

    def action_start_cb(self):  # 开始
        print("您点击了开始")

    def action_stop_cb(self):  # 停止
        print("您点击了停止")

    def action_clear_cb(self):  # 清除
        print("您点击了清除")

    def action_pause_cb(self):  # 暂停
        print("您点击了暂停")

    def radioButton_T_ascii_cb(self):  # 获取单选框选定
        print("选中了T_ASCIi")

    def radioButton_T_hex_cb(self):  #
        print("选中了t_hex")

    def radioButton_R_ascii_cb(self):  #
        print("选中了R_ascii")

    def radioButton_R_hex_cb(self):  #

        print("点击发送hex")

    def checkBox_zdhh_cb(self):  # 复选框
        print("点击了自动换行")
        res_zdhh_line = self.checkBox_zdhh.isChecked()
        print("自动换行状态", res_zdhh_line)
        res_show_send = self.checkBox_xsfs.isChecked()
        print("选中了显示发送", res_show_send)
        res_show_time = self.checkBox_xssj.isChecked()
        print("选中了显示时间", res_show_time)
        res_repeat_sand = self.checkBox_cffs.isChecked()
        print("选中了重复发送", res_repeat_sand)

    def checkBox_xssj_cb(self):  #
        print("点击了显示时间")

    def checkBox_xsfs_cb(self):  #
        print("点击了显示发送")

    def checkBox_cffs_cb(self):  #
        print("点击了重复发送")

    def spinBox_cb(self, value):  #
        print("当前时间间隔%d" % value)


if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = My_MainWindow()
    # w = qw.QMainWindow()
    # ui = ui_test.Ui_MainWindow()
    # ui.setupUi(w)
    w.show()

    sys.exit(app.exec_())
