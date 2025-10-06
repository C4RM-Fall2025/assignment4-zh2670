
def getBondDuration(y, face, couponRate, m, ppy = 1):
    y1 = y/ppy
    m1 = m*ppy
    i = 0
    pvcf = 0
    pvcfd = 0 
    for i in range(m1):
        i = i+1
        pvcf = pvcf+ (1+y1)**-i*face*couponRate/ppy
        pvcfd = pvcfd+i*(1+y1)**-i*face*couponRate/ppy
    totalpvcf = pvcf + (1+y1)**-m1*face
    totalpvcfd = pvcfd + (1+y1)**-m1*face*m1
    bondDuration = totalpvcfd/totalpvcf
    return(bondDuration)
