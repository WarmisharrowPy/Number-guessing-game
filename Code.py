 name = input("What is your name? ")
        print("Good Luck ! ", name)
        words = ['1', '2', '3', '4',
                 '5', '6', '7', '8',
                 '9']
        word = random.choice(words)
        print("Guess the Number")
        guesses = ''
        turns = 3
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You Win")
                print("The word is: ", word)
                break
            guess = input("guess a Number:")
            guesses += guess
            if guess not in word:
                turns -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')
                if turns == 0:
                    print("You Loose")
                    print("The word is: ", word)
