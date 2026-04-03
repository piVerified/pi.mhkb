import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.encoder import Encoder

keyboard = KMKKeyboard()

# 1. Matrix Configuration
# Rows: GP0 to GP4
# Cols: GP5 to GP15, GP18 to GP21
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.col_pins = (
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, 
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, 
    board.GP15, board.GP18, board.GP19, board.GP20, board.GP21
)

# Based on 1N4148 diodes pointing from Row to Column
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# 2. Rotary Encoder Configuration
# Based on the schematic: EC_A -> GP27, EC_B -> GP26, SW -> GP22
encoder = Encoder()
keyboard.extensions.append(encoder)

encoder.pins = (
    (board.GP27, board.GP26, board.GP22, False), # (A, B, Tap, inverted)
)

# Encoder behavior: Volume Up/Down and Mute on tap
encoder.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),), # Layer 0
]

# 3. Keymap
# This follows the 60% HHKB-ish layout from your previous image
# 'None' or 'KC.NO' is used for the gaps/blockers
keyboard.keymap = [
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSLS, KC.NO,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.DEL,  KC.NO,
        KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.MO(1), KC.NO,   KC.NO,
        KC.NO,   KC.LOPT, KC.LGUI, KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.RGUI, KC.ROPT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
