import wx

# 解决不支持相对路径问题，兼容win和linux路径
import os,sys
os.chdir(sys.path[0])
APP_EXIT = 1

class IconDemo(wx.Frame):
  def __init__(self, *args, **kw):
      super(IconDemo, self).__init__(*args, **kw)

      self.InitUI()
  
  def InitUI(self):
     menubar = wx.MenuBar()
     fileMenu = wx.Menu()

     qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\\tCtrl+Q')
    #  '/' 路径windows不识别
     qmi.SetBitmap(wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\demo\\assets\\icons\\quit.png'))
     fileMenu.Append(qmi)
    
    # 将菜单绑定到自定义onQuit方法
     self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

     menubar.Append(fileMenu, '&File')
     self.SetMenuBar(menubar)

     self.SetSize((500, 300))
     self.SetTitle('icon menu')
     self.Center()

  def OnQuit(self, e):
    self.Close()

def main():
  app = wx.App()
  iconDemo = IconDemo(None)
  iconDemo.Show()
  app.MainLoop()

if (__name__ == '__main__'):
  main()