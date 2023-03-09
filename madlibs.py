while True:
    option = int(input("Hello! Please enter the number 1, 2 or 3 to pick one of the texts: \n "))
    while True:
        if option == 1:
            print("Let's get started.\n")
            number1 = (input("Enter a number: "))
            measure_of_time1 = input("Enter a measure of time: ")
            transport = input("Name a mode of transportation: ")
            adjective1 = input("Enter an adjective: ")
            adjective2 = input("Enter an adjective: ")
            noun1 = input("Enter a plural noun: ")
            color1 = input("Enter a color: ")
            body_part1 = input("Name a body part: ")
            verb1 = input("Enter a verb: ")
            number2 = input("Enter a number: ") 
            noun2 = input("Enter a noun: ")
            noun3 = input("Enter a singular noun: ")
            body_part2 = input("Name a body part: ")
            verb2 = input("Enter a verb(action): ")
            noun4 = input("Enter a noun: ")
            adjective3 = input("Enter an adjective: ")
            silly_word_lol = input("Enter a silly word: ")
            noun5 = input("Enter a noun: ")

            if number1 == 1:
                print("It was ", number1, measure_of_time1, "ago when I arrived at the hospital in/on a", transport, ".")
            elif number1 == "one":
                print("It was ", number1, measure_of_time1, "ago when I arrived at the hospital in/on a", transport, ".")
            else:
                print("It was ", number1, measure_of_time1 + "s ago when I arrived at the hospital in/on a", transport, ".")
            print("The hospital is a/an", adjective1, "place, there are a lot of", adjective2, noun1, "here.")
            print("There are nurses here who have", color1, body_part1 + "(s).")
            print("If someone wants to come into my room I told them that they have to", verb1, "first.")
            if number2 == 1:
                print("I've decorated my room with", number2, noun2 + ".")
            elif number2 == "one":
                print("I've decorated my room with", number2, noun2 + ".")
            else:
                print("I've decorated my room with", number2, noun2 + "s.")
            print("Today I talked to a doctor and they were wearing a", noun3, "on their", body_part2 + ".")
            print("I heard that all the doctors", verb2, noun4, "every day for breakfast.")
            print("The most", adjective3, "thing about being in the hospital is the", silly_word_lol, noun5 + "!\n")
            print("Done!\n")
            break


        # text2
        if option == 2:
            print("Let's get started.\n")
            name = input("Enter a person's name: ")
            noun6 = input("Enter a noun: ")
            adjective_feeling1 = input("Enter an adjective describing a feeling(e.g., happy, sad, etc.): ")
            verb3 = input("Enter a verb: ")
            adjective_feeling2 = input("Enter an adjective describing a feeling(e.g., happy, sad, etc.): ")
            animal1 = input("Enter an animal's name: ")
            color2 = input("Enter a color: ")
            verb_ing1 = input("Enter a verb+ing: ")
            adverb = input("Enter a adverb(ending in ly): ")
            number3 = input("Enter a number: ")
            measure_of_time2 = input("Enter a measure of time: ")
            color3 = input("Enter a color: ")
            animal2 = input("Enter an animal's name: ")
            number4 = input("Enter a number: ")
            silly_word = input("Write a silly word(adjective): ")
            noun7 = input("Enter a noun (personal noun for better experience lol): ")

            print("This weekend I am going camping with " + name + ".")
            print("I packed my lantern, sleeping bag, and " + noun6 + ".")
            print("I am so " + adjective_feeling1 + " to " + verb3 + " in a tent.")
            print("I am " + adjective_feeling2 + " we might see a(n) " + animal1 + ", I hear they're kind of dangerous.")
            print("I have heard that the " + color3 + " lake is great for " + verb_ing1 + ".")
            if number3 == 1:
                print("Then we will " + adverb + " hike through the forest for " + number3 + " " + measure_of_time2 + ".")
            else:
                print("Then we will " + adverb + " hike through the forest for " + number3 + " " + measure_of_time2 + "s.")
            print("If I see a " + color3 + " " + animal2 + " while hiking, I am going to bring it home as a pet!")
            print("At night we will tell " + number4 + " " + silly_word + " stories and roast " + noun7 +
                  " around the campfire.\n")
            print("Done!\n")
            break


        # text3
        if option == 3:
            print("Let's get started.\n")
            name2 = input("Enter a person's name: ")
            adjective4 = input("Enter an adjective: ")
            color4 = input("Enter a color: ")
            animal3 = input("Enter an animal's name: ")
            place = input("Enter a place: ")
            adjective5 = input("Enter an adjective: ")
            magical_creature1 = input("Write magical creatures' name(plural): ")
            adjective6 = input("Enter an adjective: ")
            magical_creature2 = input("Write magical creatures' name(plural): ")
            room = input("Write name of a room in a house: ")
            noun8 = input("Enter a noun: ")
            noun9 = input("Enter a noun: ")
            noun10 = input("Enter a plural noun: ")
            adjective7 = input("Enter an adjective: ")
            noun11 = input("Enter a plural noun: ")
            number5 = input("Enter a number: ")
            measure_of_time3 = input("Enter a measure of time: ")
            verb_ing2 = input("Enter a verb+ing: ")
            adjective8 = input("Enter an adjective: ")
            noun12 = input("Enter a plural noun: ")

            print("Dear " + name2 + ", I am writing to you from a " + adjective4 + " castle in an enchanted forest.")
            print("I found myself here one day after going for a ride on a " + color4, animal3, "in", place + ".")
            print("There are", adjective5, magical_creature1, "and", adjective6, magical_creature2, "here!")
            print("In the", room, "there is a pool full of", noun8 + "(s).")
            print("I fall asleep each night on a", noun9, "of", noun10, "and dream of", adjective7, noun11 + ".")
            print("It feels as though I have lived here for", number5, measure_of_time3 + ".")
            print("I hope one day you can visit, although the only way to get here now is", verb_ing2, "on a",
                  adjective8,
                  noun12 + "!!\n")
            print("Done!\n")
            break

        else:
            import random
            option = random.randint(1, 3)
            print("Wrong number lol, I'll pick it for you.\n")
            continue
            
    answer = input("Do you want to play again?(Enter Yes or No): \n")
    if answer == "Yes":
        continue
    elif answer == "No":
        break
        
print("Bye!")
