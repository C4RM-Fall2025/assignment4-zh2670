def get_bond_price_E(face,couponRate,m,yc):
  pvcfsum=0
  for t in range(1,m+1):
    if t==m:
      coupon=face*couponRate+face
    else:
      coupon=face*couponRate
    pvcf=coupon*(1+yc[t-1])**(-t)
    pvcfsum +=pvcf
  return pvcfsum