from sys import flags

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self,language,frase=None):
        self.diz = d.Dictionary(language)
        self.language = language
        self.frase = frase if frase is not None else []
        self.diz.loadDictionary(language)
        self.listaSWC = []  #ricerca contain
        self.listaSWL = []  #ricerca lineare
        self.listaSWD = []  #ricerca dicotomica

    def printDic(self, language):
        self.diz.printAll()

    def searchWord(self):
        for word in self.frase:
            if not self.diz.dict.__contains__(word.lower()):
                self.listaSWC.append(rw.RichWord(word , False))
        return self.listaSWC

    def searchWordLinear(self):
        for word in self.frase:
            flags = False
            for i in self.diz.dict:
                if i.lower() == word.lower():
                    flags = True
                    rw.RichWord(word, True)
            if flags ==False:
                self.listaSWL.append(rw.RichWord(word, False))

        return self.listaSWL

    def binary_search(self,word_list, target):
        """Esegue la ricerca dicotomica su una lista ordinata."""
        left = 0
        right = len(word_list) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_word = word_list[mid]

            if mid_word.lower() == target.lower():
                return True  # Elemento trovato
            elif mid_word.lower() < target.lower():
                left = mid + 1  # Cerca nella parte destra
            else:
                right = mid - 1  # Cerca nella parte sinistra

        return False  # Elemento non trovato

    def searchWordDic(self):
        d = sorted(self.diz.dict)
        i = len(d)/2
        for word in self.frase:
            while len(d) == 1:
                if word.lower() != d[i].lower():
                    if word < d[i]:
                        for p in range(i,len(d)):
                            d.pop(p)
                    else:
                        for p in range(0,i):
                            d.pop(p)
                    i/=2
            if not d.__contains__(word.lower()):
                self.listaSWD.append(rw.RichWord(word, False))
            else:
                rw.RichWord(word, True)
        return self.listaSWD