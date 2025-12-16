# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QDir)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QStandardItem, QStandardItemModel,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QFileDialog, QMessageBox, QHeaderView, 
    QLineEdit, QMainWindow, QMenuBar, QPushButton, 
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter, 
    QStatusBar, QTreeView, QWidget, QFileSystemModel)

import sys
import os
from multiprocessing import freeze_support

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):

        ### Set up main GUI components (MainWindow, centralwidget, splitter) ###
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 789)
        self.set_window_icon(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(662, 461))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Directory Browser", None))
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

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ### Set up left widget container (path input, directory tree view) ###
        self.left_widget_container = QWidget(self.splitter)
        self.left_widget_container.setObjectName(u"left_widget_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_widget_container.sizePolicy().hasHeightForWidth())
        self.left_widget_container.setSizePolicy(sizePolicy2)
        self.left_widget_container.setMinimumSize(QSize(325, 300))
        self.gridLayout_3 = QGridLayout(self.left_widget_container)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        

        self.groupBox = QGroupBox(self.left_widget_container)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input Path", None))
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
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.browse_button.clicked.connect(lambda: self.folder_select(self.path_line_edit))
        sizePolicy.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy)
        self.gridLayout_2.addWidget(self.browse_button, 0, 1, 1, 1)

        self.recursive_check_box = QCheckBox(self.groupBox)
        self.recursive_check_box.setObjectName(u"recursive_check_box")
        self.recursive_check_box.setText(QCoreApplication.translate("MainWindow", u"Recursive", None))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.recursive_check_box.sizePolicy().hasHeightForWidth())
        self.recursive_check_box.setSizePolicy(sizePolicy5)
        self.recursive_check_box.setMinimumSize(QSize(50, 0))
        self.gridLayout_2.addWidget(self.recursive_check_box, 1, 0, 1, 1)

        self.scan_button = QPushButton(self.groupBox)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u" Scan", None))
        self.scan_button.clicked.connect(lambda: self.populate_tree_view(self.path_line_edit.text(), recursive=self.recursive_check_box.isChecked()))
        sizePolicy.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy)
        self.scan_button.setMinimumSize(QSize(20, 20))
        self.scan_button.setAutoFillBackground(False)
        self.scan_button.setStyleSheet(u"")
        self.set_widget_icon(self.scan_button, "refresh-arrows.png")
        self.scan_button.setFlat(False)
        self.gridLayout_2.addWidget(self.scan_button, 1, 1, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.directory_tree_view = QTreeView(self.left_widget_container)
        self.directory_tree_view.setObjectName(u"directory_tree_view")
        sizePolicy2.setHeightForWidth(self.directory_tree_view.sizePolicy().hasHeightForWidth())
        self.directory_tree_view.setSizePolicy(sizePolicy2)
        self.directory_tree_view.setMinimumSize(QSize(300, 200))
        self.directory_tree_view.setAlternatingRowColors(True)

        self.gridLayout_3.addWidget(self.directory_tree_view, 1, 0, 1, 1)

        self.splitter.addWidget(self.left_widget_container)

        ### Set up right widget container (inspector, execute button) ###
        self.right_widget_container = QWidget(self.splitter)
        self.right_widget_container.setObjectName(u"right_widget_container")
        self.splitter.addWidget(self.right_widget_container)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.right_widget_container.sizePolicy().hasHeightForWidth())
        self.right_widget_container.setSizePolicy(sizePolicy6)
        self.right_widget_container.setMinimumSize(QSize(325, 300))
        self.gridLayout_4 = QGridLayout(self.right_widget_container)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inspector_scroll_area = QScrollArea(self.right_widget_container)
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

        self.execute_push_button = QPushButton(self.right_widget_container)
        self.execute_push_button.setObjectName(u"execute_push_button")
        self.execute_push_button.setText(QCoreApplication.translate("MainWindow", u" Execute", None))
        sizePolicy5.setHeightForWidth(self.execute_push_button.sizePolicy().hasHeightForWidth())
        self.execute_push_button.setSizePolicy(sizePolicy5)
        self.execute_push_button.setMinimumSize(QSize(120, 50))
        self.set_widget_icon(self.execute_push_button, "play-button.png")

        self.gridLayout_4.addWidget(self.execute_push_button, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.scan_button.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def folder_select(self, line_edit: QLineEdit) -> None:
        """
        Opens a file dialog to select an input or folder.

        :param line_edit: A QLineEdit object where the selected folder path will be set.
        :return: None
        """
        folderpath = QFileDialog.getExistingDirectory(self, f"Select input folder")
        line_edit.setText(folderpath)

    def set_window_icon(self, window: QWidget) -> None:
        """
        Sets the window icon for a given widget.

        :param widget: A QWidget object for which the icon will be set.
        :return: None
        """
        icon = QIcon()
        data_path = os.path.abspath(os.path.dirname(__file__))
        icon_path = os.path.join(data_path, "gui_assets", "folder.png")
        if os.path.isfile(os.path.join(icon_path)):
            icon.addFile(icon_path)
            window.setWindowIcon(icon)
    
    def set_widget_icon(self, widget: QWidget, icon_name: str) -> None:
        """
        Sets the widget icon for a given widget.

        :param widget: A QWidget object for which the icon will be set.
        :param icon_name: A string representing the icon file name.
        :return: None
        """
        icon = QIcon()
        data_path = os.path.abspath(os.path.dirname(__file__))
        icon_path = os.path.join(data_path, "gui_assets", icon_name)
        print(f"icon_path: {icon_path}")
        if os.path.isfile(icon_path):
            icon.addFile(icon_path)
            widget.setIcon(icon)
    
    def populate_tree_view(self, path: str, recursive: bool=True, files: bool=False) -> None:
        """
        Populates the directory tree view with a list of files and/or folders.

        :param path: A string representing the directory path to scan.
        :param recursive: A boolean indicating whether to scan directories recursively. Default is True.
        :param files: A boolean indicating whether to include files in the scan results. Default is True.
        :return: None
        """
    
        try:
            if not recursive and not files:
                model = QStandardItemModel()
                self.directory_tree_view.setHeaderHidden(True)

                dir = QDir(path)
                dir.setFilter(QDir.Dirs | QDir.NoDotAndDotDot)

                for folder in dir.entryList():
                    item = QStandardItem(folder)
                    item.setCheckState(Qt.Unchecked)
                    item.setCheckable(True)
                    data_path = os.path.abspath(os.path.dirname(__file__))
                    icon_path = os.path.join(data_path, "gui_assets", "folder.png")
                    item.setIcon(QIcon(icon_path))

                    model.appendRow(item)
                self.directory_tree_view.setModel(model)
                print(f"Set tree view to non-recursive without files at path: {path}")
            
            elif files:
                model = CheckableFileSystemModel()
                model.setRootPath(path)
                self.directory_tree_view.setModel(model)
                index = model.index(path)
                self.directory_tree_view.setRootIndex(index)
                print(f"Set tree view to recursive with files at path: {path}")

        except Exception as e:
            self.messagebox("error", "Error Scanning Directory", str(e))
            return
    
    def messagebox(self, message_type:str, title:str, message:str) -> bool:
        """
        Displays a message box with a given title and message.

        :param message_type: A string indicating the type of message box to display. Expected: "warning", "error", or "info".
        :param title: A string containing the error title of the message box.
        :param message: A string containing the error message.
        :param worker_thread: A QThread object. (Optional)
        :return: A boolean indicating whether the user clicked 'OK' or 'Cancel'.
        """
        print(f"message_type: {message_type}")
        msg_box = QMessageBox()
        self.set_window_icon(window=msg_box)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setWindowModality(Qt.ApplicationModal)
        msg_box.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint)

        if message_type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        elif message_type == "error":
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setStandardButtons(QMessageBox.Ok)
        elif message_type == "info":
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setStandardButtons(QMessageBox.Ok)
        else:
            print(f"Invaild message type: {message_type}")
        
        button = msg_box.exec()

        if button == QMessageBox.Ok:
            return True
        elif button == QMessageBox.Cancel:
            return False


