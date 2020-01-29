def search(movie_list):
    choice = int(input("Enter year "))
    for i in movie_list:
        while choice in i:
            print(i[0])
            break