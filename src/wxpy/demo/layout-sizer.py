import wx
import os, sys

# 解决不支持相对路径问题，兼容win和linux路径
os.chdir(sys.path[0])


class LayoutSizer(wx.Frame):
    def __init__(self, parent, title):
        super(LayoutSizer, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#fff')

        vbox = wx.BoxSizer(wx.VERTICAL)

        innerPan = wx.Panel(panel)
        innerPan.SetBackgroundColour('#000')

        # wx.EXPAND 扩大，以填补提供给它的空间(wx.GROW是一样的)
        # wx.ALL wx.RIGHT | wx.LEFT | wx.TOP | wx.BOTTOM
        vbox.Add(innerPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vbox)


def main():
    app = wx.App()
    sizer = LayoutSizer(None, title='sizer')
    sizer.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