class CheckableFileSystemModel(QFileSystemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._checked = {}  # path → Qt.CheckState

    def flags(self, index):
        default = super().flags(index)
        if not index.isValid():
            return default

        # Only column 0 gets a checkbox
        if index.column() == 0:
            return default | Qt.ItemIsUserCheckable

        return default

    def data(self, index, role):
        if role == Qt.CheckStateRole and index.column() == 0:
            path = self.filePath(index)
            return self._checked.get(path, Qt.Unchecked)

        return super().data(index, role)

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole and index.column() == 0:
            path = self.filePath(index)
            self._checked[path] = value

            # If it's a folder, recursively apply to all children
            if self.isDir(index):
                self._set_children_recursive(index, value)

            self.dataChanged.emit(index, index, [Qt.CheckStateRole])
            return True

        return super().setData(index, value, role)

    def _set_children_recursive(self, parent_index, value):
        """Recursively apply check state to all descendants."""
        rows = self.rowCount(parent_index)

        for row in range(rows):
            child = self.index(row, 0, parent_index)
            child_path = self.filePath(child)

            # Set check state
            self._checked[child_path] = value
            self.dataChanged.emit(child, child, [Qt.CheckStateRole])

            # If child is a folder, recurse
            if self.isDir(child):
                self._set_children_recursive(child, value)


if __name__ == "__main__":
    freeze_support()
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())