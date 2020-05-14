def checkout():
    total=0
    count=0
    moreitems=True
    while(moreitems):
        n=int(input("Enter price of your items: "))
        if(n!=0):
            total=total+n
            count=count+1
            print("Subtotal: $", total)
    #return total
        else:
            moreitems=False
    return total
t=checkout()
print("Total Price $",t)
