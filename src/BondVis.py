# 10/24/2013 Sebastian Raschka
# BondVis
# PyMOL Plugin for visualization of molecular bonds between atom pairs.


import tkSimpleDialog,tkFileDialog
import tkMessageBox
from pymol import cmd
import sys

 
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
            if len(line_mod) == 2:
                try:
                    atoms = [int(line_mod[0]), int(line_mod[1])]
                    bond_list.append(atoms)
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
    for bond in bond_list:
        cmd.distance("BONDS", "id %s" % bond[0], "id %s" % bond[1])

#cmd.extend('load_bonds', load_bonds)
