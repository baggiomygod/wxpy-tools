import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(1000, 700))


def main():
    app = wx.App()
    ex = Example(None, title='hello wx!')
    ex.Center()
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()