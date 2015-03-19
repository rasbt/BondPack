# 10/24/2013 Sebastian Raschka
# BondVis
# PyMOL Plugin for visualization of molecular bonds between atom pairs.


import tkSimpleDialog,tkFileDialog
import tkMessageBox
from pymol import cmd
import sys
import string
import itertools


def __init__(self):
   self.menuBar.addmenuitem('Plugin', 'command',
                            'BondVis',
                            label = 'BondVis',
                            command = lambda s=self : fetch_bonds_dialog(s))

def load_bonds(bonds_filename):
    bond_list = []
    error_list = list()
    bondfile = False
    try:
        bondfile = open(bonds_filename, "r")
        for line in bondfile:
            line_mod = line.strip()
            if line_mod:
                line_mod = [i.strip(string.punctuation) for i in line_mod.split()]
            if len(line_mod) >= 2:
                try:
                    atoms = [int(line_mod[0]), int(line_mod[1])]
                    if len(line_mod) >= 3:
                        bond_list.append(atoms + [line_mod[2]])
                    else:
                        bond_list.append(atoms + ['bond'])
                except ValueError:
                    error_list.append(line)
                    pass
        if not bond_list:
            print "Unexpected error:", sys.exc_info()[0]
            tkMessageBox.showerror('Could no load bond information.',
                       'Error. Could not detect bonds in \n'
                       + bonds_filename)
        else:
            print "\n Detected the following bonds: "
            for bond in bond_list:
                print " {} ---- {}".format(bond[0], bond[1])
        if error_list:
            print "\n Warning! Ignored the following line(s):"
            for err in error_list:
                print " " + err
        draw_bonds(bond_list)

    except:
        if bondfile:
            bondfile.close()
        print "Unexpected error:", sys.exc_info()[0]
        tkMessageBox.showerror('Could not open file.',
                       'Error. Could not open file: \n'
                       + bonds_filename)

def fetch_bonds_dialog(app):
   bonds_filename = tkFileDialog.askopenfilename(parent=app.root,title='Open bond info file')
   load_bonds(bonds_filename)

def draw_bonds(bond_list):

    c = itertools.cycle(("yellow", "blue", "green", "red", "white", "black"))

    colors = dict()
    for t in bond_list:
        if t[2] not in colors:
            colors[t[2]] = c.next()


    for bond in bond_list:

        print(bond_list)
        cmd.distance("%s" % bond[2], "id %s" % bond[0], "id %s" % bond[1])
        cmd.set("dash_color", colors[bond[2]], "%s" % bond[2])


        cmd.hide("labels")
    cmd.set("dash_gap", 0.20)

#cmd.extend('load_bonds', load_bonds)
