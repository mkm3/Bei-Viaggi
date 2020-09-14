# Travel Quiz - Prep Course Project
print("Travel Quiz - Prep Course Project")
print()
print()

# Greet user
# Ask user for their name
print("Welcome! What's your name?")
name = input("> ").title()
print()
# Used ".title()"" to ensure that what was imputted was formatted correctly

# Respond back with name input()
print("Looks like you caught the travel bug, " + name + "!")
print()

# # # # # # # # # # # # # # # # # # # # # # # # # # 
#For some of the extra fun elements in the quiz, I created those within fuctions.

def haveyoutraveled():
    while True:
        print("Tell me, {}, have you ever traveled before? Y or N".format(name))
        response1 = input("> ").upper()
        print()

        no = "N"
        yes = "Y"

        if no in response1:
            print("""No way! You got to take some vacation time to enjoy a trip abroad. I really want to help you choose your next travel destination...""")
            print()
            break

        elif yes in response1:
            print("""Taking some vacation time to enjoy a trip abroad is probably one of the most spectacular things you can do for yourself. For your next adventure, I really want to help you pick a place...""")
            print()
            break

        else:
            print("That makes no sense.")

haveyoutraveled()

# # # # # # # # # # # # # # # # # # # # # # # # # # 
# I tied my itinerary (output at the end of quiz) to variables.
# It was helpful to use the triple quotations to establish them as opposed to making each individual like a print statement

#Itineraries:
it_spain = """
Best times to go:
March to May or September to November. Why? Because you'll find cheaper accomodations around this time, less crowds and good weather occurs around this time.

Suggestions/Recommendations:
If you are looking for a wealth of historic art and architecture that dates back to the Roman Empire, we recommend you visit Toledo. It's easy to lose yourself exploring the midieval streets.

Foods to try:
Paella
Patatas bravas
Jamon Inberico
Sangria
Chorizo
Marzipan
"""

it_italy = """
Best times to go: 
April to June or September to October. Why? It can be dreadfully hot during the summer. It's more favorable to go during the Spring and Fall.

Suggestions/Recommendations:
If you are looking for a wealth of historic art and architecture that dates back to the Renaissance, Florence is your city! It's easy to lose yourself exploring this spectacular city.

Foods to try:
Bistecca Fiorentina
Ribollita
Lambredotto (Not for the faint of heart!)
Chianti wine
Gelato
"""

it_germany = """
Best times to go: 
May to September. The weather is absolutely wonderful and days are longer around this time of year. However, spring and fall are great time as that you'll typically find cheaper flights and accomodations during this time.

Suggestions/Recommendations:
If you are looking for a wealth of historic art and architecture then, Berlin is your city! You'll definitely want to drop by Museum island.

Foods to try:
Currywurst
Schnitzel
Bratwurst
Spatzle
Flammkuchen
Rouladen
"""

it_ireland = """
Best times to go: 
June through early September. Temperatures are pleasant and warm. While it rains from time to time, you can visit all year round.

Suggestions/Recommendations:
If you are looking for a warm and welcoming city, you'll want to visit Dublin. It's easy to lose yourself exploring the city pubs and breweries.

Foods to try:
Irish Stew
Boxty Pancakes
Coddle
Black and white pudding
Soda bread
Guinness
"""


#To tally up the scores for each country, I created lists and made the score one of the indices.

spain = ["Spain", 0, it_spain]
italy = ["Italy", 0, it_italy]
germany = ["Germany", 0, it_germany]
ireland = ["Ireland", 0, it_ireland]

#Then, I put those countries in one list - "country_scores"
country_scores = [spain, italy, germany, ireland]
# I did the same for the itineraries (in case I needed it later)
itineraries = [it_spain, it_italy, it_germany, it_ireland]


# I created one function to next all my questions
# I used "while True:" for each question so I could loop the question back if the user inputted an invalid answer.
# For each response, I used if, elif and else statements.
# Then, depending on the choice the user made, it would add a said number of points to the appropriate part of the country_scores list

