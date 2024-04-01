f = 0

def t_movie():
    global f
    f = f + 1
    print("Which movie do you want to watch?")
    print("1. Movie 1")
    print("2. Movie 2")
    print("3. Movie 3")
    print("4. Back")
    movie = int(input("Choose your movie: "))
    if movie == 4:
        center()
        return 0
    if f == 1:
        theater()

def theater():
    print("Which screen do you want to watch the movie on?")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    a = int(input("Choose your screen: "))
    ticket = int(input("How many tickets do you want?: "))
    timing(a)

def timing(a):
    time_options = {
        1: {
            "1": "10.00-1.00",
            "2": "1.10-4.10",
            "3": "4.20-7.20",
            "4": "7.30-10.30"
        },
        2: {
            "1": "10.15-1.15",
            "2": "1.25-4.25",
            "3": "4.35-7.35",
            "4": "7.45-10.45"
        },
        3: {
            "1": "10.30-1.30",
            "2": "1.40-4.40",
            "3": "4.50-7.50",
            "4": "8.00-10.45"
        }
    }
    if a in time_options:
        print("Choose your time:")
        print(time_options[a])
        t = input("Select your time: ")
        if t in time_options[a]:
            x = time_options[a][t]
            print("Successful! Enjoy the movie at " + x)

def movie(theater):
    if 1 <= theater <= 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Wrong choice")

def center():
    print("Which theater do you wish to see the movie?")
    print("1. Inox")
    print("2. Jio")
    print("3. PVR")
    print("4. Back")
    a = int(input("Choose your option: "))
    movie(a)
    return 0

def city():
    print("Hi! Welcome to movie ticket booking.")
    print("Where do you want to watch the movie?")
    print("1. City 1")
    print("2. City 2")
    print("3. City 3")
    place = int(input("Choose your option: "))
    if 1 <= place <= 3:
        center()
    else:
        print("Wrong choice")

city()  # It calls the function city

