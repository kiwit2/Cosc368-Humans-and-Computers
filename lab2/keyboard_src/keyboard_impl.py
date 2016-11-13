#!/usr/bin/python3
#
# Keyboard for COSC368 - Used in Labs 2 and 6
#
# Author: Joshua Leung (jsl76@uclive.ac.nz)
# Date: July 2016

from tkinter import *
#from tkinter.ttk import *  # XXX: this version of frame doesn't have bg

import random
import time

import getpass # For automatic username


# For Ctrl-C to exit
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

####################################################
# Constants - User Modifiable

# use the user's own username (works for Unix and Windows) - http://stackoverflow.com/a/842096/6531515
NAME = getpass.getuser()

# which type of keyboard to use
MODE = "qwerty"
#MODE = "static"
#MODE = "dynamic"

NUM_TARGETS = 6
NUM_REPS = 6

# Basic 
BOARD = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
KEYSIZE = 32

####################################################
# Utilities for Random Letters

# All letters in the alphabet
ALPHABET = [chr(x) for x in range(ord('a'), ord('z') + 1)]
#print(ALPHABET)


# Compute random letter order
# < (max_letters): (int) Number of random letters to compute
# > returns: ([str]) List of "max_letters" randomly ordered characters
def get_random_letters(max_letters=None):
	candidates = ALPHABET[:]
	random.shuffle(candidates)
	
	if max_letters:
		return candidates[:max_letters]
	else:
		return candidates

###################################################
# Keyboards

class Keyboard:
	def __init__(self, win, callback=None):
		# Store refs for later
		self.win = win
		self.callback = callback
		
		# List of StringVars - One per button...
		self.keycache = []
		
		# Init widgets
		self.setup_prompter()
		self.setup_keys()
		
		# Always update the layout once (to ensure that everything is set up correctly)
		self.update_layout()
	
	# UI Setup ----------------------------------------------
	
	def setup_prompter(self):
		# A pane to hold the prompter label
		frame = Frame(self.win)
		frame.pack(padx=10, pady=5)
		
		# The "prompter box" (really a label) + a stringvar
		self.prompter = StringVar()
		self.prompter.set("Click any key to start...")
		
		txtbox = Label(frame, width=40, textvariable=self.prompter)
		txtbox.configure(relief=SUNKEN, borderwidth=1, background="white")
		txtbox.pack(fill=X, expand=True)
	
	def setup_keys(self):
		# The visible frame
		box_frame = Frame(self.win, relief=RAISED, borderwidth=2)
		box_frame.pack(padx=5, pady=5)
		
		# Each row in the board
		for row in BOARD:
			row_frame = Frame(box_frame, borderwidth=1, relief=FLAT)
			row_frame.pack()
			
			for letter in row:
				# A StringVar so that this button's contents can be easily replaced
				keyvar = StringVar()
				keyvar.set(letter)
				self.keycache.append(keyvar)
				
				# Use a frame to force 
				f = Frame(row_frame, width=KEYSIZE, height=KEYSIZE)
				f.pack_propagate(False)
				f.pack(side=LEFT)
				
				b = Button(f, textvariable=keyvar)
				b['command'] = (lambda x=keyvar: self.on_keypress(x))
				b.grid(sticky=NSEW)
	
	# Event Handling ----------------------------------------	
	
	# Event handler for key presses		
	def on_keypress(self, key_var):
		key = key_var.get()
		
		if self.callback is not None:
			self.callback(key)
		else:
			print("'%s' pressed" % key)
	
	# API ---------------------------------------------------
	
	# Update prompter text
	def update_prompter(self, value):
		self.prompter.set(value)
	
	
	# Update layout of keys
	def update_layout(self):
		# Compute new order for the buttons
		# (The result should be stored in self.layout)
		self.calc_layout()
		assert(hasattr(self, 'layout') and type(self.layout) is str)
		
		# Apply new layout
		for k, v in zip(self.keycache, self.layout):
			k.set(v)
	
	# Calculate new key layout
	# ! Helper for update_layout()
	# ! Subclasses should override this
	def calc_layout(self):
		# Flatten BOARD into a single string
		self.layout = ''.join(BOARD)
		
