import keyboard

def end_script():
    """
    Waits for the user to press any key in order to end the script.
    """
    print("\033[1;32m Press a key to exit...\033[m")
    while not keyboard.read_key():
        pass