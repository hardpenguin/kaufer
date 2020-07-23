#!/usr/bin/python3

import sys
import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from kaufer import Kaufer

signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication([])

class KauferGUI(QWidget):

   def __init__(self):
      QWidget.__init__(self)
      self.setWindowTitle('Käufer')
      self.setMinimumWidth(200)

      layout = QVBoxLayout()
      layout.setAlignment(Qt.AlignCenter)

      self.query_input = QLineEdit()
      self.query_input.setMaximumWidth(150)
      self.query_input.setPlaceholderText("Game title")
      self.query_input.returnPressed.connect(self.search_action)
      layout.addWidget(self.query_input)

      self.store_checkboxes = []
      self.app = Kaufer()
      for store in self.app.stores:
         checkbox = QCheckBox(store["name"])
         if store["enabled"]:
            checkbox.setCheckState(2)
         self.store_checkboxes.append(checkbox)
         layout.addWidget(checkbox)

      button_size = QSize(150, 40)

      buttons = []
      search_button = QPushButton("Search")
      buttons.append(search_button)
      search_button.clicked.connect(self.search_action)

      save_button = QPushButton("Save")
      buttons.append(save_button)
      save_button.clicked.connect(self.save_action)

      quit_button = QPushButton("Quit")
      buttons.append(quit_button)
      quit_button.clicked.connect(self.quit_action)

      for button in buttons:
         button.setFixedSize(button_size)
         layout.addWidget(button)

      self.setLayout(layout)

   def update_enabled_status(self):
      i = 0
      for checkbox in self.store_checkboxes:
         if self.store_checkboxes[i].isChecked() == False:
            self.app.stores[i]["enabled"] = False
         else:
            self.app.stores[i]["enabled"] = True
         i = i + 1

   def search_action(self):
      self.update_enabled_status()
      print("Searching \"%s\"" % self.query_input.text())
      self.app.search(self.query_input.text())

   def save_action(self):
      self.update_enabled_status()
      self.app.save_config()
      print("Config saved")

   def quit_action(self):
      print("Exiting")
      sys.exit()

window = KauferGUI()
window.show()
print("Käufer GUI started")
app.exec_()
