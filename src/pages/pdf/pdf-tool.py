# 选择文件
# 左右展示docx pdf
import wx
import os
import sys
import time
from src.utils.pdf.tools.docxToPdf.docxToPdf import coverPdf

os.chdir(sys.path[0])

ID_SPLITTER = 300


class DocView:
    def __init__(self, parent, *backgroundColor):
        cPan = wx.Panel(parent)
        cPan.SetBackgroundColour(*backgroundColor)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(cPan, wx.ID_ANY, flag=wx.EXPAND | wx.ALL, border=0)
        parent.SetSizer(vbox)

class ToolPage(wx.Frame):
    def __init__(self, *args, **kw):
        super(ToolPage, self).__init__(*args, **kw)
        self.splitter = None

        self._TextBox = None
        self.initUi()

    def initUi(self):
        self.initMenus()
        # wx.SP_BORDER绘制窗口的边框，非三维的样式
        self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
        self.splitter.SetMinimumPaneSize(50)  # 设置最小窗口尺寸

        left = wx.Panel(parent=self.splitter)
        right = wx.Panel(parent=self.splitter)
        # 左右分割窗口
        self.splitter.SplitVertically(left, right)

        d = DocView(left, '#cadeef')
        p = DocView(right, '#e5e5e5')

    def initMenus(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileSelectMenu = fileMenu.Append(wx.ID_FILE, '选择文件', 'docx')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.openFile, fileSelectMenu)

    def openFile(self, e):
        filesFilter = "Word (*.docx*)|*.docx*|" "All files (*.*)|*.*"
        fileDialog = wx.FileDialog(self, message="选择docx文件", wildcard=filesFilter, style=wx.FD_OPEN)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path = fileDialog.GetPath()
        print('文件路径：', path)
        if not path:
            return
        if path.find('*.docx'):
            return self.openOffice(path, 'kwps.Application')  # word 的接口
        # docx 转 pdf
        # coverPdf(path, path.replace('.docx',  '_' + str(time.time())) + '.pdf')

def main():
    app = wx.App()
    tp = ToolPage(None, title="预览文件转换", size=(800, 500))
    tp.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
