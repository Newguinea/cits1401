"""
Author: 114514
Stuent No: 114514
date: 16/09/2022
"""
def main(csvfile, adultID, Option):
    global dataset
    #get the dataset
    dataset = read_csv(csvfile)
    #input validation adultID
    adultIdExist = False
    for i in range(0, len(dataset) -1 ):
        if(dataset[i][0] == adultID):
            adultIdExist = True
            pass
    if(adultIdExist==False):
        if Option == "stats":
            return [],[],[],[]
        elif Option == "FR":
            return 0,""
        else:
            return ""
    #input validation Option
    if Option == "stats":
        return stats(adultID)
    elif Option == "FR":
        return FR(adultID)
    else:
        return ""
    
def read_csv(fileName):
    #return a three dimension list with header
    #get the file name
    with open(fileName, 'r') as file:
        tmp = []
        text = file.read()
        for line in text.split('\n'):
            items = line.split(',')
            tmp.append(list(items))
        # get a list with list element
        head = tmp[0]
        tmp = tmp[1:]
        tmp = tmp[:-1]
        #check whether the head is normal
        normal_head=['ID', 'Expression', 'Distance', 'Gdis', 'Ldis']
        if(head==normal_head):
            data_cleaned = tmp
        else:
            # if fields in csv is ramdom, fix it
            index_head=[]
            #get the position of each fields
            for j in normal_head:
                    index_head.append(head.index(j))
            #innitialize a new list store the cleaned data
            data_cleaned=[[[], [], [], [], []]]
            for i in range(0,len(tmp)-1):
                data_cleaned.append([[], [], [], [], []])
            #put the data to data_cleaned
            for i in range(0, len(tmp)):
                for j in range(0, len(index_head)):
                    data_cleaned[i][index_head[j]] = tmp[i][j]
        #make sure the every fields in right data format
        for i in range(0,len(data_cleaned)):
            data_cleaned[i][2] = int(data_cleaned[i][2])
            data_cleaned[i][3] = float(data_cleaned[i][3])
            data_cleaned[i][4] = float(data_cleaned[i][4])
        return data_cleaned

def stats(adultID):
    #[minimum GDis, maximum GDis, minimumLDis, maximum LDis]
    #initialize variables
    Expression = ["Neutral", "Angry", "Disgust", "Happy"]
    OP1 = [[1000, 0, 1000, 0], [1000, 0, 1000, 0], [1000, 0, 1000, 0], [1000, 0, 1000, 0],
           [1000, 0, 1000, 0], [1000, 0, 1000, 0], [1000, 0, 1000, 0], [1000, 0, 1000, 0]]
    OP2 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    Gdis_SUM = [0, 0, 0, 0, 0, 0, 0, 0]
    Ldis_SUM = [0, 0, 0, 0, 0, 0, 0, 0]
    tmp_OP4_raw = []

    for i in range(0, len(dataset) -1 ):
        if(dataset[i][0] == adultID):
            for j in range(0,8):
                if(dataset[i][2] == (j + 1)):
                    #generate OP1
                    if (OP1[j][0] > dataset[i][3]):
                        OP1[j][0] = dataset[i][3]
                    if (OP1[j][1] < dataset[i][3]):
                        OP1[j][1] = dataset[i][3]
                    if (OP1[j][2] > dataset[i][4]):
                        OP1[j][2] = dataset[i][4]
                    if (OP1[j][3] < dataset[i][4]):
                        OP1[j][3] = dataset[i][4]
                    #generate OP2
                    for h in range(0,4):
                        if(Expression[h]==dataset[i][1]):
                            OP2[h][j] = dataset[i][3] - dataset[i][4]
                    #generate OP3 with out devide by 4
                    Gdis_SUM[j] += dataset[i][3]
                    #prepare for generate OP4
                    #get average of Ldis with out devide by 4
                    Ldis_SUM[j] += dataset[i][4]
            #a temporary list for OP4
            tmp_OP4_raw.append(dataset[i])
    #generate OP3
    OP3 = [ i / 4 for i in Gdis_SUM ]
    #generate OP4
    #get average value for this adultID
    Ldis_AVG = [ i / 4 for i in Ldis_SUM ]
    sum_square_error = [0, 0, 0, 0, 0, 0, 0, 0]
    for k in range(0,len(tmp_OP4_raw)):
        for l in range(0,8):
            if( l == tmp_OP4_raw[k][2] - 1 ):
                sum_square_error[l] += (tmp_OP4_raw[k][4] - Ldis_AVG[l])**2
    sum_avg_square_error = [ i / 4 for i in sum_square_error ]
    OP4 = [ i ** (1/2) for i in sum_avg_square_error ]
    #change OP1,OP2,OP3,OP4 to four decimal pleace
    OP1 = [[round(j,4) for j in OP1[i]] for i in range(len(OP1))]
    OP2 = [[round(j,4) for j in OP2[i]] for i in range(len(OP2))]
    OP3 = [round(i,4) for i in OP3]
    OP4 = [round(i,4) for i in OP4]
    return OP1,OP2,OP3,OP4

