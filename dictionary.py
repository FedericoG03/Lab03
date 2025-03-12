class Dictionary:
    def __init__(self,nome):
        self.nome = nome
        self._dict = []

        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        try:
            # file = open(dict, 'r', encoding='UTF-8')
            with open(dict, 'r', encoding='utf-8') as file:
                for linea in file.readlines():
                    try:
                        self._dict.append(linea.lower().strip())
                    except ValueError:
                        pass
            file.close()
        except FileNotFoundError:
            print(f"Il file {dict} non esiste.")
            pass  # Nessun punteggio salvato finora
        except Exception as e:
            print(f"Errore durante la lettura del file")

    def printAll(self):
        if not self._dict:
            print("Il dizionario è vuoto.")
        else:
            for parola in self._dict:
                print(f"{parola}")
        pass

    @property
    def dict(self):
        return self._dict