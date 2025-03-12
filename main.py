from dictionary import Dictionary as dc

import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    if txtIn.isdigit():
        if int(txtIn) == 1:
            print("Inserisci la tua frase in Italiano\n")
            parole = input()
            sc.handleSentence(parole,"Italian")

        if int(txtIn) == 2:
            print("Inserisci la tua frase in Inglese\n")
            parole = input()
            sc.handleSentence(parole,"English")

        if int(txtIn) == 3:
            print("Inserisci la tua frase in Spagnolo\n")
            parole = input()
            sc.handleSentence(parole,"Spanish")

        if int(txtIn) == 4:
            break
    else:
        print("ERRORE: Inserisci un numero tra 1 e 4")

