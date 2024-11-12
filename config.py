import re
from xkeysnail.transform import *

define_modmap({
        Key.HENKAN:Key.ENTER,
        Key.Q:Key.TAB,
        Key.KATAKANAHIRAGANA:Key.CAPSLOCK,
        Key.CAPSLOCK:Key.Q,
})

define_multipurpose_modmap({
    Key.CAPSLOCK: [Key.Q, Key.LEFT_CTRL],  #### Caps Lockを単押しでESC,併用でCtrl###
    Key.SPACE:[Key.SPACE,Key.LEFT_SHIFT],
    Key.MUHENKAN:[Key.MUHENKAN,Key.LEFT_CTRL],
})

define_keymap(None, {
        K("C-f"): K("backspace"),
        K("C-Shift-f"):K("backspace"),
        K("C-d"):K("delete"),
        K("C-m"): K("enter"),
        K("C-l"): Key.RIGHT,
        K("C-h"): Key.LEFT,
        K("C-k"): Key.UP,
        K("C-j"): Key.DOWN,
        K("C-Shift-l"): K("Shift-right"),
        K("C-Shift-h"): K("Shift-left"),
        K("C-Shift-k"): K("Shift-up"),
        K("C-Shift-j"): K("Shift-down"),
        K("M-b"): with_mark(K("C-left")),
        K("M-f"): with_mark(K("C-right")),#Alt+f で Ctrl+右
        K("C-e"): with_mark(K("end")),      #Ctrl+e で 行末
        K("j"):{K("j"):Key.ESC},
}, "Custom Keymap for Ctrl+H and CapsLock swap")

