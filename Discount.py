def CalculateDiscount(rate, quantity): 
    amount = rate * quantity

    if(amount >= 100000):
        discount = 20
    elif(amount>=50000 and amount<=99999):
       discount = 10
    else:
       discount = 5

    discountAmount = (amount*discount)/100
	
    netAmt = amount - discountAmount
	
    return discount, discountAmount, netAmt