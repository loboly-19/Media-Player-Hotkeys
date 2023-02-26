import pyautogui
import keyboard

# Define the hotkeys for skipping to the next or previous song
NEXT_KEY = 'page down'
PREV_KEY = 'page up'

# Define the callback function for the hotkeys
def on_hotkey(event):
    if event.name == NEXT_KEY:
        pyautogui.press('nexttrack')
    elif event.name == PREV_KEY:
        pyautogui.press('prevtrack')

# Register the hotkey callbacks
keyboard.on_press_key(NEXT_KEY, on_hotkey)
keyboard.on_press_key(PREV_KEY, on_hotkey)

# Block the main thread to keep listening for keyboard events
keyboard.wait()
