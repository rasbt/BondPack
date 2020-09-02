# 10/24/2013 Sebastian Raschka
# BondLab PyMOL plugin

from tkinter import *
from pymol import cmd
import sys, zlib, string

def __init__(self):
    """adds plugin to PyMOL menu"""
    self.menuBar.addmenuitem('Plugin', 'command',
                        'BondLab',
                        label = 'BondLab',
                        command = lambda : open_menu())

def open_menu():
    global master
    master = Tk()
    master.wm_geometry("300x440")
    master.title('Customize Bonds')
    Button(master, text='OK', command=close).pack(side=BOTTOM)
    
    Label(master, text="Labels").pack()
    labels = IntVar(master=master)
    Radiobutton(master, text='on', variable=labels, value=1, 
            command=lambda: show_labels(True)).pack(anchor=W)
    Radiobutton(master, text='off', variable=labels, value=2, 
            command=lambda: show_labels(False)).pack(anchor=W)
  
    separator1 = Frame(master, height=2, bd=1, relief=SUNKEN)
    separator1.pack(fill=X, padx=5, pady=5)

    Label(master, text="Line Width").pack()
    line_width = IntVar(master=master)
    Radiobutton(master, text='light', variable=line_width, value=1, 
            command=lambda: adjust_width(1)).pack(anchor=W)
    Radiobutton(master, text='medium', variable=line_width, value=2, 
            command=lambda: adjust_width(2)).pack(anchor=W)
    Radiobutton(master, text='heavy', variable=line_width, value=3, 
            command=lambda: adjust_width(3)).pack(anchor=W)

    separator2 = Frame(master, height=2, bd=1, relief=SUNKEN)
    separator2.pack(fill=X, padx=5, pady=5)

    Label(master, text="Dash Gaps").pack()
    dash_gaps = IntVar(master=master)
    Radiobutton(master, text='none', variable=dash_gaps, value=1, 
            command=lambda: adjust_gaps(1)).pack(anchor=W)
    Radiobutton(master, text='narrow', variable=dash_gaps, value=2, 
            command=lambda: adjust_gaps(2)).pack(anchor=W)
    Radiobutton(master, text='normal', variable=dash_gaps, value=3, 
            command=lambda: adjust_gaps(3)).pack(anchor=W)
    Radiobutton(master, text='wide', variable=dash_gaps, value=4, 
            command=lambda: adjust_gaps(4)).pack(anchor=W)

    separator2 = Frame(master, height=2, bd=1, relief=SUNKEN)
    separator2.pack(fill=X, padx=5, pady=5)


    Label(master, text="Dash Color").pack()
    dash_color = IntVar(master=master)
    Radiobutton(master, text='yellow', variable=dash_color, value=1, 
            command=lambda: adjust_color(1)).pack(anchor=W)
    Radiobutton(master, text='blue', variable=dash_color, value=2, 
            command=lambda: adjust_color(2)).pack(anchor=W)
    Radiobutton(master, text='green', variable=dash_color, value=3, 
            command=lambda: adjust_color(3)).pack(anchor=W)
    Radiobutton(master, text='red', variable=dash_color, value=4, 
            command=lambda: adjust_color(4)).pack(anchor=W)
    Radiobutton(master, text='white', variable=dash_color, value=5, 
            command=lambda: adjust_color(5)).pack(anchor=W)
    Radiobutton(master, text='black', variable=dash_color, value=6, 
            command=lambda: adjust_color(6)).pack(anchor=W)


    mainloop()

def show_labels(show):
    if show:
        cmd.show("labels")
    else:
        cmd.hide("labels")

def adjust_width(width):
    widths = {1:"0.03", 2:"0.1", 3:"0.2"}
    cmd.set("dash_radius", widths[width])

def adjust_gaps(gap):
    gaps = {1:"0.0", 2:"0.25", 3:"0.5", 4:"0.75"}
    cmd.set("dash_gap", gaps[gap])

def adjust_color(col_ind):
    colors = {1:"yellow", 2:"blue", 3:"green", 4:"red", 5:"white", 6:"black"}
    cmd.set("dash_color", colors[col_ind])
  

def close():
    master.destroy()