def FR(adultID):
    ###
    global data_FR
    ###
    #initialize variables and return variables
    ID = ""
    cossim = -1
    data_FR = []
    #generate a three dimension list, example
    #[[[["A002"],[0, 0, 0, 0, 0, 0, 0, 0]]......]
    for i in range(0, len(dataset) -1 ):
        if not any(dataset[i][0] in x for x in data_FR):
            data_FR.append([dataset[i][0],[0, 0, 0, 0, 0, 0, 0, 0]])
    #give value to data_FR, example
    #[['E001', [48.44795743, 104.1723994, 39.43651368, 66.47704324, 9.703645084, 7.454405978, 175.2890053, 153.6035146]], ......] 
    for i in range(0, len(dataset) - 1):
        for j in range(0, len(data_FR)):
            if (dataset[i][0] == data_FR[j][0]
                and dataset[i][1] == "Neutral"):
                data_FR[j][1][dataset[i][2] -1 ] = dataset[i][3]
    #add others three expression of this adultID to data_FR
    for i in range(3):
        data_FR.append([adultID,[0, 0, 0, 0, 0, 0, 0, 0]])
    for i in range(0, len(dataset) -1 ):
        if (dataset[i][0]==adultID):
            if(dataset[i][1]=="Angry"):
                data_FR[-1][1][dataset[i][2] -1 ] = dataset[i][3]
            if(dataset[i][1]=="Disgust"):
                data_FR[-2][1][dataset[i][2] -1 ] = dataset[i][3]
            if(dataset[i][1]=="Happy"):
                data_FR[-3][1][dataset[i][2] -1 ] = dataset[i][3]
    #caculate part for loop get the ID with the maximum cosine similarity and maximum cosine similarity value
    #get the value of import adultID Gdis
    for i in range(0, len(data_FR)):
        if(data_FR[i][0] == adultID):
            import_message = data_FR[i]
            data_FR.remove(data_FR[i])
            break
    #for loop get the output of ID and cossim
    for i in range(0, len(data_FR)):
        Numerator = 0
        Denominator_import = 0
        Denominator_change = 0
        #for loop get the biggest cossim and it's ID
        for j in range(0, 8):
            Numerator += data_FR[i][1][j]*import_message[1][j]
            Denominator_import += import_message[1][j]*import_message[1][j]
            Denominator_change += data_FR[i][1][j]*data_FR[i][1][j]
        cossim_new = Numerator/((Denominator_import**(1/2))*(Denominator_change**(1/2)))
        if(cossim_new>cossim):
            cossim = cossim_new
            ID = data_FR[i][0]
    #change cossim to four decimal pleace
    cossim = round(cossim,4)
    return ID, cossim