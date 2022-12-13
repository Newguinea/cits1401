def word_counter(input_str):
    input_str = input_str.lower()
    splite = input_str.split()
    return dict([(x,splite.count(x)) for x in set(splite)])