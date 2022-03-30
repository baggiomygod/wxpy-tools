
import wx

app = wx.App(False)

frame = wx.Frame(None, wx.ID_ANY, 'hello!')
frame.Show(True)

app.MainLoop()