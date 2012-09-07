'''
Created on Aug 30, 2012

@author: sandeep
'''
import wx
import logging
import hashlib
import sqlite3 as lite
from conf import params
from screen1 import Screen1
class Login(wx.Frame):
    def __init__(self):
        logging.info("Login page started")
        wx.Frame.__init__(self, None, wx.ID_ANY,"Log in",style = wx.CLOSE_BOX| wx.SYSTEM_MENU | wx.CAPTION,size = params.LOGIN_SIZE )
        #Our panel
        basepanel=wx.Panel(self,-1) 
        #some custom fonts
        font1 = wx.Font(10, wx.FONTFAMILY_ROMAN,wx.FONTSTYLE_SLANT, wx.LIGHT) 
        font = wx.Font(15, wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_ITALIC, wx.NORMAL)

        #this is the BoxSizer
        #syntax:wx.BoxSizer(orientation)
        basebox=wx.BoxSizer(wx.VERTICAL) 

        #This is our name field
        ip_box=wx.BoxSizer(wx.HORIZONTAL) #A boxresizer
        ip_label=wx.StaticText(basepanel,label="Username") #Label "Username"
        ip_label.SetFont(font1)#setting custom font to label
        self.ip_text=wx.TextCtrl(basepanel,-1,"user1") #TextField for Username

        #adding Username label & its textfield to ip_box BoxSizer
        #syntax:Add(parent,id,proportion,spacing)
        ip_box.Add(ip_label,-1,wx.ALL,5) #wx.ALL means spacing of 5px in "all direction"
        ip_box.Add(self.ip_text,-1,wx.ALL,5) 

        #password field
        pwd_box=wx.BoxSizer(wx.HORIZONTAL) 
        pwd_label=wx.StaticText(basepanel,label="Password") 
        pwd_label.SetFont(font1) 
        self.pwd_text=wx.TextCtrl(basepanel,-1,"user1",style = wx.TE_PASSWORD) 

        pwd_box.Add(pwd_label,-1,wx.ALL,5) 
        pwd_box.Add(self.pwd_text,-1,wx.ALL,5) 

        #WELCOME title
        title_box=wx.BoxSizer(wx.HORIZONTAL) 
        title_text=wx.StaticText(basepanel,label="Login") #a non-editable text
        title_text.SetFont(font) 
        title_box.Add(title_text,-1) 

        #OK button
        bt_box=wx.BoxSizer(wx.HORIZONTAL) 
        ok_bt=wx.Button(basepanel,-1,"Login") 
        cancel_bt=wx.Button(basepanel,wx.ID_CANCEL,"Cancel") 
        bt_box.Add(ok_bt,-1,wx.ALL,5) 
        bt_box.Add(cancel_bt,-1,wx.ALL,5) 

        #adding everything to basebox
        basebox.Add(title_box,0,wx.CENTER,10) 
        basebox.Add(wx.StaticLine(basepanel),0,wx.ALL|wx.EXPAND,5) 
        basebox.Add(ip_box,0,wx.CENTER,10) 
        basebox.Add(pwd_box,0,wx.CENTER,10) 
        basebox.Add(bt_box,0,wx.CENTER,10) 

        #adding basebox to basepanel
        basepanel.SetSizer(basebox)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText(' Ready.....') 
        self.Center()
        
        ##binding
        self.Bind(wx.EVT_BUTTON, self.OnLogin, id=ok_bt.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnExit, id=cancel_bt.GetId())
        
    def OnExit(self, event):
        logging.info("application is exiting....")
        self.Close()
        
    def OnLogin(self, event):
        logging.info("checking db")
        username = self.ip_text.GetValue()
        password = self.pwd_text.GetValue()
        if self.Sanitize(username,password) == True :
            self.Authenticate(username,password)
        else :
            logging.info("sanitization failed")
            self.SetStatusText("invalid username or password")
    def Sanitize(self,username,password):
        if not username or not password :
            return False
        return True        
    def Authenticate(self,username,password):
        h = hashlib.md5()
        h.update(password)
        con = lite.connect(params.MFG_CONFIG_DB)
        with con:
            cur = con.cursor()
            cur.execute("SELECT Password from Accounts where username = ?",(username,))
            while True:
                row = cur.fetchone()
                if  row:
                    if row[0]==h.hexdigest() :
                        logging.info('authentication success')
                        frame = Screen1()
                        #frame.Show()
                        self.Close()
                    break
                else :
                    logging.error('invalid username or password')
                    self.SetStatusText("invalid username or password")
                    self.ip_text.SetValue("")
                    self.pwd_text.SetValue("")
                    break    
            