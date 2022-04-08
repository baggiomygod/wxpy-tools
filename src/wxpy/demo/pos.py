#!/bin/env python

import wx

class Pos(wx.Frame):
  def __init__(self, *args, **kw):
    wx.Frame.__init__(self, None, -1, 'Form', size=(500,600))
    panel = wx.Panel(self, -1)
    panel.Bind(wx.EVT_MOTION, self.OnMove)
    wx.StaticText(panel, -1, 'Pos:', pos=(10, 12))
    self.posCtrl = wx.TextCtrl(panel, -1, '', pos=(40, 10))

  def OnMove(self, event):
    pos = event.GetPosition()
    self.posCtrl.SetValue('%s, %s' % (pos.x, pos.y))


if __name__ == '__main__':
  app = wx.PySimpleApp()
  pos = Pos()
  pos.Show(True)
  app.MainLoop()