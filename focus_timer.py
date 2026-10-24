# Focus Timer
# This is my focus timer for study and rest. Functions: Start, Pause, Resume and Reset
# I put all the reference links at the end of this file

#
# My code has three sections
# Section 1: input and display
# Section 2: timer and button actions
# Section 3: window and controls
#


import tkinter as tk

second_remaining = 0
resting_time = 0

status_of_the_timer = "Ready"
should_deduct_seconds = False


# Section 1 of my code: input and display
# display_timer_time(), read_out_time(), user_input()

def display_timer_time():
    # I keep the time in seconds, so here I change it to minutes and seconds for the screen
    m = second_remaining // 60  # whole minutes
    s = second_remaining % 60  # use % to show leftover seconds

    show_the_timing.config(text=str(m) + ":" + str(s))
    show_the_staging.config(text=status_of_the_timer)


def read_out_time(minute_box, second_box):
    m = minute_box.get()
    s = second_box.get()

    # The input from the boxes is text, so I check it first and then change it to a number
    if not m.isdecimal() or not s.isdecimal():
        return -1  # invalid input

    m = int(m)
    s = int(s)

    # The seconds box only goes up to 59, extra time can go in the minutes box
    if s > 59:
        return -1

    time_in_seconds = m * 60 + s  # total seconds
    return time_in_seconds


def user_input(input_status):
    # When I pass normal the user can type, disabled means the boxes cannot be changed
    # config changes a setting on the box, here I change if the user can type
    box1.config(state=input_status)
    box2.config(state=input_status)
    box3.config(state=input_status)
    box4.config(state=input_status)


# Section 2 of my code: timer and buttons; Here are the function names:
# time_pass_tick(), start_my_timer(), pause_or_resume(), reset()

def time_pass_tick():
    # These timer values are outside the function, so I use global to change the same values
    # Without global the assignment would make a local name inside this function
    global second_remaining, status_of_the_timer, should_deduct_seconds

    if should_deduct_seconds:  # when this is False the time stays the same
        second_remaining = second_remaining - 1

        if second_remaining == 0:
            window.bell()  # sound when Study or Rest ends

            # Once Study reaches zero I change it to Rest and use the rest time from the boxes
            if status_of_the_timer == "Study":
                status_of_the_timer = "Rest"
                second_remaining = resting_time

            else:
                # Rest has ended too, so I stop counting and the Pause button is no longer needed
                status_of_the_timer = "Finished"
                should_deduct_seconds = False
                bt2.config(state="disabled")

        display_timer_time()

    # after asks the window to call this function later, 1000 means about one second
    # It only calls once, so I need this line again for the next update
    # I leave it outside the if so the updates still happen when the timer is paused
    # There is no () after time_pass_tick because I want it to run later, not right here
    window.after(1000, time_pass_tick)


def start_my_timer():
    # I change the shared values here so the countdown can use the new times
    global second_remaining, resting_time, status_of_the_timer, should_deduct_seconds

    if status_of_the_timer != "Ready":  # I use Reset first if a session has already started
        return

    t1 = read_out_time(box1, box2)
    t2 = read_out_time(box3, box4)
    # Both parts need some time, so zero or the -1 from a bad input cannot start the timer
    if t1 <= 0 or t2 <= 0:
        show_the_staging.config(text="Enter whole numbers. Seconds must be 0-59. Both times must be above zero.")
        return

    second_remaining = t1
    resting_time = t2

    status_of_the_timer = "Study"
    should_deduct_seconds = True

    # Once the timer starts I disable the four input boxes so the user cannot type new times
    # I also disable bt1, the Start button, so it cannot be pressed again during the session
    user_input("disabled")
    bt1.config(state="disabled")
    bt2.config(state="normal")
    display_timer_time()


def pause_or_resume():
    # I change the same True or False value that time_pass_tick checks before taking off a second
    global should_deduct_seconds
    if status_of_the_timer not in ["Study", "Rest"]:
        return

    if should_deduct_seconds:
        should_deduct_seconds = False  # the update still happens, it just does not take off a second
        bt2.config(text="Resume")  # the user can press this to continue from the same time

    else:
        should_deduct_seconds = True
        bt2.config(text="Pause")


def reset():
    # Reset stops the countdown and puts it back to Ready, it does not start Rest
    global second_remaining, status_of_the_timer, should_deduct_seconds

    should_deduct_seconds = False
    second_remaining = 0
    status_of_the_timer = "Ready"

    # I let the user type again and keep the numbers already in the boxes for another session
    user_input("normal")
    bt1.config(state="normal")
    bt2.config(text="Pause", state="disabled")
    display_timer_time()


