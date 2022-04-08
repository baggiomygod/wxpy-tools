import wx

class MyPopupMenu(wx.Menu):
  
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        minMenu = wx.MenuItem(self, wx.ID_ANY, 'Minimize')
        self.Append(minMenu)
        self.Bind(wx.EVT_MENU, self.OnMinimize, minMenu)

        closeMenu = wx.MenuItem(self, wx.ID_ANY, 'Close')
        self.Append(closeMenu)
        self.Bind(wx.EVT_MENU, self.OnClose, closeMenu)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()
class SubMenu(wx.Frame):
  def __init__(self, *args, **kw):
      super(SubMenu, self).__init__(*args, **kw)
      self.InitUI()

  def InitUI(self):
    menubar = wx.MenuBar()

    fileMenu = wx.Menu()

    # 菜单
    fileMenu.Append(wx.ID_NEW, '&New')
    fileMenu.Append(wx.ID_OPEN, '&Open')
    fileMenu.Append(wx.ID_SAVE, '&Save')
    # 菜单分割
    fileMenu.AppendSeparator()

    # 子菜单
    imp = wx.Menu()
    imp.Append(wx.ID_ANY, 'Import newsfeed list...')
    imp.Append(wx.ID_ANY, 'Import bookmarks...')
    imp.Append(wx.ID_ANY, 'Import mail...')
    fileMenu.AppendSubMenu(imp, 'import')

    # 退出按钮
    quitMenu = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+q')
    quitMenu.SetBitmap(wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\wxpyDemo\\assets\\icons\\quit.png'))
    fileMenu.Append(quitMenu)

    # 退出按钮绑定退出事件
    self.Bind(wx.EVT_MENU, self.OnQuit, quitMenu)


    viewMenus = wx.Menu()

    # statusbar 状态菜单按钮
    self.statusMenu = viewMenus.Append(wx.ID_ANY, 'Show statusbar',
            'Show Statusbar', kind=wx.ITEM_CHECK)
    viewMenus.Check(self.statusMenu.GetId(), True)
    self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.statusMenu)
    self.statusbar = self.CreateStatusBar()
    self.statusbar.SetStatusText('Ready')

    # toolbar 工具菜单按钮
    self.toolMenu = viewMenus.Append(wx.ID_ANY, 'Show toolbar',
            'Show Toolbar', kind=wx.ITEM_CHECK)
    viewMenus.Check(self.toolMenu.GetId(), True)

    self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.toolMenu)
    self.toolbar = self.CreateToolBar()
    q1tool = self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\wxpyDemo\\assets\\icons\\exit.png'))
    q2tool = self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\wxpyDemo\\assets\\icons\\quit.png'))
    self.toolbar.Realize()
    self.Bind(wx.EVT_TOOL, self.OnQuit, q1tool)
    self.Bind(wx.EVT_TOOL, self.OnQuit, q2tool)


    # 垂直布局toolbar
    vtoolbar1 = wx.ToolBar(self)
    quitToolbar1 = vtoolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\wxpyDemo\\assets\\icons\\quit.png'))
    vtoolbar1.Realize()
    vtoolbar2 = wx.ToolBar(self)
    quitToolbar2 = vtoolbar2.AddTool(wx.ID_ANY, '', wx.Bitmap('D:\\work\\jyjs-projects\\examples\\python\\wxPy-my-tools\\src\\wxpyDemo\\assets\\icons\\exit.png'))
    vtoolbar2.Realize()
    self.Bind(wx.EVT_TOOL, self.OnQuit, quitToolbar1)
    self.Bind(wx.EVT_TOOL, self.OnQuit, quitToolbar2)

    vbox = wx.BoxSizer(wx.HORIZONTAL)
    vbox.Add(vtoolbar1, 0, wx.EXPAND)
    vbox.Add(vtoolbar2, 0, wx.EXPAND)
    self.SetSizer(vbox)

    # 将fileMenu append 到菜单栏
    menubar.Append(fileMenu, '&File')
    menubar.Append(viewMenus, '&View')
    self.SetMenuBar(menubar)

    self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    # 窗口位置和大小
    self.SetSize((350, 250))
    self.SetTitle('Submenu')
    self.Centre()

  def OnQuit(self, e):
    self.Close()

  def ToggleStatusBar(self, e):
    if self.statusMenu.IsChecked():
      self.statusbar.Show()
    else:
      self.statusbar.Hide()

  def ToggleToolBar(self, e):
    if self.toolMenu.IsChecked():
      self.toolbar.Show()
    else:
      self.toolbar.Hide()

  def OnRightDown(self, e):
    self.PopupMenu(MyPopupMenu(self), e.GetPosition())

def main():
  app=wx.App()
  sm = SubMenu(None)
  sm.Show()
  app.MainLoop()

if __name__ == '__main__':
  main()