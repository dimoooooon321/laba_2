

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 521)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(370, 420))
        MainWindow.setMaximumSize(QSize(740, 770))
        icon = QIcon()
        icon.addFile(u":/icons/F:/\u0417\u0410\u0413\u0420\u0423\u0417\u041a\u0418/calculate_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(232, 231, 235);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"border-style: solid;\n"
"                border-width: 3px;\n"
"                border-color: rgb(116, 176, 69);\n"
"border-bottom-color: rgb(232, 231, 235)\n"
"")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.lineEdit.setFont(font1)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"border-style: solid;\n"
"                border-width: 3px;\n"
"                border-color: rgb(116, 176, 69);\n"
"border-top-color: rgb(232, 231, 235);\n"
"")
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_negate = QPushButton(self.centralwidget)
        self.pushButton_negate.setObjectName(u"pushButton_negate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_negate.sizePolicy().hasHeightForWidth())
        self.pushButton_negate.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_negate.setFont(font2)
        self.pushButton_negate.setStyleSheet(u"background-color: rgb(231, 164, 9);")

        self.horizontalLayout.addWidget(self.pushButton_negate)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy2.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy2)
        self.pushButton_clear.setFont(font2)
        self.pushButton_clear.setStyleSheet(u"background-color: rgb(231, 164, 9);")

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.pushButton_backspace = QPushButton(self.centralwidget)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_backspace.sizePolicy().hasHeightForWidth())
        self.pushButton_backspace.setSizePolicy(sizePolicy3)
        self.pushButton_backspace.setFont(font2)
        self.pushButton_backspace.setStyleSheet(u"background-color: rgb(231, 164, 9);")

        self.horizontalLayout.addWidget(self.pushButton_backspace)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_E = QPushButton(self.centralwidget)
        self.pushButton_E.setObjectName(u"pushButton_E")
        self.pushButton_E.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_E.sizePolicy().hasHeightForWidth())
        self.pushButton_E.setSizePolicy(sizePolicy4)
        self.pushButton_E.setFont(font3)
        self.pushButton_E.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_E, 0, 4, 1, 1)

        self.pushButton_bracket_closing = QPushButton(self.centralwidget)
        self.pushButton_bracket_closing.setObjectName(u"pushButton_bracket_closing")
        self.pushButton_bracket_closing.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_bracket_closing.sizePolicy().hasHeightForWidth())
        self.pushButton_bracket_closing.setSizePolicy(sizePolicy4)
        self.pushButton_bracket_closing.setFont(font3)
        self.pushButton_bracket_closing.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_bracket_closing, 3, 5, 1, 1)

        self.pushButton_mul = QPushButton(self.centralwidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        sizePolicy4.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy4)
        self.pushButton_mul.setFont(font3)
        self.pushButton_mul.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_mul, 1, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_percent = QPushButton(self.centralwidget)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_percent.sizePolicy().hasHeightForWidth())
        self.pushButton_percent.setSizePolicy(sizePolicy4)
        self.pushButton_percent.setFont(font3)
        self.pushButton_percent.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_percent, 2, 4, 1, 1)

        self.pushButton_mod = QPushButton(self.centralwidget)
        self.pushButton_mod.setObjectName(u"pushButton_mod")
        self.pushButton_mod.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_mod.sizePolicy().hasHeightForWidth())
        self.pushButton_mod.setSizePolicy(sizePolicy4)
        self.pushButton_mod.setFont(font3)
        self.pushButton_mod.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_mod, 1, 4, 1, 1)

        self.pushButton_PI = QPushButton(self.centralwidget)
        self.pushButton_PI.setObjectName(u"pushButton_PI")
        self.pushButton_PI.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_PI.sizePolicy().hasHeightForWidth())
        self.pushButton_PI.setSizePolicy(sizePolicy4)
        self.pushButton_PI.setFont(font3)
        self.pushButton_PI.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_PI, 0, 5, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy4.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy4)
        self.pushButton_0.setFont(font3)
        self.pushButton_0.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_0, 3, 0, 1, 1)

        self.pushButton_sqrt = QPushButton(self.centralwidget)
        self.pushButton_sqrt.setObjectName(u"pushButton_sqrt")
        self.pushButton_sqrt.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_sqrt.sizePolicy().hasHeightForWidth())
        self.pushButton_sqrt.setSizePolicy(sizePolicy4)
        self.pushButton_sqrt.setFont(font3)
        self.pushButton_sqrt.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_sqrt, 2, 5, 1, 1)

        self.pushButton_bracket_opening = QPushButton(self.centralwidget)
        self.pushButton_bracket_opening.setObjectName(u"pushButton_bracket_opening")
        self.pushButton_bracket_opening.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_bracket_opening.sizePolicy().hasHeightForWidth())
        self.pushButton_bracket_opening.setSizePolicy(sizePolicy4)
        self.pushButton_bracket_opening.setFont(font3)
        self.pushButton_bracket_opening.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_bracket_opening, 3, 4, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(116, 176, 69)")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy4.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy4)
        self.pushButton_1.setFont(font3)
        self.pushButton_1.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)

        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        sizePolicy4.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy4)
        self.pushButton_plus.setFont(font3)
        self.pushButton_plus.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)

        self.pushButton_equals = QPushButton(self.centralwidget)
        self.pushButton_equals.setObjectName(u"pushButton_equals")
        sizePolicy4.setHeightForWidth(self.pushButton_equals.sizePolicy().hasHeightForWidth())
        self.pushButton_equals.setSizePolicy(sizePolicy4)
        self.pushButton_equals.setFont(font3)
        self.pushButton_equals.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_equals, 3, 2, 1, 1)

        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        sizePolicy4.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy4)
        self.pushButton_minus.setFont(font3)
        self.pushButton_minus.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_minus, 2, 3, 1, 1)

        self.pushButton_power = QPushButton(self.centralwidget)
        self.pushButton_power.setObjectName(u"pushButton_power")
        self.pushButton_power.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_power.sizePolicy().hasHeightForWidth())
        self.pushButton_power.setSizePolicy(sizePolicy4)
        self.pushButton_power.setFont(font3)
        self.pushButton_power.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_power, 1, 5, 1, 1)

        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        sizePolicy4.setHeightForWidth(self.pushButton_divide.sizePolicy().hasHeightForWidth())
        self.pushButton_divide.setSizePolicy(sizePolicy4)
        self.pushButton_divide.setFont(font3)
        self.pushButton_divide.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_divide, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy4.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy4)
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy4.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(116, 176, 69)")

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.pushButton_point = QPushButton(self.centralwidget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        sizePolicy4.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy4)
        self.pushButton_point.setFont(font3)
        self.pushButton_point.setStyleSheet(u"background-color: rgb(224, 230, 228);")

        self.gridLayout.addWidget(self.pushButton_point, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_left = QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_left.sizePolicy().hasHeightForWidth())
        self.pushButton_left.setSizePolicy(sizePolicy3)
        self.pushButton_left.setFont(font3)
        self.pushButton_left.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout_2.addWidget(self.pushButton_left, 3, 0, 1, 1)

        self.pushButton_arctan = QPushButton(self.centralwidget)
        self.pushButton_arctan.setObjectName(u"pushButton_arctan")
        self.pushButton_arctan.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_arctan.sizePolicy().hasHeightForWidth())
        self.pushButton_arctan.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setStrikeOut(False)
        self.pushButton_arctan.setFont(font4)
        self.pushButton_arctan.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_arctan, 2, 0, 1, 1)

        self.pushButton_right = QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_right.sizePolicy().hasHeightForWidth())
        self.pushButton_right.setSizePolicy(sizePolicy3)
        self.pushButton_right.setFont(font3)
        self.pushButton_right.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout_2.addWidget(self.pushButton_right, 3, 1, 1, 1)

        self.pushButton_tan = QPushButton(self.centralwidget)
        self.pushButton_tan.setObjectName(u"pushButton_tan")
        self.pushButton_tan.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_tan.sizePolicy().hasHeightForWidth())
        self.pushButton_tan.setSizePolicy(sizePolicy3)
        self.pushButton_tan.setFont(font3)
        self.pushButton_tan.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_tan, 0, 2, 1, 1)

        self.pushButton_cos = QPushButton(self.centralwidget)
        self.pushButton_cos.setObjectName(u"pushButton_cos")
        self.pushButton_cos.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_cos.sizePolicy().hasHeightForWidth())
        self.pushButton_cos.setSizePolicy(sizePolicy3)
        self.pushButton_cos.setFont(font3)
        self.pushButton_cos.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_cos, 0, 1, 1, 1)

        self.pushButton_arcsin = QPushButton(self.centralwidget)
        self.pushButton_arcsin.setObjectName(u"pushButton_arcsin")
        self.pushButton_arcsin.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_arcsin.sizePolicy().hasHeightForWidth())
        self.pushButton_arcsin.setSizePolicy(sizePolicy3)
        self.pushButton_arcsin.setFont(font4)
        self.pushButton_arcsin.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_arcsin, 1, 1, 1, 1)

        self.pushButton_arccos = QPushButton(self.centralwidget)
        self.pushButton_arccos.setObjectName(u"pushButton_arccos")
        self.pushButton_arccos.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_arccos.sizePolicy().hasHeightForWidth())
        self.pushButton_arccos.setSizePolicy(sizePolicy3)
        self.pushButton_arccos.setFont(font4)
        self.pushButton_arccos.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_arccos, 1, 2, 1, 1)

        self.pushButton_arccot = QPushButton(self.centralwidget)
        self.pushButton_arccot.setObjectName(u"pushButton_arccot")
        self.pushButton_arccot.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_arccot.sizePolicy().hasHeightForWidth())
        self.pushButton_arccot.setSizePolicy(sizePolicy3)
        self.pushButton_arccot.setFont(font4)
        self.pushButton_arccot.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_arccot, 2, 1, 1, 1)

        self.pushButton_sin = QPushButton(self.centralwidget)
        self.pushButton_sin.setObjectName(u"pushButton_sin")
        self.pushButton_sin.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_sin.sizePolicy().hasHeightForWidth())
        self.pushButton_sin.setSizePolicy(sizePolicy3)
        self.pushButton_sin.setFont(font3)
        self.pushButton_sin.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_sin, 0, 0, 1, 1)

        self.pushButton_cot = QPushButton(self.centralwidget)
        self.pushButton_cot.setObjectName(u"pushButton_cot")
        self.pushButton_cot.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_cot.sizePolicy().hasHeightForWidth())
        self.pushButton_cot.setSizePolicy(sizePolicy3)
        self.pushButton_cot.setFont(font3)
        self.pushButton_cot.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_cot, 1, 0, 1, 1)

        self.pushButton_ln = QPushButton(self.centralwidget)
        self.pushButton_ln.setObjectName(u"pushButton_ln")
        self.pushButton_ln.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_ln.sizePolicy().hasHeightForWidth())
        self.pushButton_ln.setSizePolicy(sizePolicy3)
        self.pushButton_ln.setFont(font4)
        self.pushButton_ln.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_ln, 2, 2, 1, 1)

        self.pushButton_log = QPushButton(self.centralwidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_log.sizePolicy().hasHeightForWidth())
        self.pushButton_log.setSizePolicy(sizePolicy3)
        self.pushButton_log.setFont(font4)
        self.pushButton_log.setStyleSheet(u"background-color: rgb(195, 195, 195);")

        self.gridLayout_2.addWidget(self.pushButton_log, 3, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 370, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_clear.clicked.connect(self.lineEdit.clear)
        self.pushButton_backspace.clicked.connect(self.lineEdit.undo)

        self.pushButton_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_negate.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_negate.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Up", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.pushButton_backspace.setText(QCoreApplication.translate("MainWindow", u"<-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_E.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.pushButton_bracket_closing.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_mul.setText(QCoreApplication.translate("MainWindow", u"×", None))
#if QT_CONFIG(shortcut)
        self.pushButton_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_mod.setText(QCoreApplication.translate("MainWindow", u"mod", None))
        self.pushButton_PI.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_bracket_opening.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_equals.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_power.setText(QCoreApplication.translate("MainWindow", u"^\u2610", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.pushButton_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_left.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.pushButton_arctan.setText(QCoreApplication.translate("MainWindow", u"arctan", None))
        self.pushButton_right.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.pushButton_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.pushButton_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.pushButton_arcsin.setText(QCoreApplication.translate("MainWindow", u"arcsin", None))
        self.pushButton_arccos.setText(QCoreApplication.translate("MainWindow", u"arccos", None))
        self.pushButton_arccot.setText(QCoreApplication.translate("MainWindow", u"arccot", None))
        self.pushButton_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.pushButton_cot.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.pushButton_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.pushButton_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
    # retranslateUi

