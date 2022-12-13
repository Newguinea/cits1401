"""
Author@ 114514
Date@4/10/2022
StudentNumber@114514
"""

'''
this mian function carry two argus, however there are some condition that some of our data can not be used,
if that part of data is missing or broken, our program will return a None for that part.
'''


def main(csvfile, SubjIDs):
    """
    :type csvfile: str
    :type SubjIDs: str
    """
    readfile(csvfile)  # clean the data and generate the list <IdList>, <todelete> , dictionary <res>

    # check the format of SubjIDs
    if bool(1 - isinstance(SubjIDs, list)):  # check SubjIDs is a list
        print("the SubjIDs is not a list, the data with problem is `{}`".format(SubjIDs))
        return [None, None, None, None]
    if len(SubjIDs) != 2:  # check the len if SubjIDs is 2
        print("the length of SubjIDs is not 2, the data with problem is `{}`".format(SubjIDs))
        return [None, None, None, None]
    if bool(1 - isinstance(SubjIDs[0], str)):  # check the datatype of the first element of SubjIDs is `str`
        print("the SubjIDs[0] is not a str, the data with problem is `{}`".format(SubjIDs[0]))
        return [None, None, None, None]
    if bool(1 - isinstance(SubjIDs[1], str)):  # check the datatype of the second element of SubjIDs is `str`
        print("the SubjIDs[1] is not a str, the data with problem is `{}`".format(SubjIDs[1]))
        return [None, None, None, None]
    if len(res) == 0:  # check the length of res is not 0
        print("all the data is corrupted")
        return [None, None, None, None]

    # if any one of the element of SubjIDs is not in <IdList> or <todelete>, return [None, None, None, None]
    for i in [0, 1]:
        if checkSubjID(SubjIDs[i]) == False:
            print("SubjIDs[{}] is not a valid input, it is not in file \"{}\"".format(i, csvfile))
            return [None, None, None, None]

    # determine the available data and calculate the return value
    if SubjIDs[0].upper() not in IdList and SubjIDs[1].upper() not in IdList:
        return [None, None, op3(), None]
    elif SubjIDs[0].upper() in IdList and SubjIDs[1].upper() not in IdList:
        return [[op1(SubjIDs[0]), None], [op2(SubjIDs[0]), None], op3(), None]
    elif SubjIDs[0].upper() not in IdList and SubjIDs[1].upper() in IdList:
        return [[None, op1(SubjIDs[1])], [None, op2(SubjIDs[1])], op3(), None]
    elif SubjIDs[0].upper() in IdList and SubjIDs[1].upper() in IdList:
        return [[op1(SubjIDs[0]), op1(SubjIDs[1])], [op2(SubjIDs[0]), op2(SubjIDs[1])], op3(), op4(SubjIDs)]
    else:
        return [None, None, None, None]


'''
this readfile(csvfile) function returns nothing and generate a distionary named
res, a dictionary has cleaned data from csvfile, cleaned means deleted the unavaliable data
IdList, a list has the ID that in res dictionary
'''


def readfile(csvfile):
    global res  # a dic store the data from csv file, example: {('B7033', 'ft'): [-48, -17, -24, -47, -16, -25], ...}
    global IdList  # a list store the IDs which is available for future calculation
    global todelete  # a list store the IDs which is not available for future calculation
    # ensure the <csvfile> exist
    try:
        file = open(csvfile, "r")
    except FileNotFoundError:
        print("\"{}\" is not found, please check the file name.".format(csvfile))
        return [None, None, None, None]
    # check the header, get the order of the columns, store order in a dictionary named <serial>
    normalHeader = ['subjid', 'landmark', 'ox', 'oy', 'oz', 'mx', 'my', 'mz']
    header = file.readlines()[0].rstrip().lower().split(",")
    file.close()
    headerCompare = header.copy()
    headerCompare.sort()
    tmplist = []
    for i in headerCompare:
        tmplist.append(i.replace(" ", ""))
    headerCompare = tmplist
    if (header == normalHeader):
        serial = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    elif (headerCompare == ['landmark', 'mx', 'my', 'mz', 'ox', 'oy', 'oz', 'subjid']):
        serial = {}
        for i in range(8):
            for j in range(8):
                if (normalHeader[i] == header[j]):
                    serial[i] = j
    else:
        return [None, None, None, None]
    # put the data into dictionary named <res>, use dictionary <serial> determine the position of each column
    res = {}
    file = open(csvfile, "r")
    _ = next(file)  # remove the header
    for lines in file:
        if (lines == "") or (lines.rstrip().split(",")[serial.get(0)] == "") or \
                (lines.rstrip().split(",")[serial.get(1)] == ""):
            pass
        else:
            res[(lines.rstrip().split(",")[serial.get(0)].upper(),
                 lines.rstrip().split(",")[serial.get(1)].lower())] = [
                ForceFloat(lines.rstrip().split(",")[serial.get(2)]),
                ForceFloat(lines.rstrip().split(",")[serial.get(3)]),
                ForceFloat(lines.rstrip().split(",")[serial.get(4)]),
                ForceFloat(lines.rstrip().split(",")[serial.get(5)]),
                ForceFloat(lines.rstrip().split(",")[serial.get(6)]),
                ForceFloat(lines.rstrip().split(",")[serial.get(7)])]
    file.close()
    # generate the id list named <IdList>, all the id is in a list as element
    IDtmp = []
    for key in res:
        IDtmp.append(key[0])
    IdList = list(set(IDtmp))
    '''
    #data clean part, OX,OY,OZ,MX,MY,MZ should in range[-200,200]
        for each ID, 7 Landmark should all exist, they are['ft', 'ex', 'en', 'al', 'sbal', 'ch', 'prn']
        for each ID, when landmark is 'prn', in this row, (OX,OY,OZ) == (MX,MY,MZ)
    if has ID do not satisfied the condition above,list <todelete> should add this ID
    '''
    todelete = []
    for i in IdList:
        for j in ['ft', 'ex', 'en', 'al', 'sbal', 'ch', 'prn']:
            if ((i, j) in res.keys()):
                for h in res[(i, j)]:
                    if (h < -200 or h > 200):
                        todelete.append(i)
            else:
                todelete.append(i)
        if ((i, 'prn') in res.keys()):
            if (res[(i, 'prn')][0:3] != res[(i, 'prn')][3:6]):
                todelete.append(i)
        else:
            todelete.append(i)
    # remove <todelete> duplicates, there are maybe some id has more than one problem,
    # then, delete it if it is in <IdList>.
    todelete = list(set(todelete))
    deleteid(todelete)
    for i in todelete:
        if i in IdList:
            IdList.remove(i)


