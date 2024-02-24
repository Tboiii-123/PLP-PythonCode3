
def calculate_discount(price,discount_price):
    if discount_price>=20:
        Appliedprice =price*(discount_price/100)
        finalprice =Appliedprice
        return finalprice
    else:
        return price






price =int(input("Insert your price pls:"))
discount_price=int(input("Insert your discount pls:"))                                
result =calculate_discount(price,discount_price)
if  result == price:
    print(discount_price,"% was lower for us to make a discount  so your original price is still ",price)
else:
    print("The final price after the discount is ",result)



                                
