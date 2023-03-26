import json
import random
import os
from pop import pop
import parliament
from definitions import *
import tkinter as tk
import _tkinter
from tkinter import ttk



root = tk.Tk() #initialize root for window
root.geometry("700x500")
frm = ttk.Frame(root, padding=10)
frm.grid()

parliament = parliament.parliament()

entryMil = tk.Entry(root)
entryMil.insert(0, parliament.militarists)
entryMil.grid(column=1, row=4)
milLab = tk.Label(root, text="Number of Militarists: ").grid(column=0, row=4)

entryXPho = tk.Entry(root)
entryXPho.insert(0, parliament.xenophobes)
entryXPho.grid(column=1, row=5)
xphoLab = tk.Label(root, text="Number of Xenophobes: ").grid(column=0, row=5)

entryEgal = tk.Entry(root)
entryEgal.insert(0, parliament.egalitarians)
entryEgal.grid(column=1, row=6)
egalLab = tk.Label(root, text="Number of Egalitarians: ").grid(column=0, row=6)

entryMat = tk.Entry(root)
entryMat.insert(0, parliament.materialists)
entryMat.grid(column=1, row=7)
matLab = tk.Label(root, text="Number of Materialists: ").grid(column=0, row=7)

entryPac = tk.Entry(root)
entryPac.insert(0, parliament.pacifists)
entryPac.grid(column=1, row=8)
pacLab = tk.Label(root, text="Number of Pacifists: ").grid(column=0, row=8)

entryXPhi = tk.Entry(root)
entryXPhi.insert(0, parliament.xenophiles)
entryXPhi.grid(column=1, row=9)
xphiLab = tk.Label(root, text="Number of Xenophiles: ").grid(column=0, row=9)

entryAuth = tk.Entry(root)
entryAuth.insert(0, parliament.authoritarians)
entryAuth.grid(column=1, row=10)
authLab = tk.Label(root, text="Number of Authoritarians: ").grid(column=0, row=10)

entrySpir = tk.Entry(root)
entrySpir.insert(0, parliament.spiritualists)
entrySpir.grid(column=1, row=11)
spirLab = tk.Label(root, text="Number of Spiritualists: ").grid(column=0, row=11)




tk.Label(root, text="Select Ethic Aligned with Vote").grid(column=3, row=3)
factionSelect = tk.IntVar(root,MILITARIST)

tk.Radiobutton(root, text="Militarist Aligned Vote", variable=factionSelect, value=MILITARIST).grid(column=3, row=4)
tk.Radiobutton(root, text="Xenophobe Aligned Vote", variable=factionSelect, value=XENOPHOBE).grid(column=3, row=5)
tk.Radiobutton(root, text="Egalitarian Aligned Vote", variable=factionSelect, value=EGALITARIAN).grid(column=3, row=6)
tk.Radiobutton(root, text="Materialist Aligned Vote", variable=factionSelect, value=MATERIALIST).grid(column=3, row=7)
tk.Radiobutton(root, text="Pacifist Aligned Vote", variable=factionSelect, value=PACIFIST).grid(column=3, row=8)
tk.Radiobutton(root, text="Xenophile Aligned Vote", variable=factionSelect, value=XENOPHILE).grid(column=3, row=9)
tk.Radiobutton(root, text="Authoritarian Aligned Vote", variable=factionSelect, value=AUTHORITARIAN).grid(column=3, row=10)
tk.Radiobutton(root, text="Spiritualist Aligned Vote", variable=factionSelect, value=SPIRITUALIST).grid(column=3, row=11)


ttk.Button(frm, text="Simulate Parliament", command=lambda: parliament.runVote(factionSelect.get())
           ).grid(column=0,row=1)

ttk.Button(frm, text="New Parliament", command= lambda: parliament.createParliament(int(entryMil.get()),
                                                                                    int(entryXPho.get()),
                                                                                    int(entryEgal.get()),
                                                                                    int(entryMat.get()),
                                                                                    int(entryPac.get()),
                                                                                    int(entryXPhi.get()),
                                                                                    int(entryAuth.get()),
                                                                                    int(entrySpir.get()))
           ).grid(column=0,row=2)
ttk.Button(frm, text="Store Current Parliament", command=lambda: parliament.storeParliament()).grid(column=5, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=12)

root.mainloop()




