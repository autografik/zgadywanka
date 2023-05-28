### 'Zgadywanka' is litle application alowed to guess rundomed numbers 
#   and inform a gamer about his results  ###
import random
import os 

# start the game
print("\n\n\t\tZGADYWANKA\n\tLosuj 6 liczb spośród 49-ciu\n")
game = input("Gramy? (wybierz tak = t lub zakończ - nie = n): ")

#   Checked if the gamer chose corresponding character
while game != 't' and game != 'n':
    print("Błąd wyboru!\nSprubuj ponoenie ...")
    game = input("Gramy? (wybierz TAK = t lub zakończ - NIE = n): ")
#   declatations variables and the others
rundomed = []
guessed = []
num = 0
nums = 0
#   main loop of application
while game == 't':
    print("OK, a więc losuj liczbę: ")
    #   get the numbers guessed by gamer
    for i in range(6):
        try:    #   if the gamer hit wrong key, applications inform his  
            nums = int(input(" \tnr " + str(i + 1) + ": "))
            while nums is not int:
                #print("Podaj liczbę: ", i)
                nums = int(input(" \tnr " + str(i - 1) + ": "))
                print("Nr liczby: " + str(i) + "wartość: ", nums)
                break
            if nums not in guessed:
                guessed.append(nums)
        except ValueError:
            print("To  nie liczba ...") # !!! to naley przenieść jakoś do pętli while ...
            ### 
            # jeśli pojawi się błąd napisz procedurę powrotu 
            # do tej samej komórki by wprowadzi liczbę 
            # Przewidywane błędy to:
            #   1. znak zamiast liczby
            #   2. enter zamiast liczby
            #   3. inny klawisz np.esc, tab, ... zamiast liczby
            #   4. chęć przzerwania programu
            # ###    
    #   apps draws rundom numbers
    for j in range(6):
        num = random.randint(1, 50)
        if num not in rundomed:
            rundomed.append(num)
    #   declaration variable and marg two lists of numbers
    trafione = 0
    for m in guessed:
        for n in rundomed:
            if m == n:
                trafione = trafione + 1
    #   presentation results of two lists marge
    if trafione == 0:
        print("\nPrzykro mi, ale nie odgadłeś rzadnej z wylosowanych liczb. Może spróbuj jescze raz.")
    elif trafione > 0:
        if trafione < 6:
            print("\nNieźle, odgadłeś: " + str(trafione) + " liczb(ę)y")
    else:
        print("GRATULACJE! Odgadłeś wszystkie liczby.")
    print("\nWylosowane liczby to: ")
    for i in rundomed:
        print(i, end=" ")
    print("\n\nPodałe(a)ś następujące liczby: ")
    for i in guessed:
        print(i, end=" ")    
    # new game suggestion
    game = input("\n\n\tGramy? (wybierz t = tak lub zakończ n = nie): ")
    while game != 't' and game != 'n':
        print("    OK, ale jaka jest Twoja decyzja?\n")
        game = input("Gramy? (wybierz tak = t lub zakończ - nie = n): ")
    # reset two lists and clear terminal window
    guessed.clear()
    rundomed.clear()
    os.system("clear")
# end of the game and farewell the gamer 
print("\nDziękuję, mam nadzieję, że następnym razem wybierzesz inaczej.")
