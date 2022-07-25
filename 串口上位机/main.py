# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw  # 导入PYQT库命名为ｑｗ
from ui import ui_test  # 导入PYQTUI目录的包


class My_MainWindow(qw.QMainWindow, ui_test.Ui_MainWindow): #类调用
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

    def combobox_baud_cb(self):  # 波特率下拉框
        content = self.comboBox_btl.currentText()  # 选中的内容
        print("combox is", content)
        text = "您当前选中了%s" % content
        qw.QMessageBox.information(self, "提示", text, qw.QMessageBox.Ok | qw.QMessageBox.Cancel)  # 弹出消息框
        return ()  # 返回参数

    def pushButton_sinp_cb(self):  # 发送按钮
        print("发送")
        text = self.textEdit_get.toPlainText()
        print(" 文本内容是", text)
        self.comboBox_uart.addItem(text)

    def action_start_cb(self):  # 开始
        print("开始")

    def action_stop_cb(self):  # 停止
        print("停止")

    def action_clear_cb(self):  # 清除
        print("清除")

    def action_pause_cb(self):  # 暂停
        print("暂停")

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    w = My_MainWindow()
    # w = qw.QMainWindow()
    # ui = ui_test.Ui_MainWindow()
    # ui.setupUi(w)
    w.show()

    sys.exit(app.exec_())
