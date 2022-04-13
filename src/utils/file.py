def openFileDialog():
    filesFilter = "Word (*.docx*)|*.docx*|" "All files (*.*)|*.*"
    fileDialog = wx.FileDialog(self, message="选择docx文件", wildcard=filesFilter, style=wx.FD_OPEN)
    dialogResult = fileDialog.ShowModal()
    if dialogResult != wx.ID_OK:
        return
    path = fileDialog.GetPath()
    print('文件路径：', path)