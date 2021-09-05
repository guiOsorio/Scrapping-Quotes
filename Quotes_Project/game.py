quote = "I'm not a man till I have a woman"
author = "Gui Osorio"
facts = ["He has a twin brother", "He plays tennis", "He studies programming"]

print("\nWELCOME TO THE QUOTES SCRAPPING GAME!\n")


chances = 3
print(f"\"{quote}\"")
answer = input("Which author claims the quote above? ")
if answer.upper() == author.upper():
    print(f"\nThat is correct, the author is {author}!")
    print("YOU WIN")
else:
    chances -= 1
    while True:
        print(f"\nWRONG")
        print(f"You have {chances} chance(s) left")
        print(f"Here is a trivia fact about the author to help you out: - {facts[-1]}\n")
        facts.pop()
        answer = input("Who is the author? ")
        if answer.upper() == author.upper():
            print(f"That is correct, the author is {author}!")
            break
        chances -= 1
        if chances == 0:
            print("\nGAME OVER, YOU LOST")
            break
