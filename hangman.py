import sys
from PhraseBank import PhraseBank

def play_one_round(PhraseBank): #plays one round of the game
    remaining_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    print("Please choose a topic")
    topic_command = int(input("(0) MOVIE \n(1) COUNTRY NAME \n(2) NBA TEAM \nEnter topic number (0,1,...): "))
    topic = PhraseBank.get_all_topics()
    if topic_command not in range(len(topic)):
        print("Invalid Topic")
        return
    phrase_topic = topic[topic_command]
    print("I am thinking of a", phrase_topic, "...")
    phrase = PhraseBank.next_phrase(phrase_topic)
    letter_stars = replace_by_stars(phrase, remaining_letters)

    wrong_guess = 0
    print("\nThe current phrase is ", letter_stars)
    while wrong_guess < 5:
        print("The letters you have not guessed yet are: " + "\n" + remaining_letters)
        guess = get_valid_guess(remaining_letters)
        remaining_letters = remaining_letters.replace(guess, "")
        if guess in phrase:
            letter_stars = replace_star_letter(phrase, letter_stars, guess)
            print("You guessed ", guess)
            print("That is present in the secret phrase.")
        else:
            print("You guessed ", guess)
            print("That is not present in the secret phrase.")
            wrong_guess = wrong_guess + 1
        print("You have made ", wrong_guess, "wrong guesses.")
        print("\nThe current phrase is ", letter_stars)
        if letter_stars == phrase:
            print("\nYOU WIN!!!!")
            return
    print("\nYou lose. The secret hrase was " + phrase)


def replace_by_stars(phrase, remaining_letters): #takes target phrase and replaces all remaining letters by *
    letter_stars = ""
    for letter in phrase:
        if letter.upper() in remaining_letters:
                letter_stars = letter_stars + "*"
        else:
                letter_stars = letter_stars + letter
    return letter_stars

def replace_star_letter(phrase, letter_stars, guess): #takes the guess and replaces the star with the letter if the guess is in the phrase
    add_letter_with_star = ""
    for i in range(len(phrase)):
        if phrase[i].upper() == guess:
            add_letter_with_star = add_letter_with_star + guess
        else:
            add_letter_with_star = add_letter_with_star + letter_stars[i]
    return add_letter_with_star 


def get_valid_guess(remaining_letters): #repeatedly prompts user for their guess until they provide one of the remaining letters
    guess = input("\nEnter your next guess: ")
    guess = guess.upper()
    while guess not in remaining_letters:
        print(guess, "is not a valid letter.")
        guess = input("The letters you have not guessed yet are:\n" + remaining_letters + "\nEnter your next guess: ")
        guess = guess.upper()
    return guess

def main():
    fname = PhraseBank(sys.argv[1])
    print("Welcome to the game of hangman. \nThe computer will pick a random phrase. \nAfter 5 wrong guesses you lose.")
    yes_no = "y"
    while yes_no == "y":
        play_one_round(fname)
        yes_no = input("Do you want to play again? (y/n) ")
    if yes_no == "n":
        print("Goodbye!")
    else:
        print("Invalid command")
main()
