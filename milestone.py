movies = []
error= "Failed to load!.Enter a valid a command!"
MENU_PROMPT = "Enter 'a' to add a movie OR Enter 's' to show movies OR Enter 'f' to find a movie OR Enter 'q' to exit: "

def add_movie():
    title = input("Enter the moive title : ")
    director = input("Enter the moive director : ")
    year = input("Enter the moive year : ")

    movies.append({
        'title':title,
        'director':director,
        'year':year,
    })


def show_movies():
    for show_movie in movies:
        print_show_movie(show_movie)

def print_show_movie(show_movie):
    print(f"Title{show_movie['title']}")
    print(f"Director{show_movie['director']}")
    print(f"Year{show_movie['year']}")

def find_movie():
    search_title=input("Enter movie title you have added!")
    for show_movie in movies:
        if show_movie['title']== search_title :
            print_show_movie(show_movie)


user_options ={
    "a":add_movie,
    "s":show_movies,
    "f":find_movie,
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q' :
        if selection in user_options :
            selectrd_function = user_options[selection]
            selectrd_function()
        else: 
            print(error)
        selection = input(MENU_PROMPT)        
menu()


 # if selection == 'a' :
        #     add_movie()
        # elif selection == 's' :
        #     show_movies()
        # elif selection == 'f' :
        #     find_movie()