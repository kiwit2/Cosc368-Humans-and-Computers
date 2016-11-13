#!/usr/bin/python3
# Stub to run the demo of the finished keyboard

import keyboard_impl

########################################
# Configure some of the parameters
#keyboard_impl.MODE = "qwerty"
#keyboard_impl.MODE = "static"
keyboard_impl.MODE = "dynamic"

keyboard_impl.NUM_TARGETS = 6
keyboard_impl.NUM_REPS = 6


########################################

# Run keyboard
keyboard_impl.main()
