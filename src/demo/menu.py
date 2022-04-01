#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx

class Menu(wx.Frame):
  def __init__(self, *args, **kw):
      super(Menu, self).__init__(*args, **kw)

      self.InitUI()

  def InitUI(self):
    menubar = wx.MenuBar()
    fileMenu = wx.Menu()
    fileItem = fileMenu.Append(wx.ID_EXIT, '退出', '退出应用')
    menubar.Append(fileMenu, '&File') # windows下无效
    self.SetMenuBar(menubar)

    self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

    self.SetSize((300,200))
    self.SetTitle('菜单')
    self.Center()
  
  def OnQuit(self, e):
    self.Close()

def main():
  app = wx.App()
  mu = Menu(None)
  mu.Show()
  app.MainLoop()


if __name__ == '__main__':
  main()