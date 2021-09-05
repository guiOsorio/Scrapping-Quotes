# https://quotes.toscrape.com/
import requests
from random import choice, shuffle
# from csv import writer
from bs4 import BeautifulSoup

# Greet player
print("WELCOME TO THE QUOTES SCRAPPING GAME!\n")

# Game logic
while True:
    response = requests.get("https://quotes.toscrape.com")

    all_quotes = []
    pagenum = 1

    # Go through all the pages with quotes
    while True:
        # Store all quotes and respective authors in a nested list (each list value contains an array with the quote at index 0 and its author at index 1)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_divs = soup.select(".quote")
        if len(quote_divs) == 0:
            break
        for div in quote_divs:
            quote = div.select(".text")[0].get_text()
            author = div.select(".author")[0].get_text()
            # Get link of 2nd span of the .quote div, and the href of the 1st a tag of that span
            quote_span = div.select('span')[1]
            author_link = quote_span.find("a")["href"]
            author_info_response = requests.get(f"https://quotes.toscrape.com{author_link}")
            author_soup = BeautifulSoup(author_info_response.text, "html.parser")
            # From author_soup, create a string representing the author's date of birth and birthplace
            # this info will be extracted from the first p tag in .author-details
            ######################################
            author_p = author_soup.select(".author-details")[0].select("p")[0]
            author_birth_date = author_p.select(".author-born-date")[0].get_text()
            author_birth_place = author_p.select(".author-born-location")[0].get_text()
            author_fact = f"This author was born {author_birth_place} on {author_birth_date}."
            all_quotes.append([quote, author, author_fact])
        pagenum += 1
        response = requests.get(f"https://quotes.toscrape.com/page/{pagenum}")

    # with open("quotes_data.csv", "w", newline="", encoding="utf-8") as csv_file:
    #     csv_writer = writer(csv_file)
    #     csv_writer.writerow(["quote", "author"])
    #     for quote in all_quotes:
    #         # Text
    #         text = quote[0]
    #         # Author
    #         author = quote[1]
    #         csv_writer.writerow([text, author])

    # Select quote and its author
    selected_quote_div = choice(all_quotes)
    selected_quote = selected_quote_div[0]
    selected_author = selected_quote_div[1]
    selected_author_fact = selected_quote_div[2]

    # Get author's initials
    initials = []
    selected_author_full = selected_author.split(" ")
    first_name = selected_author_full[0]
    last_name = selected_author_full[1]
    initials.append(first_name[0])
    initials.append(last_name[0])
    author_initials_facts = [f"This author's first name starts with {initials[0]}", f"This author's last name starts with {initials[1]}"]

    # Make list with the author's facts
    # (3 facts, two for the initials (one for each initial, and one for date and place of birth)
    author_facts = [selected_author_fact, author_initials_facts[0], author_initials_facts[1]]
    shuffle(author_facts)

    # Game logic and interface
    chances = 4
    print(f"{selected_quote}")
    answer = input("Which author claims the quote above? ")
    if answer.upper() == selected_author.upper():
        print(f"\nThat is correct, the author is {selected_author}!")
        print("YOU WIN")
    else:
        chances -= 1
        while True:
            print(f"\nWRONG")
            print(f"You have {chances} chance(s) left")
            print(f"Here is a trivia fact about the author to help you out: - {author_facts[-1]}\n")
            author_facts.pop()
            answer = input("Who is the author? ")
            if answer.upper() == selected_author.upper():
                print(f"That is correct, the author is {selected_author}!")
                break
            chances -= 1
            if chances == 0:
                print("\nGAME OVER, YOU LOST")
                break

    # After a round is played
    game_over = False
    while True:
        play_again = input("Would you like to play again? ")
        print("\n", end="")
        if play_again.upper() == "N" or play_again.upper() == "NO":
            game_over = True
            break
        elif play_again.upper() == "Y" or play_again.upper() == "YES":
            break
        else:
            print("We don't recognize your answer, please type either 'yes' or 'no'")
    
    if game_over:
        break





