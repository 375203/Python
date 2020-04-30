import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QFont
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")
        QToolTip.setFont(QFont("SansSerif", 12))
        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()
        # 添加表单布局
        formLayout.addRow("整数类型", intLineEdit)
        formLayout.addRow("浮点类型", doubleLineEdit)
        formLayout.addRow("数字和字母", validatorLineEdit)
        # 控件占位信息
        intLineEdit.setPlaceholderText("整形")
        doubleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("数字和字母")
        # 控件提示信息
        intLineEdit.setToolTip("整形")
        doubleLineEdit.setToolTip("浮点型")
        validatorLineEdit.setToolTip("数字和字母")
        # 整形校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)
        # 浮点校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)  # 设置精度，小数点后2位
        # 字符和数字  采用正则表达式
        reg = QRegExp("[a-zA-z0-9]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)
        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
