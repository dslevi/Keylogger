"""
Terminal Commands:
- xev 
    - opens new window to test event listeners
    - displays info about event in Terminal
        -event type (KeyPress, KeyRelease), keycode, timestamp, ASCII code value
-sudo showkey
    -displays keycode num, press/release in terminal
- cd /dev/input/event$ ($=event# you are interested in)
    -displays the input file logs for specific events

Research:
- ubuntu keysyms
- install as root
- X Window system

Remapping project:
- xmodmap: used to edit and display keyboard modifier

Keylogger project:
-Outline
    -capture keystrokes
        -identify keyboard identity: xinput --list
        -log keystrokes: xinput --test $id
    -throw keys into a file
"""
"""
Sample code:

struct input_event {
    struct timeval time;
    unsigned short type;
    unsigned short code;
    unsigned int value;
};
    -linux/input.h defines type/code
        -type: EV_KEY (keypress), EV_REL (time, relative motion events)
        -code: keycode











Event handlers:
    modules get input events and pass to corresponding interface
    keystrokes to kernal

Input subsystem:
    user action -> input device
    input event
    input core -> interested handlers
    -> user space (standard Unix file interface)

Input event - data structure:
    -struct timeval time of event
    -unsigned short type: event type
    -unsigned short code: event code
    -unsigned int value: event number value














"""
#contains C extensions, building requires python dev and kernal kernal headers installed
from evdev import InputDevice
from select import select

dev = InputDevice('dev/input/event1')

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
        print event
