print ('Podaj liczbę od 1 do 100')
liczba = int(input())
while liczba:
    if not liczba % 2:
        liczba = liczba /2
        print (liczba)
    elif liczba % 2:
        liczba = liczba*3 + 1
        print (liczba)
    if liczba == 1:
        print ("stop")
        break
