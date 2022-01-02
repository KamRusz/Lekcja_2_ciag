print ('Podaj liczbę od 1 do 100')
liczba = int(input())
dlugosc = 1
while liczba:
    if not liczba % 2:
        liczba = liczba /2
       # print (liczba)
        dlugosc += 1
    elif liczba % 2:
        liczba = liczba*3 + 1
        #print (liczba)
        dlugosc += 1
    if liczba == 1:
       # print ("stop")
        print (f"długość ciągu Colatza to {dlugosc} liczb")
        break
