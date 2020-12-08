import getFollowers
import getBio
import getLikes

choice = input("Type \"help\" for help\n")
if choice == "followers":
    getFollowers.getFollowers()
if choice == "likes":
    getLikes.getLikes()
if choice == "bio":
    getBio.getBio()
if choice == "help":
    print("""bio -- Prints a user's bio.
followers -- Prints the amount of followers a user has.
likes -- Prints the ammount of likes a user has""")
