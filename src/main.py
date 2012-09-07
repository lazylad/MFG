'''
Created on Aug 30, 2012

@author: sandeep
'''
import wx
import logging
from windows.login import Login
from conf.logger import *

if __name__ == "__main__":
    loadDefaults()
    app = wx.App(False)
    frame = Login()
    frame.Show()
    app.MainLoop()