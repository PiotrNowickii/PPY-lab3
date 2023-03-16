questionOne = "Jak masz na imię oraz nazwisko?"
print(questionOne)
name = input("Imie: ")
surname = input("Nazwisko: ")
questionTwo = "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?"
answerTwo = input(questionTwo + "\na.oglądanie telewizji/filmów/seriali\nb.czytanie książek/czasopism\nc.słuchanie muzyki\nd.spotkania z rodziną/przyjaciółmi\ne.podróżowanie\nf.uprawianie sportu\n")
if answerTwo.lower() == 'a':
    answerTwo = "Oglądanie telewizji/filmów/seriali"
elif answerTwo.lower() == 'b':
    answerTwo = "Czytanie książek/czasopism"
elif answerTwo.lower() == 'c':
    answerTwo = "Słuchanie muzyki"
elif answerTwo.lower() == 'd':
    answerTwo = "Spotkania z rodziną/przyjaciółmi"
elif answerTwo.lower() == 'e':
    answerTwo = "Podróżowanie"
elif answerTwo.lower() == 'f':
    answerTwo = "Uprawianie sportu"
else:
    answerTwo = "ERROR"
    print("ERROR")
questionThree = "W jakich okolicznościach czytasz książki najczęściej?"
answerThree = input(questionThree + "\na.podczas podróży\nb.w czasie wolnym (po pracy, na urlopie)\nc.podczas pracy/nauki (to ich element)\nd.w ogóle nie czytam\n")
if answerThree.lower() == 'a':
    answerThree = "Podczas podróży"
elif answerThree.lower() == 'b':
    answerThree = "W czasie wolnym (po pracy, na urlopie)"
elif answerThree.lower() == 'c':
    answerThree = "Podczas pracy/nauki (to ich element)"
elif answerThree.lower() == 'd':
    answerThree = "W ogóle nie czytam"
else:
    answerThree = "ERROR"
    print("ERROR")
questionFour = "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?"
answerFour = input(questionFour + "\na.chęć poszerzenia wiedzy\nb.czytanie mnie relaksuje/odpręża\nc.fakt, że czytanie jest modne\nd.czytanie to moje hobby\ne.konieczność nauki w związku z wykonywaną pracą/studiami\nf.odczuwam presję rodziny/środowiska, żeby czytać\n")
if answerFour.lower() == 'a':
    answerFour = "Chęć poszerzenia wiedzy"
elif answerFour.lower() == 'b':
    answerFour = "Czytanie mnie relaksuje/odpręża"
elif answerFour.lower() == 'c':
    answerFour = "Fakt, że czytanie jest modne"
elif answerFour.lower() == 'd':
    answerFour = "Czytanie to moje hobby"
elif answerFour.lower() == 'e':
    answerFour = "Konieczność nauki w związku z wykonywaną pracą/studiami"
elif answerFour.lower() == 'f':
    answerFour = "Odczuwam presję rodziny/środowiska, żeby czytać"
else:
    answerFour = "ERROR"
    print("ERROR")

print("pytanie: " + questionOne)
print("odpowiedź: " + name + " " + surname)

print("pytanie: " + questionTwo)
print("odpowiedź: " + answerTwo)

print("pytanie: " + questionThree)
print("odpowiedź: " + answerThree)

print("pytanie: " + questionFour)
print("odpowiedź: " + answerFour)
