# 10/24/2013 Sebastian Raschka
# HydroBond
# PyMOL Plugin for visualization of hydrogen bonds between protein and ligand.


import tkSimpleDialog,tkFileDialog
import tkMessageBox
from pymol import cmd
import sys
 
def __init__(self):
   self.menuBar.addmenuitem('Plugin', 'command',
                            'HydroBond',
                            label = 'HydroBond',
                            command = lambda s=self : fetch_bonds_dialog(s))
  
def draw_bonds(protein_obj, ligand_obj, distance):
    cmd.select("donor", "(elem n,o and (neighbor hydro))")
    cmd.select("acceptor", "(elem o or (elem n and not (neighbor hydro)))")
    cmd.distance("HBAcc", "({} and acceptor)".format(ligand_obj),
           "({} and donor)".format(protein_obj), distance)
    cmd.distance("HBDon", "({} and donor)".format(ligand_obj),
                "({} and acceptor)".format(protein_obj), distance)

    cmd.delete("donor")
    cmd.delete("acceptor")
    cmd.hide("labels")


def fetch_bonds_dialog(app):
    protein_obj = tkSimpleDialog.askstring('Object selection',
            'Please enter the name of a protein object loaded in PyMOL: ',
                           parent=app.root) 
    ligand_obj = tkSimpleDialog.askstring('Object selection',
            'Please enter the name of a ligand object loaded in PyMOL: ',
                           parent=app.root)
    distance = tkSimpleDialog.askstring('Distance selection',
            'Please enter a distance in Angstrom (e.g., 3.2): ',
                           parent=app.root)

    draw_bonds(protein_obj, ligand_obj, distance)



