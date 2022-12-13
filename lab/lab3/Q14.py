def hunting_animals(weather, animal, n):
    if weather == "sunny" and animal == "rabbit":
        return n
    elif weather == "rainy" and animal == "deer":
        return n//3
    else:
        return n//2