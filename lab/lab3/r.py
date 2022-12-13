currentValue = [120000,450000,755000,1800000,10300000]
year = [2,5,15]
growRate = [0.02,0.04,0.06]

print('{0:10} {1:10} {2:10} {3:10}'.format("current value", "year", "growth rate", "final value"))
for i in growRate:
    for j in year:
        for h in currentValue:
            print('{0:10} {1:10} {2:10} {3:10}'.format(h, j, i, (h*(1+i)**j)))