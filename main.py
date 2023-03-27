import json
import random
import os
from pop import pop
import parliament
from definitions import *
import tkinter as tk
import _tkinter
from tkinter import ttk

def runVote():
    global outcome
    global voteSession
    outcome = parliament.runVote(factionSelect.get(), twoThirds.get(), unanimous.get(), atWar.get(), crisisThreat.get())
    voteSessionVar.set(voteSession)
    ttk.Label(root, textvariable=voteSessionVar).grid(column=1, row=14, ipadx=10, ipady=10, sticky=tk.W)
    if outcome:
        vote.set("VOTE PASSED")
    else:
        vote.set("VOTE FAILED  ")
    voteSession += 1
    ttk.Label(root, textvariable=vote).grid(column=1, row=15, ipadx=10, ipady=10, sticky=tk.W)
    #print(outcome)

outcome = True

root = tk.Tk() # initialize root for window
#root.config(bg="white")
root.geometry("800x500")
root.title("Stellaris Parliament Simulator")
root.resizable(False, False)

#Set up a frame (Top right, contains all buttons)
frm = ttk.Frame(root, padding=5)
frm.grid()

prevVotes = []
parliament = parliament.parliament()
voteSession = 1

entryMil = tk.Entry(root)
entryMil.insert(0, parliament.militarists)
entryMil.grid(column=1, row=4,sticky=tk.W)
milLab = tk.Label(root, text="Number of Militarists: ").grid(column=0, row=4,sticky=tk.W)

entryXPho = tk.Entry(root)
entryXPho.insert(0, parliament.xenophobes)
entryXPho.grid(column=1, row=5,sticky=tk.W)
xphoLab = tk.Label(root, text="Number of Xenophobes: ").grid(column=0, row=5,sticky=tk.W)

entryEgal = tk.Entry(root)
entryEgal.insert(0, parliament.egalitarians)
entryEgal.grid(column=1, row=6,sticky=tk.W)
egalLab = tk.Label(root, text="Number of Egalitarians: ").grid(column=0, row=6,sticky=tk.W)

entryMat = tk.Entry(root)
entryMat.insert(0, parliament.materialists)
entryMat.grid(column=1, row=7,sticky=tk.W)
matLab = tk.Label(root, text="Number of Materialists: ").grid(column=0, row=7,sticky=tk.W)

entryPac = tk.Entry(root)
entryPac.insert(0, parliament.pacifists)
entryPac.grid(column=1, row=8,sticky=tk.W)
pacLab = tk.Label(root, text="Number of Pacifists: ").grid(column=0, row=8,sticky=tk.W)

entryXPhi = tk.Entry(root)
entryXPhi.insert(0, parliament.xenophiles)
entryXPhi.grid(column=1, row=9,sticky=tk.W)
xphiLab = tk.Label(root, text="Number of Xenophiles: ").grid(column=0, row=9,sticky=tk.W)

entryAuth = tk.Entry(root)
entryAuth.insert(0, parliament.authoritarians)
entryAuth.grid(column=1, row=10,sticky=tk.W)
authLab = tk.Label(root, text="Number of Authoritarians: ").grid(column=0, row=10,sticky=tk.W)

entrySpir = tk.Entry(root)
entrySpir.insert(0, parliament.spiritualists)
entrySpir.grid(column=1, row=11,sticky=tk.W)
spirLab = tk.Label(root, text="Number of Spiritualists: ").grid(column=0, row=11,sticky=tk.W)




tk.Label(root, text="Select Ethic Aligned with Vote").grid(column=3, row=3)
factionSelect = tk.IntVar(root,MILITARIST)

tk.Radiobutton(root, text="Militarist Aligned Vote", variable=factionSelect, value=MILITARIST).grid(column=3, row=4,sticky=tk.W)
tk.Radiobutton(root, text="Xenophobe Aligned Vote", variable=factionSelect, value=XENOPHOBE).grid(column=3, row=5,sticky=tk.W)
tk.Radiobutton(root, text="Egalitarian Aligned Vote", variable=factionSelect, value=EGALITARIAN).grid(column=3, row=6,sticky=tk.W)
tk.Radiobutton(root, text="Materialist Aligned Vote", variable=factionSelect, value=MATERIALIST).grid(column=3, row=7,sticky=tk.W)
tk.Radiobutton(root, text="Pacifist Aligned Vote", variable=factionSelect, value=PACIFIST).grid(column=3, row=8,sticky=tk.W)
tk.Radiobutton(root, text="Xenophile Aligned Vote", variable=factionSelect, value=XENOPHILE).grid(column=3, row=9,sticky=tk.W)
tk.Radiobutton(root, text="Authoritarian Aligned Vote", variable=factionSelect, value=AUTHORITARIAN).grid(column=3, row=10,sticky=tk.W)
tk.Radiobutton(root, text="Spiritualist Aligned Vote", variable=factionSelect, value=SPIRITUALIST).grid(column=3, row=11,sticky=tk.W)

twoThirds = tk.BooleanVar(root, False)
twoThirdsButton = tk.Checkbutton(root, text="twoThirds vote required",variable=twoThirds).grid(column=4, row=4,sticky=tk.W)
unanimous = tk.BooleanVar(root, False)
unanimousButton = tk.Checkbutton(root, text="unanimous vote required",variable=unanimous).grid(column=4, row=5,sticky=tk.W)
atWar = tk.BooleanVar(root, False)
atWarButton = tk.Checkbutton(root, text="at war",variable=atWar).grid(column=4, row=6,sticky=tk.W)
crisisThreat = tk.BooleanVar(root, False)
crisisThreatButton = tk.Checkbutton(root, text="under crisis threat",variable=crisisThreat).grid(column=4, row=7,sticky=tk.W)

ttk.Button(frm, text="Simulate Parliament",command=lambda: runVote()).grid(
        column=2, row=0, ipady=10, ipadx=10)
ttk.Button(frm, text="New Parliament", command= lambda: parliament.createParliament(int(entryMil.get()),
                                                                                    int(entryXPho.get()),
                                                                                    int(entryEgal.get()),
                                                                                    int(entryMat.get()),
                                                                                    int(entryPac.get()),
                                                                                    int(entryXPhi.get()),
                                                                                    int(entryAuth.get()),
                                                                                    int(entrySpir.get()))
           ).grid(column=0,row=1,sticky=tk.W)
ttk.Button(frm, text="Store Current Parliament", command=lambda: parliament.storeParliament()).grid(column=0, row=2, sticky=tk.W)
ttk.Button(frm, text="Clear Parliament", command=lambda: parliament.clearParliament(root)).grid(column=0, row=3,sticky=tk.W)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0,sticky=tk.W+tk.N)

ttk.Label(root, text="Session ").grid(column=0, row=14, ipadx=10, ipady=10, sticky=tk.W)
ttk.Label(root, text="OUTCOME: ").grid(column=0, row=15, ipadx=10, ipady=10, sticky=tk.W)
vote = tk.StringVar()
voteSessionVar = tk.StringVar()

root.mainloop()



