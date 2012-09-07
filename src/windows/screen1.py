'''
Created on Aug 31, 2012

@author: sandeep
'''
import wx
import logging
import wx.lib.agw.labelbook as LB
from wx.lib.agw.fmresources import *

class PageOne(wx.Panel):
    def __init__(self, parent):
        logging.info("loading class")
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageTwo(wx.Panel):
    def __init__(self, parent):
        logging.info("loading class")        
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class PageThree(wx.Panel):
    def __init__(self, parent):
        logging.info("loading class")        
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))





class Screen1(wx.Frame):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        logging.info("generating screen-1")
        wx.Frame.__init__(self, None, wx.ID_ANY,"screen 1")
           
        #some custom fonts
        
        p = wx.Panel(self)
        #nb = wx.Notebook(p)
        style = self.GetBookStyles()
        nb = LB.LabelBook(p, -1, agwStyle = style)
        # create the page windows as children of the notebook
        #nb.SetFontBold(True)
        nb.SetFontSizeMultiple(2)
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "Page 1")
        nb.AddPage(page2, "Page 2")
        nb.AddPage(page3, "Page 3")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        self.InitUI()
    def InitUI(self):    
        logging.info('initialising UI for screen 1')
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        #toolbar = self.CreateToolBar()
        """qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit')
        toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool,None)
        """
        self.Centre()
        self.Show(True)
        top = self.GetTopLevelParent()
        top.Maximize()
        
        
    def OnQuit(self, e):
        logging.info("application is exiting....")
        self.Close()
       
    def GetBookStyles(self):

        style = INB_FIT_BUTTON
        style |= INB_SHOW_ONLY_TEXT
        #style |= INB_SHOW_ONLY_IMAGES
        style |= INB_USE_PIN_BUTTON
        style |= INB_DRAW_SHADOW
        style |= INB_WEB_HILITE
        style |= INB_GRADIENT_BACKGROUND
        style |= INB_BORDER
        style |= INB_FIT_LABELTEXT
        style |= INB_NO_RESIZE
        style |= INB_BORDER
        #self.book.SetFontBold(self.boldtext.GetValue())

        return style
