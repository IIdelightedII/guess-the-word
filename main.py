import os

print("Привет! Я загадал слово, твоя задача угадать его по буквам.")
input("Нажмите Enter чтобы продолжить")
os.system("cls")
print("Поехали!")


word = "дистрибутив"
attempts = 10
letters = []
guessed_letters = 0
while attempts > 0:
    print(f"твоё количество попыток: {attempts}")

    for i in range(len(word)):
        if word[i] in letters:
            print(word[i],  end =" ")
            guessed_letters += 1
            if guessed_letters == len(word):
                os.system("cls")
                print(f"Поздравляю, ты отгадал слово!: \n{word}")
                exit()

        else:
            print("*", end=" ")

    letters.append(input("\nВведи букву: "))
    os.system("cls")

    while letters[-1] in letters[0:-1]:
        del letters[-1]
        letters.append(input(f"кажется, ты уже вводил эту букву, введи другую. Вот все твои буквы: {letters}: "))

    if not letters[-1] in word:
        attempts -= 1
    guessed_letters = 0

print("К сожалению ты не отгадал слово")