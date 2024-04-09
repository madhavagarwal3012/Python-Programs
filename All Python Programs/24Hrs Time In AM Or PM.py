#Make A Program To Find AM Or PM Of a 24 Hours Time, Entered By User At Runtime

t=float(input("enter t : "))        #EXAMPLE FOR USER IN ENTERING TIME : 00.00
if t<12:
    print("AM")
elif t<24:
    print("PM")                           
elif t==00:
    print("AM")
else:
    print("enter correct time format")
