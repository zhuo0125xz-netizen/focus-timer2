Focus Timer

This is a small timer for study and rest I built for the assignment. I can choose the time for each part. It starts with 25 minutes for Study and 5 minutes for Rest, but I can change both.

--------------
How to run it

You need Python 3 with Tkinter. There are no extra pip packages to install.

First open a terminal in this folder.

On Mac, run:
python3 focus_timer.py

On Windows, run:
python focus_timer.py

The timer window should open. Liek this: 

--------------
How I use it

For a quick check I enter 0 minutes and 10 seconds for Study, then 0 minutes and 5 seconds for Rest. Start begins Study. When it ends the timer goes to Rest and then Finished.

Pause keeps the same time and changes to Resume. Reset brings it back to Ready and 0:0. The numbers stay in the boxes so I can use them again. I need Reset before starting another session.

The inputs need whole numbers instead of decimals. Seconds are 0 to 59 and both times need to be positive numbers, which should above 0. For one and a half minutes I enter 1 minute and 30 seconds instead of 1.5.

--------------
Code parts

I separated the code into three parts: input and display, timer and button actions, and the window and controls. 
I not only used concepts from the class, but also researched online to read and learn some other concepts like Tkinter, which are not covered in the class. I read a lot of exteranl mateirals links. Those links are at the end of my focus_timer.py Python file.

--------------
Things to improve

Sometimes I would like to learn or rest 1 or 2 min longer. Current vesrion our Rest starts without asking me first. The system bell might not be heard when the computer is muted. The timer does not save settings or send a background notification.

The display shows 0:5 instead of 00:05. The first update after Start or Resume can be early, and a busy window can delay the updates. It is a basic timer rather than a precise stopwatch.
