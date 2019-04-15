import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os


screen = tk.Tk()
floors_file = open("Floors.txt", "r")
floors = []
for line in floors_file:
	floors.append(line.rstrip())
floors_file.close()


def search():
	flag = False

	if entry_box.get() is not "":
		for x in range(0, len(floors)):
			if selection.get() == floors[x].split('	', 1)[0]:
				while floors[x] != "," and flag is not True:
					x += 1
					if entry_box.get() == floors[x]:
						flag = True
						not_valid.place_forget()
						while len(floors[x].split(' ', 2)) != 2:
							x -= 1
						print(floors[x].replace(':', ''))

		if not flag:
			not_valid.place(x=645, y=25)

	if selection.get() is "E":
		print("")
	elif selection.get() is "CS":
		print("")
	elif selection.get() is "EC":
		print("")
	elif selection.get() is "GH":
		print("")
	elif selection.get() is "Hum":
		print("")
	elif selection.get() is "LH":
		print("")
	elif selection.get() is "MH":
		print("")


# screen title and size
screen.title("Campus")
screen.geometry("930x610")

# Campus image
img = ImageTk.PhotoImage(Image.open("campus.png"))
panel = tk.Label(screen, image=img)
panel.pack(side=BOTTOM)

# What can be searched for
title_question = tk.Label(screen, text="Classes to Search:")
title_question.pack(side=TOP)


# Entry Box
Label(screen, text="Room #:").place(x=438, y=25)
entry_box = tk.Entry(screen, width=6)
entry_box.place(x=500, y=25)

# Search Button
search_button = tk.Button(screen, text="Search", bg="Blue", command=search)
search_button.place(x=558, y=20)

# Dropdown menu
Label(screen, text="Building Initials:").place(x=252, y=25)
buildings = ["E", "CS", "EC", "GH", "Hum", "LH", "MH"]
selection = StringVar(screen)
selection.set(buildings[0])
buildings_dropdown = OptionMenu(screen, selection, *buildings)
buildings_dropdown.config(width=3)
buildings_dropdown.place(x=360, y=20)

# Information box

# Building highlight


# Error text
not_valid = tk.Label(screen, text="Invalid room #")

screen.mainloop()
