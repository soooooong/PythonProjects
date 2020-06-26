'''
1，添加组播地址获取
2，进度条的动态适应窗口

'''

__author__ = 'song'
import wx
import win32api
import sys
import os
import wx.lib.agw.aui as aui

APP_TITLE = u"升级监测工具"
rootpath = os.getcwd()
print('--------')
print(rootpath)
#APP_ICON = 'D:/GitHub/PythonProjects/hello/socket_module/res/1.ico'
APP_ICON = './res/1.ico'


class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''
    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()

    id_help = wx.NewId()
    id_about = wx.NewId()

    def __init__(self, Parent):
        '''构造函数'''
        wx.Frame.__init__(self, Parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozemn") == "windows_exe":
            exeName = win32api.GetModuleFileName(
                win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else:
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.tb1 = self._CreateToolBar()
        self.tb2 = self._CreateToolBar()
        #self.tbv = self._CreateToolBar('V')

        p_left = wx.Panel(self, -1)
        
        p_center0 = wx.Panel(self, -1)
        

        p_center1 = wx.Panel(self, -1)
        p_bottom = wx.Panel(self, -1)


        btn = wx.Button(p_left, -1, u'切换', pos=(30,200), size=(100, -1))
        btn.Bind(wx.EVT_BUTTON, self.OnSwitch)

        texto = wx.StaticText(p_center0, -1, u'xia',
                              pos=(0, 0), size=(200, -1), style=wx.ALIGN_LEFT)
        text1 = wx.StaticText(p_center1, -1, u'我是第2页',
                              pos=(0, 0), size=(200, -1), style=wx.ALIGN_LEFT)


        self._CreateprogressBar(p_center0)

        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self._mgr.AddPane(self.tb1,
                           aui.AuiPaneInfo().Name("ToolBar1").Caption(
                               u"工具条").ToolbarPane().Top().Row(0).Position(0).Floatable(False)
                           )
   
        self._mgr.AddPane(self.tb2,
                          aui.AuiPaneInfo().Name("ToolBar2").Caption(
                              u"工具条").ToolbarPane().Top().Row(0).Position(1).Floatable(True)
                          )
        '''
        self._mgr.AddPane(self.tbv,
                          aui.AuiPaneInfo().Name("ToolBarV").Caption(
                              u"工具条").ToolbarPane().Right().Floatable(True)
                          )
        '''
        self._mgr.AddPane(p_left,
                          aui.AuiPaneInfo().Name("LeftPanel").Left().Layer(1).MinSize((200, -1)).Caption(u"操作区").MinimizeButton(True).MaximizeButton(True).CloseButton(True)
                          )

        self._mgr.AddPane(p_center0,
                          aui.AuiPaneInfo().Name("CenterPanel0").CenterPane().Show()
                          )

        self._mgr.AddPane(p_center1,
                          aui.AuiPaneInfo().Name("CenterPanel1").CenterPane().Hide()
                          )

        self._mgr.AddPane(p_bottom,
                          aui.AuiPaneInfo().Name("BottomPanel").Bottom().MinSize(
                              (-1, 100)).Caption(u"消息区").CaptionVisible(False).Resizable(True)
                          )


        self._mgr.Update()

    def _CreateprogressBar(self,parent):
        for i in range(0,100,1):
            gauge=wx.Gauge(parent,1001,100,pos=(2,i*20),size=(wx.DefaultSize),style = wx.ALIGN_LEFT)
        ScrollBar = wx.ScrollBar(parent,1002,pos=(2,0*20),size=(wx.DefaultSize),style =wx.SB_VERTICAL) 
        ScrollBar.SetScrollbar(0, 16, 50, 15,True)  




        
        #gauge.SetBezelFace(3)
        #gauge.SetShadowWidth(3)
        #gauge.SetValue(50)
        return gauge
        



    def _CreateToolBar(self, d='H'):
        '''创建工具栏'''

        bmp_open = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY)
        bmp_save = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY)
        bmp_help = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY)
        bmp_about = wx.Bitmap(APP_ICON, wx.BITMAP_TYPE_ANY)

        if d.upper() in ['V', 'VERTICAL']:
            tb = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                                agwStyle=aui.AUI_TB_TEXT | aui.AUI_TB_VERTICAL)
        else:
            tb = aui.AuiToolBar(self, -1, wx.DefaultPosition,
                                wx.DefaultSize, agwStyle=aui.AUI_TB_TEXT)
        tb.SetToolBitmapSize(wx.Size(16, 16))

        tb.AddSimpleTool(self.id_open, u'打开', bmp_open, u'打开文件')
        tb.AddSimpleTool(self.id_save, u'保存', bmp_save, u'保存文件')
        tb.AddSeparator()
        tb.AddSimpleTool(self.id_help, u'帮助', bmp_help, u'帮助')
        tb.AddSimpleTool(self.id_about, u'关于', bmp_about, u'关于')

        tb.Realize()
        return tb

    def OnSwitch(self, evt):
        '''切换信息显示窗口'''
        print('test button')
        p0 = self._mgr.GetPane('CenterPanel0')
        p1 = self._mgr.GetPane('CenterPanel1')

        p0.Show(not p0.IsShown())
        p1.Show(not p1.IsShown())

        self._mgr.Update()


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True


if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()
