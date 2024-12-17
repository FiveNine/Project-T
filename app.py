import tkinter as tk
import pynput
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

start_x, start_y = 0, 0
isMouseDown = False

def on_mouse_move(x, y):
    global isMouseDown, rect
    if isMouseDown:
        # print(f'x={x}, y={y}')
        print(type(root))
        width = abs(x - start_x)
        height = abs(y - start_y)
        root.geometry(f"{width}x{height}+{start_x}+{start_y}")

def on_mouse_click(x, y, button, pressed):
    global start_x, start_y, isMouseDown
    print(f'x={x}, y={y}, button={button}, pressed={pressed}')
    if pressed:
        isMouseDown = True
        start_x, start_y = x, y
    else:
        isMouseDown = False
        end_x, end_y = x, y



root = tk.Tk()

root.overrideredirect(True)
root.geometry("+350+400")
root.tk.call('tk', 'scaling', 2.0)
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "red")

canvas = tk.Canvas(root, width=350, height=400, bg='red')

rect = canvas.create_rectangle(0,0,100,100, fill='red', outline='white')

# label = tk.Label(root, text='Hello\n\n\nWorld\n\n\nreeeeee', bg='white', font=('Helvetica ', 20, 'bold'))
# label.pack()
with pynput.mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click) as listener:
    listener.join()
root.mainloop()



#----------------PYQT6----------------

# import sys
# from PyQt6 import QtCore, QtWidgets
# from PyQt6.QtCore import Qt

# def main():
#     app = QtWidgets.QApplication(sys.argv)

#     window = QtWidgets.QWidget()


#     window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
#     window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
#     window.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
#     # window.setAttribute(Qt.WidgetAttribute.WA_InputMethodTransparent)

#     layout = QtWidgets.QVBoxLayout()

#     # sizegrip = QtWidgets.QSizeGrip(window)
#     # layout.addWidget(sizegrip, 0, QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignRight)

#     # change_size_button = QtWidgets.QPushButton()
#     # change_size_button.setText('a big button that does nothing')
#     # change_size_button.clicked.connect(lambda: window.setStyleSheet('QWidget#vc{background-color: transparent}'))
#     # layout.addWidget(change_size_button)

#     test_label = QtWidgets.QLabel("Hello World")
#     test_label.setStyleSheet('color: red;')
#     layout.addWidget(test_label)
#     test_label_width = test_label.fontMetrics().boundingRect(test_label.text()).width()
#     test_label_height = test_label.fontMetrics().boundingRect(test_label.text()).height()
    

#     window.setGeometry(QtCore.QRect(300, 300, test_label_width, test_label_height))
#     window.setLayout(layout)

#     window.show()
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()