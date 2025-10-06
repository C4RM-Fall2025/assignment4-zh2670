
def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0

    for t, y in zip(times, yc):
        C = face * couponRate if t < max(times) else face * (1 + couponRate) 
        PV = 1 / ((1 + y) ** t) 
        PVCF = C * PV 
        bondPrice += PVCF 

    return bondPrice
