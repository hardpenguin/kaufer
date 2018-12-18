#!/usr/bin/python3

import sys
import signal

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import stores
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
      self.query_input.returnPressed.connect(self.SearchAction)
      layout.addWidget(self.query_input)

      self.store_checkboxes = []
      for store, link in stores.search_links.items():
         checkbox = QCheckBox(store)
         checkbox.setCheckState(2)
         self.store_checkboxes.append(checkbox)
         layout.addWidget(checkbox)

      button_size = QSize(150, 40)

      buttons = []
      search_button = QPushButton("Search")
      buttons.append(search_button)
      search_button.clicked.connect(self.SearchAction)

      quit_button = QPushButton("Quit")
      buttons.append(quit_button)
      quit_button.clicked.connect(self.QuitAction)

      for button in buttons:
         button.setFixedSize(button_size)
         layout.addWidget(button)

      self.setLayout(layout)

   def SearchAction(self):
      action_links = stores.search_links.copy()
      i = 0
      for store, link in stores.search_links.items():
         if self.store_checkboxes[i].isChecked() == False:
            action_links.pop(store)
         i = i + 1
      Kaufer.Search(self.query_input.text(), action_links)

   def QuitAction(self):
      print("Exiting")
      sys.exit()

window = KauferGUI()
window.show()
print("Käufer GUI started")
app.exec_()
