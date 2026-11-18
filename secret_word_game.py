import requests
response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
secret_word = response.json()[0]

import random

max_attempts = 10
secret_word_split = [secret_word.split]
game_attempts = 0

def game_start(start_game):
    attempts = 0
    user_guess = input("Enter a guess: ")
    if user_guess != secret_word:
        print("Incorrect guess")
        attempts +=1
        return attempts
        for i in range(secret_word_split):
            randint(secret_word_split.len)
            print(i[randint])
    elif user_guess == secret_word:
        print("Congratulations! You guessed the word!")
        game_attempts = attempts
        new_round = input("Enter 'yes' to begin a new round: ").lower
        if new_round == "yes":
            print(game_start(new_round))
            game_number += 1
        elif new_round == "no":
            best_score = input("Would you like to see your best score?").lower
            if best_score == "yes":
                print(score_keeping)
            else:
                print("Thank you for playing!")
    if attempts == max_attempts:
        print("Maximum number of attempts reached. Secret word was not guessed. Game lost. Secret word: ", secret_word)
        game_attempts = attempts
        new_round = input("Enter 'yes' to begin a new round: ").lower
        if new_round == "yes":
            print(game_start(new_round))
            game_number += 1
        elif new_round == "no":
            best_score = input("Would you like to see your best score?").lower
            if best_score == "yes":
                print(score_keeping)
            else:
                print("Thank you for playing!")

start_game = input("Enter 'start' to begin a new game: ").lower
if start_game == "start":
    print(game_start(start_game))
    game_number = 1


def score_keeping():
    all_scores = []
    for i in game_number:
        all_scores.append(game_attempts)
    return max(all_scores)