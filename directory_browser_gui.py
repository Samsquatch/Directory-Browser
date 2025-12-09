# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Directory-Browser-qtdesignerhiSmKK.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTreeView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 789)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(662, 461))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(662, 400))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(425, 400))
        self.splitter.setAutoFillBackground(False)
        self.splitter.setStyleSheet(u"QSplitter::handle {\n"
"    background-color: rgb(200, 200, 200);\n"
"    margin-top: 15px;   /* shrink visible part */\n"
"    margin-bottom: 9px;  /* shrink visible part */\n"
"}\n"
"")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(4)
        self.splitter.setChildrenCollapsible(False)
        self.LeftWidgetContainer = QWidget(self.splitter)
        self.LeftWidgetContainer.setObjectName(u"LeftWidgetContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LeftWidgetContainer.sizePolicy().hasHeightForWidth())
        self.LeftWidgetContainer.setSizePolicy(sizePolicy2)
        self.LeftWidgetContainer.setMinimumSize(QSize(325, 300))
        self.gridLayout_3 = QGridLayout(self.LeftWidgetContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.LeftWidgetContainer)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(300, 86))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.path_line_edit = QLineEdit(self.groupBox)
        self.path_line_edit.setObjectName(u"path_line_edit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.path_line_edit.sizePolicy().hasHeightForWidth())
        self.path_line_edit.setSizePolicy(sizePolicy4)
        self.path_line_edit.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.path_line_edit, 0, 0, 1, 1)

        self.browse_button = QPushButton(self.groupBox)
        self.browse_button.setObjectName(u"browse_button")
        sizePolicy.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.browse_button, 0, 1, 1, 1)

        self.recursive_check_box = QCheckBox(self.groupBox)
        self.recursive_check_box.setObjectName(u"recursive_check_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.recursive_check_box.sizePolicy().hasHeightForWidth())
        self.recursive_check_box.setSizePolicy(sizePolicy5)
        self.recursive_check_box.setMinimumSize(QSize(50, 0))

        self.gridLayout_2.addWidget(self.recursive_check_box, 1, 0, 1, 1)

        self.refresh_button = QPushButton(self.groupBox)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setMinimumSize(QSize(20, 20))
        self.refresh_button.setAutoFillBackground(False)
        self.refresh_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../assets/refresh-arrows.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_button.setIcon(icon)
        self.refresh_button.setFlat(False)

        self.gridLayout_2.addWidget(self.refresh_button, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.directory_tree_view = QTreeView(self.LeftWidgetContainer)
        self.directory_tree_view.setObjectName(u"directory_tree_view")
        sizePolicy2.setHeightForWidth(self.directory_tree_view.sizePolicy().hasHeightForWidth())
        self.directory_tree_view.setSizePolicy(sizePolicy2)
        self.directory_tree_view.setMinimumSize(QSize(300, 200))
        self.directory_tree_view.setAlternatingRowColors(True)

        self.gridLayout_3.addWidget(self.directory_tree_view, 1, 0, 1, 1)

        self.splitter.addWidget(self.LeftWidgetContainer)
        self.RightWidgetContainer = QWidget(self.splitter)
        self.RightWidgetContainer.setObjectName(u"RightWidgetContainer")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.RightWidgetContainer.sizePolicy().hasHeightForWidth())
        self.RightWidgetContainer.setSizePolicy(sizePolicy6)
        self.RightWidgetContainer.setMinimumSize(QSize(325, 300))
        self.gridLayout_4 = QGridLayout(self.RightWidgetContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inspector_scroll_area = QScrollArea(self.RightWidgetContainer)
        self.inspector_scroll_area.setObjectName(u"inspector_scroll_area")
        sizePolicy2.setHeightForWidth(self.inspector_scroll_area.sizePolicy().hasHeightForWidth())
        self.inspector_scroll_area.setSizePolicy(sizePolicy2)
        self.inspector_scroll_area.setMinimumSize(QSize(300, 200))
        self.inspector_scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setObjectName(u"scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 424, 600))
        self.inspector_scroll_area.setWidget(self.scroll_area_widget_contents)

        self.gridLayout_4.addWidget(self.inspector_scroll_area, 3, 0, 1, 1)

        self.top_vertical_spacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.top_vertical_spacer, 0, 0, 1, 1)

        self.bottom_vertical_spacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.bottom_vertical_spacer, 2, 0, 1, 1)

        self.execute_push_button = QPushButton(self.RightWidgetContainer)
        self.execute_push_button.setObjectName(u"execute_push_button")
        sizePolicy5.setHeightForWidth(self.execute_push_button.sizePolicy().hasHeightForWidth())
        self.execute_push_button.setSizePolicy(sizePolicy5)
        self.execute_push_button.setMinimumSize(QSize(120, 50))
        icon1 = QIcon()
        icon1.addFile(u"../assets/play-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.execute_push_button.setIcon(icon1)

        self.gridLayout_4.addWidget(self.execute_push_button, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.splitter.addWidget(self.RightWidgetContainer)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.refresh_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input Path", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.recursive_check_box.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u" Refresh", None))
        self.execute_push_button.setText(QCoreApplication.translate("MainWindow", u" Execute", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())