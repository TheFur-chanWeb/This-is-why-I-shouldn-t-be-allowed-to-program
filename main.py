# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pynput import keyboard
from pyautogui import press, hotkey, keyDown, keyUp
from Tkinter import Tk
import gui
import sys
import string
import random
import threading
import win32clipboard

zalgochars = [ "̍","̎","̄","̅","̿","̑","̆","̐","͒","͗",
               "͑","̇","̈","̊","͂","̓","̈́","͊","͋","͌",
               "̃","̂","̌","͐","́","̋","̏","̓",
               "̔","̽","̉","ͣ","ͤ","ͥ","ͦ","ͧ","ͨ","ͩ",
               "ͪ","ͫ","ͬ","ͭ","ͮ","ͯ","̾","͛","͆","̚",
               "̖","̗","̘","̙","̜","̝","̞","̟","̠","̤",
               "̥","̦","̩","̪","̫","̬","̭","̮","̯","̰",
               "̱","̲","̳","̹","̺","̻","̼","ͅ","͇","͈",
               "͉","͍","͎","͓","͔","͕","͖","͙","͚","̣"]

class why(QtGui.QMainWindow, gui.Ui_MainWindow,threading.Thread):
  def __init__(self):
    super(why, self).__init__()
    self.setupUi(self)
    QtGui.QApplication.processEvents()
    self.enabled=False
    self.aesCaps=False
    self.Start.setEnabled(False)
    self.togglekey=''
    self.toggleswitch.clicked.connect(self.getToggle)
    self.Killme.clicked.connect(self.doExit)
    self.Start.clicked.connect(self.startListenerThread)
    self._stop_event = threading.Event()
    self.aestheticsSettings.addItems(["( ( ( l o w e r c a s e ) ) )","( ( ( C A P I T A L S ) ) )"])
    self.zalgoSettings.addItems(["Low","Med","High"])
    self.owoSettings.addItems(["Wepwase R's", "Wepwase L's", "Wepwase Bowth"])

  def doExit(self):
    self.close()

  def closeEvent(self, event):
    try:self.lis.stop()
    except:pass
    self.stop()
    sys.exit()

  def startListener(self):
    self.lis = keyboard.Listener(on_press=self.Listener)
    self.lis.start()
    self.lis.join()

  def startListenerThread(self):
    self.enabled=True
    self.endisable.setText("Enabled")
    t=threading.Thread(target=self.startListener)
    t.start()

  def stop(self):
      self._stop_event.set()

  def stopped(self):
    return self._stop_event.is_set()

  def Listener(self,key):
    try: k = key.char
    except: k = key.name
    if key==self.togglekey:
      if self.enabled:
        self.endisable.setText("Disabled")
        self.enabled=False
      else:
        self.endisable.setText("Enabled")
        self.enabled=True
    if self.Spang.isChecked() and self.enabled:
      if k in string.digits+string.ascii_letters+string.punctuation:
        press("capslock")
    elif self.aesthetics.isChecked() and self.enabled:
      if str(self.aestheticsSettings.currentText())=="( ( ( C A P I T A L S ) ) )":
        if not self.aesCaps:
          self.aesCaps=True
          press("capslock")
      if key == keyboard.Key.caps_lock:
        press("capslock")
      if k in string.digits+string.ascii_letters+string.punctuation:
        press("space")
    elif self.zalgo.isChecked() and self.enabled and k in string.digits+string.ascii_letters+string.punctuation+"space":
      if str(self.zalgoSettings.currentText())=="Low":
        txt=''.join([random.choice(zalgochars).strip("\n").strip("\t").strip("\r") for i in range(random.randint(2,6))])
      if str(self.zalgoSettings.currentText())=="Med":
        txt=''.join([random.choice(zalgochars).strip("\n").strip("\t").strip("\r") for i in range(random.randint(5,10))])
      if str(self.zalgoSettings.currentText())=="High":
        txt=''.join([random.choice(zalgochars).strip("\n").strip("\t").strip("\r") for i in range(random.randint(8,15))])
      r = Tk()
      r.withdraw()
      r.clipboard_clear()
      r.clipboard_append(txt)
      r.update()
      r.destroy()
      press(self.togglename)
      hotkey("ctrl","v")
      press(self.togglename)
    elif self.owo.isChecked() and self.enabled:
      if str(self.owoSettings.currentText())=="Wepwase R's":
        if k in "r":
          press("backspace")
          press("w")
      if str(self.owoSettings.currentText())=="Wepwase L's":
        if k in "l":
          press("backspace")
          press("w")
      if str(self.owoSettings.currentText())=="Wepwase Bowth":
        if k in "rl":
          press("backspace")
          press("w")
        
  def toggleListener(self,key):
    try: k = key.char
    except: k = key.name
    self.togglekey=key
    self.togglename=k
    self.toggleswitch.setText("Toggle: "+k)
    self.tlis.stop()
    self.Start.setEnabled(True)
    
  def getToggle(self):
    self.tlis = keyboard.Listener(on_press=self.toggleListener)
    self.tlis.start()
    self.tlis.join()
        
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = why()
  window.show()
  sys.exit(app.exec_())
