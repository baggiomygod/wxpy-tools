import wx.html
import wx
from src.utils.docx.docx2html import read_word2html
import os
import sys

os.chdir(sys.path[0])

# 展示样式不好 docx 转html  展示
class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        htmlStr = read_word2html('./docx/2.docx')
        html.SetPage(htmlStr)


app = wx.App()
frm = MyHtmlFrame(None, "Simple HTML")
frm.Show()
app.MainLoop()
