from datetime import datetime
 
name=input("enter your name:")

list='''
Rice    Rs 2/kg
sugar   Rs 35/kg
salt    Rs 5/kg
oil     Rs 150/liter
paneer  Rs 110/kg
maggi   Rs 50/kg
boost   Rs 190/each
colgate Rs 45/each'''

#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rats for items
items={'rice':2,'sugar':35,'salt':5,'oil':150,'pannir':110,'maggi':50,'boost':190,'colgate':45}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(price)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterd item is not available")
    else:
        print("you enterd wrong numkber")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
           print(25*"=","subbu supermarket",25*"=") 
           print(28*" ","kodur")  
           print("Name:",name,30*" ","Date:",datetime.now())
           print(75*"=")  
           print("sno",5*" ",'items',9*" ",'Quantity',5*" ",'price')   
           for i in range(len(pricelist)):
              print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
           print(75*"-")
           print(50*" ",'TotalAmount:','Rs',totalprice)
           print("gst amount",40*" ",'Rs',gst) 
           print(75*"-") 
           print(50*" ",'FinalAmount:','Rs',finalamount)
           print(25*" ","Thanks for visiting")
           print(75*"-")