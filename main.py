import os
import random
print("Привет! Я загадал слово, твоя задача угадать его по буквам.")
input("Нажмите Enter чтобы продолжить")
os.system("cls")
print("Поехали!")
words = ["тумба", "компьютер", "камера", "клавиатура", "линейка"]

word = random.choice(words)
attempts = 10
letters = []
guessed_letters = 0
while attempts > 0:
    guessed_letters = 0
    print(f"твоё количество попыток: {attempts}")

    for i in range(len(word)):
        if word[i] in letters:
            print(word[i],  end =" ")
            guessed_letters += 1
        else:
            print("*", end=" ")

    if guessed_letters == len(word):
        os.system("cls")
        print(f"Поздравляю, ты отгадал слово! \n{word}")
        exit()
    letter = input("\nВведи букву: ").lower()
    os.system("cls")
    if letter in letters:
        print(f"Вот все твои буквы: {letters}.\nТы уже вводил букву \"{letter}\"")
        continue
    letters.append(letter)

    if not letters[-1] in word:
        attempts -= 1

print(f"К сожалению ты не отгадал слово - {word}")