def noll():
    passolw = "279307asKL"
    lives = 3
    for i in range(3):
        askpalow = input("Введите Пароль - ")
        if askpalow == passolw:
            print ("Молодец! Ты прошёл проверку")
        else:
            lives = lives - 1
            print ("У тебя осталось")
            print (lives)
            print ("Попытки")

        if lives == 0:
            print ("Ты не прошёл проверку")

noll()