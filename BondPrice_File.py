def getBondPrice(y, face, couponRate, m, ppy=1):
    i = 0
    pvcf = 0
    y1 = y/ppy
    m1 = m*ppy
    for i in range(m1):
        i = i+1
        pvcf = ((1+y1)**-i)*face*couponRate/ppy + pvcf     
        
    bondPrice = pvcf + face*(1+y1)**-m1
    return(bondPrice)