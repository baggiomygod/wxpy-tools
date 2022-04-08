import wx 
from docx import Document 
	
def cs(self):
	doc = Document()
	bbTi=doc.add_heading('', 1)
	wjBj=bbTi.add_run('测试内容')
	print('写文档前')
	doc.save('1.docx')
	print('写文档后')
 
app = wx.App() 
frame=wx.Frame(None,title='测试')
panel=wx.Panel(frame,-1)
bt=wx.Button(panel,-1,label='测试')
 
bt.Bind(wx.EVT_BUTTON, cs)
 
 
frame.Show()
