def num_words(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    if string == "":
        return count
    else:
        return count + 1