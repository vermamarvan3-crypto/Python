profit=0
cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
profit=sp-cp
loss=cp-sp
if profit>0:
    print("The profit is",profit,"$")
else:    print("The loss is",loss,"$")