# =================================================

class StaticKeyboard(Keyboard):
	# Calculate new key layout
	# ! Overrides default
	def calc_layout(self):
		# Only compute new layout on the first run
		# (i.e. to change the qwerty layout to something else)
		if hasattr(self, 'layout') is False:
			self.layout = ''.join(get_random_letters())


class DynamicKeyboard(Keyboard):
	# Calculate new key layout
	# ! Overrides default
	def calc_layout(self):
		# Always compute new layout
		self.layout = ''.join(get_random_letters())

###################################################

class Experiment:
	def __init__(self, window):
		# setup the keyboard ui
		if MODE == 'dynamic':
			KB_ctor = DynamicKeyboard
		elif MODE == 'static':
			KB_ctor = StaticKeyboard
		else:
			KB_ctor = Keyboard
			
		self.keyboard = KB_ctor(window, self.on_keypress)
		
		# logging
		self.log = None
		
		# handle the target set
		self.targets = get_random_letters(NUM_TARGETS)
		
		self.cur_index = -1
		self.block = 0
		
		# time tracking
		self.last_time = time.time()
	
	# ---------------------------------------
		
	# Callback for handling an event 
	def on_keypress(self, key):
		if self.is_acceptable(key):
			# Log current event
			task_time = time.time() - self.last_time
			self.log_event(task_time, key)
			
			# Advance to next task
			print("'%s' pressed" % key)
			self.advance()
		elif self.cur_index == -1:
			# First (dummy) trial - Start the games...
			self.start_experiment()
			self.advance()
		else:
			# Invalid/Nothing more to do...
			return
		
	# Prepare to show next target
	def advance(self):	
		# Increment index
		self.cur_index += 1
		
		# Wraparound?
		if self.cur_index >= NUM_TARGETS:
			print("  Starting Block  %d" % (self.block + 1))
			self.cur_index = 0
			self.block += 1
			
			self.shuffle_targets()
			
		# Update UI
		if self.block >= NUM_REPS:
			# Exit
			self.end_experiment()
		else:
			# Update UI
			self.keyboard.update_prompter(self.targets[self.cur_index])
			self.keyboard.update_layout()
		
		# Update last-seen time (for next trial)
		self.last_time = time.time()
	
	# ------------------------------------------
	
	# Shuffle the target order - Once per block
	def shuffle_targets(self):
		random.shuffle(self.targets)
		
	# Check if the current key is acceptable
	def is_acceptable(self, key):
		return key == self.keyboard.prompter.get()
		
	# ------------------------------------------
	
	# Setup the log file
	def start_experiment(self):
		print("Starting Experiment")
		
		fileN = "experiment_%s_log.txt" % (MODE)
		self.log = open(fileN, 'w')
		
		#self.log.write("START - %.4f\n" % (time.time()))
		#self.log.flush()
		
		print("  Starting Block  1")
		
	# Write a trial result to the log
	def log_event(self, task_time, description="<?>"):
		if self.log is None:
			print("ERROR: No log file loaded")
			return
			
		# task time in ms (time.time() gives secs)
		self.log.write("%s %s %s %d %.1f\n" % (NAME, MODE, description, self.block, task_time * 1000))
		self.log.flush()
		
	# Close the log and the file
	def end_experiment(self):
		print("Experiment Done!")
		
		if self.log is None:
			self.keyboard.update_prompt("ERROR: Experiment Over")
			return
		else:			
			# close the log file
			self.log.flush()
			self.log.close()
			
			# change the prompt
			self.keyboard.update_prompter("ALL DONE!")
			self.cur_index = -100
	

def main():
	window = Tk()
	window.title("Click on the keys shown below...")
	window.resizable(0,0)

	#kb = Keyboard(window)
	exp = Experiment(window)
	
	window.mainloop()

if __name__ == '__main__':
	main()

