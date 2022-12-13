def list_sorting(lst1,lst2):
    list1 = lst1.copy()
    list2 = lst2.copy()
    list1, list2 = zip(*sorted(zip(list1, list2), key=(lambda x:[-x[1],x[0]]), reverse = False))
    list1 = list(list1)
    list2 = list(list2)
    return list1, list2