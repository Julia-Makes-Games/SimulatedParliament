import json
import random
import os
from pop import pop
from definitions import *

# MODIFIABLE VARIABLES
# FACTION POPULATION
militarists = 4
xenPhobes = 0
egalitarians = 0
materialists = 0
pacifists = 0
xenPhiles = 0
authoritarians = 0
spiritualists = 0
totalPop = militarists + xenPhobes + egalitarians + materialists + pacifists + xenPhiles + authoritarians + spiritualists

# PROPOSAL SETTINGS
operation = SIM_PARLIAMENT # RUN_ELECTION or SIM_PARLIAMENT
ethicOfProposal = MILITARIST
twoThirdsREQ = False
unanimousREQ = False
crisisSolution = False
underThreat = False

parliament: list = []


def createParliament(numMil, numXenPho, numEgal, numMat, numPac, numXenPhi, numAuth, numSpir):
    global parliament
    parliament = []
    for i in range(totalPop):
        if numMil != 0:
            tempPop = pop(MILITARIST)
            numMil = numMil - 1
        elif numXenPho != 0:
            tempPop = pop(XENOPHOBE)
            numXenPho = numXenPho - 1
        elif numEgal != 0:
            tempPop = pop(EGALITARIAN)
            numEgal = numEgal - 1
        elif numMat != 0:
            tempPop = pop(MATERIALIST)
            numMat = numMat - 1
        elif numPac != 0:
            tempPop = pop(PACIFIST)
            numPac = numPac - 1
        elif numXenPhi != 0:
            tempPop = pop(XENOPHILE)
            numXenPhi = numXenPhi - 1
        elif numAuth != 0:
            tempPop = pop(AUTHORITARIAN)
            numAuth = numAuth - 1
        elif numSpir != 0:
            tempPop = pop(SPIRITUALIST)
            numSpir = numSpir - 1
        else:
            tempPop = pop(random.randint(0,8)) # Random ethics if population is larger than factions
        parliament.append(tempPop)
    storeParliament()

def storeParliament():
    output = []
    for i in parliament:
        temp = {
            "militarist": i.ethicsArr[MILITARIST],
            "xenophobe": i.ethicsArr[XENOPHOBE],
            "egalitarian": i.ethicsArr[EGALITARIAN],
            "materialist": i.ethicsArr[MATERIALIST],
            "pacifist": i.ethicsArr[PACIFIST],
            "xenophile": i.ethicsArr[XENOPHILE],
            "authoritarian": i.ethicsArr[AUTHORITARIAN],
            "spiritualist": i.ethicsArr[SPIRITUALIST],
            "volitility": i.volitility
        }
        output.append(temp)
    with open("parliament.json", 'w') as outFile:
        json.dump(output,outFile, indent=4)

def readParliament():
    with open("parliament.json", 'r') as inFile:
        data = json.load(inFile)
        for i in data:
            tempEthics = []
            tempEthics.append(i.get("militarist"))
            tempEthics.append(i.get("xenophobe"))
            tempEthics.append(i.get("egalitarian"))
            tempEthics.append(i.get("materialist"))
            tempEthics.append(i.get("pacifist"))
            tempEthics.append(i.get("xenophile"))
            tempEthics.append(i.get("authoritarian"))
            tempEthics.append(i.get("spiritualist"))
            parliament.append(pop(tempEthics[MILITARIST],tempEthics[XENOPHOBE],tempEthics[EGALITARIAN],
                                  tempEthics[MATERIALIST],tempEthics[PACIFIST],tempEthics[XENOPHILE],
                                  tempEthics[AUTHORITARIAN],tempEthics[SPIRITUALIST],i.get("volitility")))


def runVote():
    inFavor = 0
    against = 0
    for i in parliament:
        if i.vote(ethicOfProposal, crisisSolution, underThreat):
            inFavor+=1
        else:
            against+=1
    if unanimousREQ:
        if against != 0:
            print("VOTE FAILED")
            return False
        else:
            print("VOTE PASSED")
            return True
    elif twoThirdsREQ:
        if inFavor >= int(2 * (totalPop) / 3):
            print("VOTE PASSED")
            return True
        else:
            print("VOTE FAILED")
            return False
    else:
        if inFavor > against:
            print("VOTE PASSED")
            return True
        elif inFavor == against:
            print("STALEMATE, ANOTHER VOTE REQUIRED")
            return runVote()
        else:
            print("VOTE FAILED")
            return False

if operation == RUN_ELECTION:
    createParliament(militarists, xenPhobes, egalitarians, materialists, pacifists, xenPhiles, authoritarians,spiritualists)
    storeParliament()
elif operation == SIM_PARLIAMENT:
    readParliament()
    runVote()
else:
    print("INVALID OPERATION")