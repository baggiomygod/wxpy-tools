import wx
import os,sys

# 解决不支持相对路径问题，兼容win和linux路径
os.chdir(sys.path[0])
class Layout(wx.Frame):
  def __init__(self, parent, title):
    super(Layout, self).__init__(parent, title=title, size=(600, 800))

  def InitUI(self):
    self.panel = wx.Panel(self)

    self.panel.SetBackgroundColour('gray')

    self.LoadImages()

    self.mincol.SetPosition((20,20))
    self.bardejov.SetPosition((40,60))
    self.rotunda.SetPositio((170,50))
  
  def LoadImages(self):
    self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('../assets/images/mincol.jpg', wx.BITMAP_TYPE_ANY))
    self.bardejov = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('../assets/images/bardejov.jpg', wx.BITMAP_TYPE_ANY))
    self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('../assets/images/rotunda.jpg', wx.BITMAP_TYPE_ANY))

def main():
  app = wx.App()
  layout = Layout(None, title="layout")
  layout.Show()
  app.MainLoop()

if __name__ == '__main__':
  main()