def double_list(items):
    if len(items)%2 == 0:
        items += items
    else:
        items.append(items[-1])
    return items