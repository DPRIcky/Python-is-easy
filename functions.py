# USING DEFINITION OR FUNCTION #

# Defining a function for calling the function to get the name of the artist of my favourite song #
def artist():
    print("Arijit Singh")
artist()

# Defining a function for calling the function to print the genre of my favourite song #
def genre():
    print("Acoustic music, Filmi, Indian pop")
genre()

# Defining a function for calling the function to print the year of release of my favourite song #
def year():
    print(2013)
year()

# Defining a function for checking the duration of the song is correct or not in booleans #
def check(time):
    duration = 4.22
    if (time == duration):
        print(bool(True))
    else:
        print(bool(False))
time = 4.22
check(time)