'''
ForceFloat return a float number, it has one argue named <str>
if <str> can change to float number, return float(str)
,else return 114514.114514
'''


def ForceFloat(str):
    try:
        out = float(str)
    except ValueError:
        out = 114514.114514
    return out


# <idlist> is a list include the IDs need to deleted in <res>, this function deleted the unusable data
def deleteid(idlist):
    global res
    for key in list(res.keys()):
        if key[0] in idlist:
            del res[key]


# if any of <SubjID> is not in (<IdList> or <todelete>), return [None, None, None, None]
def checkSubjID(SubjID):
    return (SubjID in (IdList + todelete))


# return a dictionary contains facial asymmetry values between the original and mirrored face of input <SubjID>
def op1(SubjID):
    output1 = {}
    showOrder = ['ft', 'ex', 'en', 'al', 'sbal', 'ch']
    for i in showOrder:
        output1[i.upper()] = round(((res[(SubjID.upper(), i)][0] - res[(SubjID.upper(), i)][3]) ** 2 +
                                    (res[(SubjID.upper(), i)][1] - res[(SubjID.upper(), i)][4]) ** 2 +
                                    (res[(SubjID.upper(), i)][2] - res[(SubjID.upper(), i)][5]) ** 2) ** 0.5, 4)
    return output1


# return the Euclidean distance between two 3D landmarks of input <SubjID>
def op2(SubjID):
    SubjID = SubjID.upper()
    output2 = {}
    addShowOrder = {'EXEN': ['ex', 'en'], 'ENAL': ['en', 'al'],
                    'ALEX': ['al', 'ex'], 'FTSBAL': ['ft', 'sbal'],
                    'SBALCH': ['sbal', 'ch'], 'CHFT': ['ch', 'ft']}
    for key, value in addShowOrder.items():
        output2[key] = round((((res[(SubjID, value[0])][0] - res[(SubjID, value[1])][0]) ** 2) + (
                (res[(SubjID, value[0])][1] - res[(SubjID, value[1])][1]) ** 2) + (
                                      (res[(SubjID, value[0])][2] - res[(SubjID, value[1])][2]) ** 2)) ** 0.5, 4)
    return output2


# return a list contains face asymmetry of <SubjID> in each <landmark>
def preop3(SubjID):
    SubjID = SubjID.upper()
    preoutput3 = []
    showOrder = ['ft', 'ex', 'en', 'al', 'sbal', 'ch']
    for i in showOrder:
        element_preoutput3 = ((res[(SubjID, i)][0] - res[(SubjID, i)][3]) ** 2 +
                              (res[(SubjID, i)][1] - res[(SubjID, i)][4]) ** 2 +
                              (res[(SubjID, i)][2] - res[(SubjID, i)][5]) ** 2) ** 0.5
        preoutput3.append(element_preoutput3)
    return preoutput3


# return 5 tuple sequences will represent 5 lowest total facial asymmetries
def op3():
    output3 = {}
    for i in IdList:
        element = round(sum(preop3(i)), 4)
        output3[i] = element
    # sort and get 5 lowest facial asymmetries tuple
    output3 = list(output3.items())
    output3 = sorted(output3, key=lambda t: t[1])
    output3 = output3[0:5]
    return output3


# return cosine similarity between faces F1 and F2
def op4(SubjIDs):
    pre = [op2(SubjIDs[0]), op2(SubjIDs[1])]
    similarity = (pre[0]['EXEN']*pre[1]['EXEN'] + pre[0]['ENAL']*pre[1]['ENAL'] +
                  pre[0]['ALEX']*pre[1]['ALEX'] + pre[0]['FTSBAL']*pre[1]['FTSBAL'] +
                  pre[0]['SBALCH']*pre[1]['SBALCH'] + pre[0]['CHFT']*pre[1]['CHFT'])/(
                         (pre[0]['EXEN']) ** 2 + (pre[0]['ENAL']) ** 2 +
                         (pre[0]['ALEX']) ** 2 + (pre[0]['FTSBAL']) ** 2 +
                         (pre[0]['SBALCH']) ** 2 + (pre[0]['CHFT']) ** 2) ** 0.5/(
                         (pre[1]['EXEN']) ** 2 + (pre[1]['ENAL']) ** 2 +
                         (pre[1]['ALEX']) ** 2 + (pre[1]['FTSBAL']) ** 2 +
                         (pre[1]['SBALCH']) ** 2 + (pre[1]['CHFT']) ** 2) ** 0.5
    return round(similarity, 4)
