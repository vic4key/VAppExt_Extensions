import sys, os, json
import VExt

__name__    = "Example PyQt5"
__version__ = "1.x"
__author__  = "Vic P."
__summary__ = "The summary of the extension"
__url__     = "https://github.com/vic4key/VAppExt.git"

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WidgetGallery(QDialog):
  def __init__(self, parent=None):
    super(WidgetGallery, self).__init__(parent)

    self.originalPalette = QApplication.palette()

    styleComboBox = QComboBox()
    styleComboBox.addItems(QStyleFactory.keys())

    styleLabel = QLabel("&Style:")
    styleLabel.setBuddy(styleComboBox)

    self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
    self.useStylePaletteCheckBox.setChecked(True)

    disableWidgetsCheckBox = QCheckBox("&Disable widgets")

    self.createTopLeftGroupBox()
    self.createTopRightGroupBox()
    self.createBottomLeftTabWidget()
    self.createBottomRightGroupBox()
    self.createProgressBar()

    styleComboBox.activated[str].connect(self.changeStyle)
    self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
    disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
    disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
    disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
    disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

    topLayout = QHBoxLayout()
    topLayout.addWidget(styleLabel)
    topLayout.addWidget(styleComboBox)
    topLayout.addStretch(1)
    topLayout.addWidget(self.useStylePaletteCheckBox)
    topLayout.addWidget(disableWidgetsCheckBox)

    mainLayout = QGridLayout()
    mainLayout.addLayout(topLayout, 0, 0, 1, 2)
    mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
    mainLayout.addWidget(self.topRightGroupBox, 1, 1)
    mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
    mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
    mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
    mainLayout.setRowStretch(1, 1)
    mainLayout.setRowStretch(2, 1)
    mainLayout.setColumnStretch(0, 1)
    mainLayout.setColumnStretch(1, 1)
    self.setLayout(mainLayout)

    self.setWindowTitle("Styles")

    default_style = "Fusion"
    self.changeStyle(default_style)
    styleComboBox.setCurrentText(default_style)

  def changeStyle(self, styleName):
    QApplication.setStyle(QStyleFactory.create(styleName))
    self.changePalette()

  def changePalette(self):
    if (self.useStylePaletteCheckBox.isChecked()):
      QApplication.setPalette(QApplication.style().standardPalette())
    else:
      QApplication.setPalette(self.originalPalette)

  def advanceProgressBar(self):
    curVal = self.progressBar.value()
    maxVal = self.progressBar.maximum()
    self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

  def createTopLeftGroupBox(self):
    self.topLeftGroupBox = QGroupBox("Group 1")

    radioButton1 = QRadioButton("Radio button 1")
    radioButton2 = QRadioButton("Radio button 2")
    radioButton3 = QRadioButton("Radio button 3")
    radioButton1.setChecked(True)

    checkBox = QCheckBox("Tri-state check box")
    checkBox.setTristate(True)
    checkBox.setCheckState(Qt.PartiallyChecked)

    layout = QVBoxLayout()
    layout.addWidget(radioButton1)
    layout.addWidget(radioButton2)
    layout.addWidget(radioButton3)
    layout.addWidget(checkBox)
    layout.addStretch(1)
    self.topLeftGroupBox.setLayout(layout)    

  def createTopRightGroupBox(self):
    self.topRightGroupBox = QGroupBox("Group 2")

    defaultPushButton = QPushButton("Default Push Button")
    defaultPushButton.setDefault(True)

    togglePushButton = QPushButton("Toggle Push Button")
    togglePushButton.setCheckable(True)
    togglePushButton.setChecked(True)

    flatPushButton = QPushButton("Flat Push Button")
    flatPushButton.setFlat(True)

    layout = QVBoxLayout()
    layout.addWidget(defaultPushButton)
    layout.addWidget(togglePushButton)
    layout.addWidget(flatPushButton)
    layout.addStretch(1)
    self.topRightGroupBox.setLayout(layout)

  def createBottomLeftTabWidget(self):
    self.bottomLeftTabWidget = QTabWidget()
    self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
        QSizePolicy.Ignored)

    tab1 = QWidget()
    tableWidget = QTableWidget(10, 10)

    tab1hbox = QHBoxLayout()
    tab1hbox.setContentsMargins(5, 5, 5, 5)
    tab1hbox.addWidget(tableWidget)
    tab1.setLayout(tab1hbox)

    tab2 = QWidget()
    textEdit = QTextEdit()

    textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                "How I wonder what you are.\n" 
                "Up above the world so high,\n"
                "Like a diamond in the sky.\n"
                "Twinkle, twinkle, little star,\n" 
                "How I wonder what you are!\n")

    tab2hbox = QHBoxLayout()
    tab2hbox.setContentsMargins(5, 5, 5, 5)
    tab2hbox.addWidget(textEdit)
    tab2.setLayout(tab2hbox)

    self.bottomLeftTabWidget.addTab(tab1, "&Table")
    self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

  def createBottomRightGroupBox(self):
    self.bottomRightGroupBox = QGroupBox("Group 3")
    self.bottomRightGroupBox.setCheckable(True)
    self.bottomRightGroupBox.setChecked(True)

    lineEdit = QLineEdit('s3cRe7')
    lineEdit.setEchoMode(QLineEdit.Password)

    spinBox = QSpinBox(self.bottomRightGroupBox)
    spinBox.setValue(50)

    dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
    dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
    slider.setValue(40)

    scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
    scrollBar.setValue(60)

    dial = QDial(self.bottomRightGroupBox)
    dial.setValue(30)
    dial.setNotchesVisible(True)

    layout = QGridLayout()
    layout.addWidget(lineEdit, 0, 0, 1, 2)
    layout.addWidget(spinBox, 1, 0, 1, 2)
    layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
    layout.addWidget(slider, 3, 0)
    layout.addWidget(scrollBar, 4, 0)
    layout.addWidget(dial, 3, 1, 2, 1)
    layout.setRowStretch(5, 1)
    self.bottomRightGroupBox.setLayout(layout)

  def createProgressBar(self):
    self.progressBar = QProgressBar()
    self.progressBar.setRange(0, 10000)
    self.progressBar.setValue(0)

    timer = QTimer(self)
    timer.timeout.connect(self.advanceProgressBar)
    timer.start(1000)

def main():
  app = QApplication.instance() if QApplication.instance() else QApplication([])
  gallery = WidgetGallery()
  gallery.show()
  app.exec_()

def VExt_Load():
  return

def VExt_Unload():
  return

class Window(VExt.UI.Window):
  def __init__(self):
    super().__init__()
    return

  def on_menu_define(self):
    result = super().on_menu_define()
    result = [
      {
        "caption": "Display UI",
        "index": 1,
        "children": [],
      },
      {
        "caption": "Information",
        "index": 2,
        "children": [],
      },
    ]
    return result

  def on_menu_execute(self, idx, lp):
    super().on_menu_execute(idx, lp)
    if idx == 1: main()
    elif idx == 2: VExt.API.message_box(f"{__name__} {__version__}\n\nCopyright (c) {__author__}", f"Information")
    return

  def on_menu_update(self, idx, lp):
    result = super().on_menu_update(idx, lp)
    result = (True, False)
    return result
