def isbn_dictionary(filename):
    global res
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print ("The file {0} was not found.".format(filename))
        return None
    res = {}
    file.close
    for lines in file:
        #res[(lines.split(",")[2])] = ((lines.split(",")[0]),(lines.split(",")[1]))
        res[(lines[:-1].split(",")[2])] = ((lines[:-1].split(",")[0]),(lines[:-1].split(",")[1]))
    return res