def questions():
    # Question 1 
    print()
    print("Question 1")
    print()
    print("Which sounds like the best thing to do in your spare time?")
    print("[A] Go to a museum")
    print("[B] Spend the days outdoors, enjoy a hike")
    print("[C] Read a book")
    print("[D] Go Skydiving")


    while True:

        Q1_Input = input("> ").upper()
        print()

        if Q1_Input == "A":
            print("Going to a museum sounds like fun.")
            italy[1] += 1
            break

        elif Q1_Input == "B":
            print("Getting some fresh air sounds nice.")
            ireland[1] += 1
            break

        elif Q1_Input == "C":
            print("That sounds absolutely relaxing!")
            germany[1] += 1
            break

        elif Q1_Input == "D":
            print("How thrilling!")
            spain[1] += 1
            break
        
        else:
            print("Invalid answer.. try again")

        
    print()

    # Question 2

    print()
    print("Question 2")
    print()
    print("Humidity doesn't bother me.")
    print("[A] True")
    print("[B] False")

    while True:
        Q2_Input = input("> ").upper()
        print()
        
        if Q2_Input == "A":
            print("It's not too bad, right?")
            italy[1] += 3
            spain[1] += 3
            break

        elif Q2_Input == "B":
            print("Not your thing? No worries.")
            ireland[1] += 3
            germany[1] += 3
            break

        else:
            print("Invalid answer.. try again")
        print()

    # Question 3 

    print()
    print("Question 3")
    print()
    print("Which would you choose as your animal companion?")
    print("[A] Lion")
    print("[B] Deer")
    print("[C] Bear")
    print("[D] Wolf")
    print()

    # I also used lists to create a madlib experience.
    animal_list = ["Lion", "Deer", "Bear", "Wolf"]

    while True:
        Q3_Input = input("> ").upper()
        print()

        if Q3_Input == "A":
            italy[1] += 2
            animal = animal_list[0]
            break

        elif Q3_Input == "B":
            ireland[1] += 2
            animal = animal_list[1]
            break

        elif Q3_Input == "C":
            germany[1] += 2
            animal = animal_list[2]
            break

        elif Q3_Input == "D":
            spain[1] += 2
            animal = animal_list[3]
            break

        else:
            print("Invalid answer.. try again")

    #One of my favorite string formatting methods has got to be .format(). 
    animal_name = input("What would you name them? > ").title()
    print()
    print("I love that... {} the {}!".format(animal_name, animal))
    print()


    # Question 4
    print()
    print("Question 4")
    print()
    print("I prefer to explore places where the climate is...")
    print("[A] Sunny and Hot")
    print("[B] Warm and Breezy")
    print("[C] Mild but I'm not bothered by snow")
    print("[D] Windy and Cold")

    while True:
        Q4_Input = input("> ").upper()
        print()

        if Q4_Input == "A":
            print("You've got the attitude of a great explorer!")
            italy[1] += 2
            break

        elif Q4_Input == "B":
            print("You've got the attitude of a great explorer!")
            spain[1] += 2
            break

        elif Q4_Input == "C":
            print("You've got the attitude of a great explorer!")
            germany[1] += 2
            break

        elif Q4_Input == "D":
            print("You've got the attitude of a great explorer!")
            ireland[1] += 2
            break

        else:
            print("Invalid answer.. try again")
        print()


    # Question 5

    print()
    print("Question 5")
    print()
    print("When I study, I prefer to listen to...")
    print("[A] Classical/Opera")
    print("[B] Flamenco/Classical Guitar")
    print("[C] Folk Music/Bluegrass")
    print("[D] Trance/Techno")
    print("[E] Nothing, I prefer silence.")

    while True:
        Q6_Input = input("> ").upper()
        print()

        if Q6_Input == "A":
            print("I feel like dancing now!")
            italy[1] += 4
            break

        elif Q6_Input == "B":
            print("I feel like dancing now!")
            spain[1] += 4
            break

        elif Q6_Input == "C":
            print("I feel like dancing now!")
            ireland[1] += 4
            break

        elif Q6_Input == "D":
            print("I feel like dancing now!")
            germany[1] += 4
            break

        elif Q6_Input == "E":
            print("Understandable!")
            None
            break
        
        else:
            print("Invalid answer.. try again")
        print()
        print()


    # Question 6

    print()
    print("Question 6")
    print()
    print("Let me pour you a glass, what would you like?")
    print("[A] Wine")
    print("[B] Beer")
    print("[C] Soda")
    print("[D] Actually, I'd prefer a cup of espresso.")


    while True:
        Q6_Input = input("> ").upper()
        print()

        if Q6_Input == "A":
            print("You got it!")
            italy[1] += 3
            spain[1] += 3
            break

        elif Q6_Input == "B":
            print("Coming right up!")
            ireland[1] += 3
            germany[1] += 3
            break

        elif Q6_Input == "C":
            print("Coming right up!")
            None
            break
            
        elif Q6_Input == "D":
            print("You got it!")
            italy[1] += 3
            break

        else:
            print("Invalid answer.. try again")


# I created a fuction to add up the scores for each country. Within that function I used a "for" loop
def location_choice():

    max_score = 0
    max_country = None
    itinerary = None

    for country in country_scores:
        if max_score < country[1]:
            max_score = country[1]
            max_country = country[0]
            itinerary = country[2]

    print("\n\n\n")
    print("I think you'd love, {}!".format(max_country))
    print()

    print("Here's your itinerary, {}:".format(name))
    print(itinerary)


questions()
location_choice()

#If I had more time -----

# def play():
#   questions()
#   location_choice()

# play()

# print()
# print("**Erase before Submitting Project**")
# for item in country_scores:
#   print(item)


# Output: Suggested Travel Destination


# # # # # # # # # # # # # # # # # # # # # # # # # # 

# Actions:
# [T]ravel quiz

# Fun to haves
# [A]dd a travel plan
# [V]iew future travel dates (For Fun, Wedding, Business Trip)
# [D]elete a travel plan
# [C]ountdown travel timer (Year + Months + Days)