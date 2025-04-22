def computepay(h,r):
    basicpay = h*r
    totalpay = basicpay
    overtime = h-40
    if overtime > 0 :
        totalpay = basicpay + (overtime*r/2)
    return (totalpay)
    


hrs = raw_input("Enter Hours:")
h = float(hrs)
rte = raw_input("Rate per hour:")
r = float(rte)
print computepay(h,r)
