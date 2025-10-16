# Project: Movie Budgets

# 1

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

'''
# These work but unnecessary:
mv_count = len(list(map(str, movies)))
mv_count = len(list(str(n) for n in movies))
'''

budget_sum = sum(list(float(n[1]) for n in movies))
print(budget_sum)

mv_count = len(movies)
print(mv_count)

budget_mean = budget_sum / mv_count
print(budget_mean)


# 2, 3

mv_over: list[tuple[str, int]] = []

for movie in movies:
    if movie[1] > budget_mean:
        budget_over = movie[1] - budget_mean
        print(f"{movie[0]} costs ${movie[1] / 1e+06}M, which is ${budget_over / 1e+06}M more than average budget.")
        mv_over.append(movie)

print(mv_over)
print(f"There are {len(mv_over)} movies that cost more than the average budget.")


# Extra

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("How many movies do you want to add? "))

for _ in range(new_movie_count):
    title = input("Enter movie title: ")
    budget = int(input("Enter movie budget: "))
    new_movie_tuple = (title, budget)
    movies.append(new_movie_tuple)
print(movies)
