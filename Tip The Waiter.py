def totalcalc(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print("Total Bill Is:",total)
totalcalc(670,10)
