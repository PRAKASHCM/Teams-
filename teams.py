import wx

def prompt_password():
    app = wx.App(False)
    dialog = wx.TextEntryDialog(None, "Enter your password:", "Password Prompt", "", style=wx.TE_PASSWORD)
    
    if dialog.ShowModal() == wx.ID_OK:
        password = dialog.GetValue()
        print("Password entered:", password)
    else:
        print("Password input was canceled.")
    
    dialog.Destroy()

prompt_password()
