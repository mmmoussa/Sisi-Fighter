import wx

class interface(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, "Sisi game", size=(400,300))
		panel = wx.Panel(self)

		status = self.CreateStatusBar()
		menubar = wx.MenuBar()
		firstMenu = wx.Menu()
		secondMenu = wx.Menu()
		firstMenu.Append(wx.NewId(), "Play game", "Click to play the game")
		firstMenu.Append(wx.NewId(), "Show credits", "Click to show credits")
		secondMenu.Append(wx.NewId(), "Exit", "Click to exit")
		menubar.Append(firstMenu, "Options")
		menubar.Append(secondMenu, "Exit")
		self.SetMenuBar(menubar)

if __name__=="__main__":
	app = wx.PySimpleApp()
	frame = interface(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
