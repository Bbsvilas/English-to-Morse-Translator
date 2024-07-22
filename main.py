from Dictionary import englishToMorseDict



def EnglishToMorse(english):
    for i in english:
        print(englishToMorseDict[i.lower()], end=" ")
    print('\n')


def Query():
        english = input("What English phrase do you want to translate?\n")
        EnglishToMorse(english)


Query()

