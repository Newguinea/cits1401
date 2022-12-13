def find_key(test_dictionary, value):
    new_dict = {v : k for k, v in test_dictionary.items()}
    return new_dict.get(value)