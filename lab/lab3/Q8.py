def buy_goods(cost, savings):
    if cost/savings < 0.05:
        return True
    else:
        return False