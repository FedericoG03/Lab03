import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.language = ""

    def handleSentence(self, frase, language):
        self.language = f"./resources/{language}.txt"
        parole = replaceChars(frase).strip().split(" ")
        dizLingua = md.MultiDictionary(self.language,parole)

        print("-------------------------------\n")
        print("Using Contains method\n")
        tI1=time.time()
        lS1=dizLingua.searchWord()
        if len(lS1) == 0:
            print("No corrections found")
        else:
            for p in lS1:
                print(p.__str__())
        tF1=time.time()
        print(f"Time: {tF1 - tI1} seconds")

        print("-------------------------------\n")
        print("Using Linear method\n")
        tI2=time.time()
        lS2=dizLingua.searchWordLinear()
        if len(lS2) == 0:
            print("No corrections found")
        else:
            for p in lS2:
                print(p.__str__())
        tF2 = time.time()
        print(f"Time: {tF2-tI2} seconds")

        print("-------------------------------\n")
        print("Using Dichotomic method\n")
        tI3 = time.time()
        lS3 = dizLingua.searchWordDic()
        if len(lS3) == 0:
            print("No corrections found")
        else:
            for p in lS3:
                print(p.__str__())
        tF3 = time.time()
        print(f"Time: {tF3-tI3} seconds")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'\".,;!?@#$%^&*()-_+=<>[]{}|"
    for c in chars:
        text = text.replace(c, "")
    return text