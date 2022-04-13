import wx
import os
import sys

# 解决不支持相对路径问题，兼容win和linux路径
os.chdir(sys.path[0])


class Layout(wx.Frame):
    def __init__(self, parent, title):
        super(Layout, self).__init__(parent, title=title, size=(600, 800))
        self.rotunda = None
        self.bardeJov = None
        self.panel = None
        self.minCol = None
        self.initUi()
        self.Centre()

    def initUi(self):
        # A panel is a window on which controls are placed.
        # panel面板是放置控件的窗口
        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour('white')
        # self.SetTransparent(2000) # 设置透明度
        self.LoadImages()

        # 绝对定位
        self.minCol.SetPosition((20, 20))
        self.bardeJov.SetPosition((40, 60))
        self.rotunda.SetPosition((170, 50))

    def LoadImages(self):
        self.minCol = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                      wx.Bitmap('../assets/images/mincol.jpg', wx.BITMAP_TYPE_ANY))
        self.bardeJov = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                        wx.Bitmap('../assets/images/bardejov.jpg', wx.BITMAP_TYPE_ANY))
        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                       wx.Bitmap('../assets/images/rotunda.jpg', wx.BITMAP_TYPE_ANY))


def main():
    app = wx.App()
    layout = Layout(None, title="layout")
    layout.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
