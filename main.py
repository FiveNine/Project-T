import pyautogui
import pytesseract
from pynput import mouse, keyboard
from googletrans import Translator
import tkinter as tk
import TkUtils

def translate_text(text, dest='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

def translate_highlighted_text(startX, startY, end_x, end_y):
    # Determine the region to capture based on start and end positions
    region_left = min(startX, end_x)
    region_top = min(startY, end_y)
    region_width = abs(end_x - startX)
    region_height = abs(end_y - startY)
    region = (region_left, region_top, region_width, region_height)
    # print(f'Region: {region}')

    # Capture a screenshot of the determined region
    screenshot = pyautogui.screenshot(region=region)

    screenshot.save('screenshot.png')

    # Perform OCR to extract the text from the screenshot
    extracted_text = pytesseract.image_to_string(screenshot, config='-l jpn+eng+ara+fre')

    print(f'Extracted text: {extracted_text}')

    # Translate the extracted text
    translation = translate_text(extracted_text, 'en')

    # Display the translation
    print(f'Translation: {translation}')
    return translation

def create_translation_label(root, input_text, posX, posY):
    label = TkUtils.TkLabel(input_text, posX, posY, 'white', root)
    label.bind('<Button-1>', lambda e: label.destroy())
    addQueue.append(label)


def on_mouse_move(x, y):
    global mouse_position_x, mouse_position_y, dragBox
    mouse_position_x = x
    mouse_position_y = y

    if (dragBox != None):
        canvasUpdateQueue.append((x, y))

    if quitProgram:
        return False
        

def on_key_press(key):
    global quitProgram, startX, startY, isCapturingRegion, dragBox
    if key == keyboard.Key.ctrl_l and not isCapturingRegion:
        isCapturingRegion = True
        startX, startY = mouse_position_x, mouse_position_y

        dragBox = TkUtils.TkRect(startX, startY, 'green', 'red', canvas)
        addQueue.append(dragBox)

    if key == keyboard.Key.esc:
        quitProgram = True
        return False
def on_key_release(key, root):
    global isCapturingRegion, startX, startY, dragBox
    if key == keyboard.Key.ctrl_l and isCapturingRegion:
        isCapturingRegion = False
        end_x, end_y = mouse_position_x, mouse_position_y

        removeQueue.append(dragBox)

        if (startX == end_x or startY == end_y):
            return
        output = translate_highlighted_text(startX, startY, end_x, end_y)
        create_translation_label(root, output, end_x, end_y)

def updateRoot():
    if len(addQueue) > 0:
        addQueue.pop(0).build()
    if len(removeQueue) > 0:
        removeQueue.pop(0).destroy()
    if quitProgram:
        root.destroy()
        return
    root.after(ms=100, func=updateRoot)

def updateCanvas():
    if len(canvasUpdateQueue) > 0:
        if (dragBox != None):
            mouseX, mouseY = canvasUpdateQueue.pop(0);
            dragBox.update(mouseX, mouseY)
        pass
    canvas.after(ms=1, func=updateCanvas)

def main():
    global isCapturingRegion, quitProgram, root, addQueue, removeQueue, canvas, canvasUpdateQueue, dragBox
    isCapturingRegion = False
    quitProgram = False

    addQueue = []
    removeQueue = []
    canvasUpdateQueue = []

    dragBox = None

    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("1920x1080+0+0")
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "green")
    root.configure(bg='green')

    canvas = tk.Canvas(root, width=1920, height=1080, bg='green', highlightcolor='green', highlightthickness=0, bd=0)
    canvas.place(x=0, y=0)

    kb_listener = keyboard.Listener(on_press=on_key_press, on_release= lambda event: on_key_release(event, root))
    kb_listener.start()
    mouse_listener = mouse.Listener(on_move=on_mouse_move)
    mouse_listener.start()

    updateCanvas()
    updateRoot()
    
    root.mainloop()

    kb_listener.join()
    mouse_listener.join()


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = 'D:\Misc_Projects\Tesseract-OCR\\tesseract.exe'
    print(pytesseract.image_to_string('image.png', 'eng'))
    # main()