import pyHook, pythoncom

def OnMouseEvent(event):
    print "Mouse location", event.Position
    print "Window", event.Window
    print "Scrolling?", event.Wheel == -1

hm = pyHook.HookManager()
hm.MouseAll = OnMouseEvent
hm.HookMouse()
pythoncom.PumpMessages()
