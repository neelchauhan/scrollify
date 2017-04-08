from pynput.mouse import Controller
import os.path
import sys

def usage():
    print('Usage: %s [up | down]' % sys.argv[0])
    sys.exit()

if __name__ == '__main__':
    mouse = Controller()
    file_loc = os.path.join(os.path.expanduser('~'), '.scrollifyrc')

    scroll_amt = 1
    if os.path.exists(file_loc):
        file_desc = open(file_loc, "r")
        scroll_amt = int(file_desc.read())

    if len(sys.argv) > 1:
        if sys.argv[1] == 'up':
            mouse.scroll(0, scroll_amt)
        elif sys.argv[1] == 'down':
            mouse.scroll(0, -scroll_amt)
        else:
            usage();
    else:
        usage()
