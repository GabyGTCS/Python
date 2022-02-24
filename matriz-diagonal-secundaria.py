grelha=[["-","-","H","-"],["-","H","-","H"],["-","-","-","-"],["-","-","-","-"]]
for linha in range len(grelha):
    print ("%s " % grelha [linha][((len(grelha-1))-linha)], end="")