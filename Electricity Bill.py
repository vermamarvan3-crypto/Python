units=int(input("Enter the amount of electricity consumed in units: "))
if units<=50:
    bill=units*2.60
    surcharge=25
elif units>50 and units<=100:
    bill=50*2.60+(units-50)*3.25
    surcharge=35
elif units>100 and units<=200:
    bill=50*2.60+50*3.25+(units-100)*5.26
    surcharge=45
elif units>200:
   bill=50*2.60+50*3.25+100*5.26+(units-200)*8.45
   surcharge=75
total=bill+surcharge
print("The total electricity bill is: ",total,"$")
