def getBondPrice_E(face, couponRate, yc):
    m = len(yc) 
    bondPrice = 0
    
    for t, y in enumerate(yc, start=1):
        C = face * couponRate if t < m else face * (1 + couponRate)
        pv = 1 / ((1 + y) ** t) 
        pvcf = C * pv 
        bondPrice += pvcf 
    
    return bondPrice
