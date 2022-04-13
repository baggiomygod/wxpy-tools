import datetime

import wx
from docx import Document


class DocxTest(wx.Frame):
    def __init__(self, parent, title):
        super(DocxTest, self).__init__(parent, title=title)
        self.initUi()

    def initUi(self):
        panel = wx.Panel(self)
        bt = wx.Button(panel, wx.ID_ANY, label="测试")
        # bt.Bind(panel, 1)
        self.Bind(wx.EVT_BUTTON, self.docFun, bt)

    def docFun(self, e):
        doc = Document()
        bb_ti = doc.add_heading('', 1)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        print(current_time)
        wj_bj = bb_ti.add_run('测试内容' + current_time)
        print('写文档前')
        doc.save('1.docx')
        print('写文档后')


def main():
    app = wx.App()
    dt = DocxTest(None, title="docx")
    dt.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
