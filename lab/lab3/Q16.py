def compare_strings(string1, string2):
    if string1[0] == string2[0]:
        if len(string1) > len(string2):
            return string1
        elif len(string1) == len(string2):
            return "error"
        else:
            return string2
    else:
        if string1[-1] > string2[-1]:
            return string1
        elif string1[-1] == string2[-1]:
            return "error"
        else:
            return string2