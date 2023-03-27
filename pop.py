import random
from definitions import *
from multipledispatch import dispatch

class pop:
    @dispatch(int)
    def __init__(self, ethic: int):
        self.__volitility = random.randint(0,20)
        self.__primaryEthic = ethic
        self.__ethicsArr = [0 for i in range(8)]
        self.ethicsGen(ethic)

    @dispatch(int, int, int, int, int, int, int, int, int, int)
    def __init__(self, prim, mil, xepho, egal, mat, pac, xephi, auth, spir, vol):
        self.__volitility = vol
        self.__primaryEthic = prim
        self.__ethicsArr = [0 for i in range(8)]
        self.__ethicsArr[MILITARIST] = mil
        self.__ethicsArr[XENOPHOBE] = xepho
        self.__ethicsArr[EGALITARIAN] = egal
        self.__ethicsArr[MATERIALIST] = mat
        self.__ethicsArr[PACIFIST] = pac
        self.__ethicsArr[XENOPHILE] = xephi
        self.__ethicsArr[AUTHORITARIAN] = auth
        self.__ethicsArr[SPIRITUALIST] = spir


    @property
    def ethicsArr(self):
        return self.__ethicsArr

    @property
    def volitility(self):
        return self.__volitility

    @property
    def primaryEthic(self):
        return self.__primaryEthic

    def vote(self, ethic, atWar, underThreat):
        voteNum = random.randint(0,100)
        if underThreat:
            voteNum -= 25
        #print(str(self.__ethicsArr[ethic]) + " - " + str(voteNum))
        if atWar and ethic == MILITARIST:
            voteNum -= 15
        if self.__ethicsArr[ethic] - voteNum >= 0:
            return True
        else:
            return False

    def ethicsGen(self, popEthic):
        base = 5
        for i in range(8): # randomly assign odds of voting in favor, minimum of 5 - volitility, max 75 + volitility
            self.__ethicsArr[i] = base + random.randint(0,70) + (random.randint(-1,1)*self.__volitility)
        if popEthic == MILITARIST:
            self.__ethicsArr[MILITARIST] = 100 - self.__volitility
            self.__ethicsArr[PACIFIST] = self.__ethicsArr[PACIFIST] - 50
        elif popEthic == XENOPHOBE:
            self.__ethicsArr[XENOPHOBE] = 100 - self.__volitility
            self.__ethicsArr[XENOPHILE] = self.__ethicsArr[XENOPHILE] - 50
        elif popEthic == EGALITARIAN:
            self.__ethicsArr[EGALITARIAN] = 100 - self.__volitility
            self.__ethicsArr[AUTHORITARIAN] = self.__ethicsArr[AUTHORITARIAN] - 50
        elif popEthic == MATERIALIST:
            self.__ethicsArr[MATERIALIST] = 100 - self.__volitility
            self.__ethicsArr[SPIRITUALIST] = self.__ethicsArr[SPIRITUALIST] - 50
        elif popEthic == PACIFIST:
            self.__ethicsArr[PACIFIST] = 100 - self.__volitility
            self.__ethicsArr[MILITARIST] = self.__ethicsArr[MILITARIST] - 50
        elif popEthic == XENOPHILE:
            self.__ethicsArr[XENOPHILE] = 100 - self.__volitility
            self.__ethicsArr[XENOPHOBE] = self.__ethicsArr[XENOPHOBE] - 50
        elif popEthic == AUTHORITARIAN:
            self.__ethicsArr[AUTHORITARIAN] = 100 - self.__volitility
            self.__ethicsArr[EGALITARIAN] = self.__ethicsArr[EGALITARIAN] - 50
        elif popEthic == SPIRITUALIST:
            self.__ethicsArr[SPIRITUALIST] = 100 - self.__volitility
            self.__ethicsArr[MATERIALIST] = self.__ethicsArr[MATERIALIST] - 50

        for i in range(8): # checks for min and max
            if self.__ethicsArr[i] < 0:
                self.__ethicsArr[i] = 0
            elif self.__ethicsArr[i] > 100:
                self.__ethicsArr[i] = 100