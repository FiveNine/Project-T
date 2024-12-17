import win32gui

windowClass = win32gui.WNDCLASS()
windowClass.lpszClassName = "Test"

win32gui.CreateWindow("Test", "Test Title", 0, 0, 0, 300, 300, 0, 0, 0, None)