# Section 3 of my code: window and controls
# Labels, input boxes and buttons

# Tk makes the main window, the other parts go inside this window
window = tk.Tk()  # main app window
window.title("Study then Rest")  # title at the top of the window

tk.Label(window, text="Study / Rest").pack()
show_the_staging = tk.Label(window, text="Ready")  # shows Ready or the current status_of_the_timer
show_the_staging.pack()  # pack puts this label below the heading
show_the_timing = tk.Label(window, text="0:0")  # countdown display
show_the_timing.pack()


# Frame is like a container, I put the time boxes and their labels together in this part
box_for_user_input = tk.Frame(window)  # holds the time input rows
box_for_user_input.pack()  # place the input frame below the time


# Label is for showing text, the user does not type into it
# Here I use the labels to show which box is minutes and which box is seconds
tk.Label(box_for_user_input, text="").grid(row=0, column=0)  # empty corner above the row names
tk.Label(box_for_user_input, text="Minutes").grid(row=0, column=1)  # minutes column heading
tk.Label(box_for_user_input, text="Seconds").grid(row=0, column=2)  # seconds column heading
tk.Label(box_for_user_input, text="Study").grid(row=1, column=0)  # first input row
tk.Label(box_for_user_input, text="Rest").grid(row=2, column=0)  # second input row


# Entry is the box the user can type into, I need four boxes for the two times
box1 = tk.Entry(box_for_user_input, width=6)  # study minutes box
box2 = tk.Entry(box_for_user_input, width=6)  # study seconds box
box3 = tk.Entry(box_for_user_input, width=6)  # rest minutes box
box4 = tk.Entry(box_for_user_input, width=6)  # rest seconds box


# insert puts a starting number in the box, 0 means the beginning of the text
box1.insert(0, "25")  # start with 25 study minutes
box2.insert(0, "0")  # no extra study seconds
box3.insert(0, "5")  # default rest is 5 minutes
box4.insert(0, "0")  # insert at position 0 in the empty box


# grid gives each box a row and column so the boxes line up with the labels
# I use grid inside this frame, pack puts the frame in the main window
box1.grid(row=1, column=1)  # study row and minutes column
box2.grid(row=1, column=2)  # study row and seconds column
box3.grid(row=2, column=1)  # rest row and minutes column
box4.grid(row=2, column=2)  # rest row and seconds column

# This is another Frame so I can put the three buttons together in one row
place_for_buttons = tk.Frame(window)  # separate frame for the three buttons
place_for_buttons.pack()

# Button gives the user something to click, command says which function to use
# I do not put () after the function name because it needs to wait for the click
bt1 = tk.Button(place_for_buttons, text="Start", command=start_my_timer)  # pass start_my_timer without () so it runs on a click
bt1.pack(side="left")  # buttons sit beside each other

bt2 = tk.Button(place_for_buttons, text="Pause", command=pause_or_resume, state="disabled")  # disabled until the timer starts
bt2.pack(side="left")  # place Pause next to Start

bt3 = tk.Button(place_for_buttons, text="Reset", command=reset)  # clicking calls reset()
bt3.pack(side="left")  # last button in this row

time_pass_tick()  # start the update chain once

# mainloop keeps the window open and handles the clicks and the later updates
window.mainloop()  # handles clicks and scheduled updates


# Here are my learning resources and references
# Recap Python Materisl from the course
# variables.py and functions.py: stored values and functions with parameters.
# conditionals.py: if/else and % for remaining seconds.
# The four input boxes are changed one by one in user_input().
#
# References
# Tkinter: window, Label, Entry, Button, Frame, pack/grid and mainloop.
# https://docs.python.org/3/library/tkinter.html
# TkDocs Event Loop: short callbacks and after() scheduling one later call.
# https://tkdocs.com/tutorial/eventloop.html
# TkDocs - Entry state and config()
# https://tkdocs.com/pyref/entry.html
# TkDocs API: get, insert, config, bell and after.
# https://tkdocs.com/pyref/onepage.html
# Python types: isdecimal, //, %, str, lists and Boolean values.
# https://docs.python.org/3/library/stdtypes.html
# int: converting checked input into a whole number.
# https://docs.python.org/3/library/functions.html#int
# global: changing the shared timer values inside functions.
# https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
#
# TutorialsPoint: short example of playing the system bell with bell().
# https://www.tutorialspoint.com/article/tkinter-bell-method
