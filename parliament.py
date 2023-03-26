import json
import random
import os
from pop import pop
from definitions import *
from multipledispatch import dispatch

# PROPOSAL SETTINGS
operation = SIM_PARLIAMENT # RUN_ELECTION or SIM_PARLIAMENT
ethicOfProposal = SPIRITUALIST
twoThirdsREQ = False
unanimousREQ = False
crisisSolution = False
underThreat = True

class parliament:
    @dispatch(int, int, int, int, int, int, int, int)
    def __init__(self, mil, xenPho, egal, mat, pac, xenPhi, auth, spir):
        self.__militarists = mil
        self.__xenophobes = xenPho
        self.__egalitarians = egal
        self.__materialists = mat
        self.__pacifists = pac
        self.__xenophiles = xenPhi
        self.__authoritarians = auth
        self.__spiritualists = spir
        self.__totalPops = mil + xenPho + egal + mat + pac + xenPhi + auth + spir
        self.__parliament = []
        self.createParliament(mil, xenPho, egal, mat, pac, xenPhi, auth, spir)

    @dispatch()
    def __init__(self):
        self.__parliament = []
        self.readParliament()
        self.__militarists = 0
        self.__xenophobes = 0
        self.__egalitarians = 0
        self.__materialists = 0
        self.__pacifists = 0
        self.__xenophiles = 0
        self.__authoritarians = 0
        self.__spiritualists = 0
        self.__totalPops = len(self.__parliament)



    @property
    def parliament(self):
        return self.__parliament


    def readParliament(self):
        with open("parliament.json", 'r') as inFile:
            data = json.load(inFile)
            for i in data:
                primEthic = i.get("primary")
                tempEthics = []
                tempEthics.append(i.get("militarist"))
                tempEthics.append(i.get("xenophobe"))
                tempEthics.append(i.get("egalitarian"))
                tempEthics.append(i.get("materialist"))
                tempEthics.append(i.get("pacifist"))
                tempEthics.append(i.get("xenophile"))
                tempEthics.append(i.get("authoritarian"))
                tempEthics.append(i.get("spiritualist"))
                self.__parliament.append(pop(primEthic,tempEthics[MILITARIST], tempEthics[XENOPHOBE], tempEthics[EGALITARIAN],
                                      tempEthics[MATERIALIST], tempEthics[PACIFIST], tempEthics[XENOPHILE],
                                      tempEthics[AUTHORITARIAN], tempEthics[SPIRITUALIST], i.get("volitility")))
            self.__totalPops = len(self.__parliament)

    def storeParliament(self):
        output = []
        for i in self.__parliament:
            temp = {
                "primary": i.primaryEthic,
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
            json.dump(output, outFile, indent=4)

    def runVote(self, factionBias):
        inFavor = 0
        against = 0
        for i in self.parliament:
            if i.vote(factionBias, crisisSolution, underThreat):
                inFavor += 1
            else:
                against += 1
        print(str(inFavor) + " VS " + str(against))
        if unanimousREQ:
            if against != 0:
                print("VOTE FAILED")
                return False
            else:
                print("VOTE PASSED")
                return True
        elif twoThirdsREQ:
            if inFavor >= int(2 * (self.__totalPops) / 3):
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
                return self.runVote(factionBias)
            else:
                print("VOTE FAILED")
                return False

    def createParliament(self, numMil, numXenPho, numEgal, numMat, numPac, numXenPhi, numAuth, numSpir):
        self.__parliament = []
        self.__totalPops = numMil + numXenPho + numEgal + numMat + numPac + numXenPhi + numAuth + numSpir
        for i in range(self.__totalPops):
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
                tempPop = pop(random.randint(0, 8))  # Random ethics if population is larger than factions
            self.__parliament.append(tempPop)