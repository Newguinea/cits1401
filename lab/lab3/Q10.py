def balance_list(items):
    if len(items)%2 == 1:
        items.append(items[len(items)-1])
    return items