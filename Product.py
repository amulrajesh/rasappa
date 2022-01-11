class Product: 

    def GetProduct(self):
        self._id = input("Enter id : ")
        self._name = input("Enter name : ")
        self._rate = int(input("Enter rate : "))
        self._stock = int(input("Enter Stock : "))

    def PutProduct(self):
        print(self._id, self._name, self._rate, self._stock)
        
    def SearchById(self, id):
        if self._id == id:
            return True
        else:
            return False
            
    def SearchByName(self, name):
        if self._name == name:
            return True
        else:
            return False

    def Sale(self):
            print("Sale.......")
            print("Quantity of Product present in stock is:", self.__stock)
            q=int(input("input enter qty:"))
            if(self.__stock>=q):
             amt=q*self.__rate
             print("Amount:",amt)

             self.__stock -= q
            else:
                print("Less Stock")

        def Purchase(self):
            print("Purchase....")
            q = int(input("enter quantity of particular product you want to purchase:"))
            self.__stock += q


    n = int(input("Enter Total products?"))
    L = []
    for i in range(n):
        P = Product()
        P.GetProduct()
        L.append(P)
    while True:
        print("Main Menu\n1]Show All Products\n2]Search By Id\n3]Search By Name\n4]Sale\n5]Purchase\n6]Exit")
        ch = int(input("Enter Your Choice?"))
        if ch == 1:
            for c in L:
                c.PutProduct()

        elif ch == 2:
            id = input("Enter Product Id U want to Search? ")
            found = False
            for c in L:
                found = c.SearchById(id)
                if found:
                    c.PutProduct()
                    break
            if not found:
                print("Record Not Found..")

        elif ch == 3:
            name = input("Enter Product Name?")
            count = 0
            for c in L:
                found = c.SearchByName(name)
                if found:
                    c.PutProduct()
                    count += 1

            if count == 0:
                print("Product Not Found..")
            else:
                print("Product Found:", count)

        elif ch == 4:
            q = input("enter product name:")
            count = 0
            for c in L:
                found = c.SearchByName(q)
                if found:
                    c.Sale()
                    c.PutProduct()
            if count == 0:
                print("No product!")
        elif ch == 5:
            name = input("enter product name you want to purchase:")
            count = 0
            for c in L:
                found = c.SearchByName(name)
                if found:
                    c.Purchase()
                    c.PutProduct()
                    count += 1
        elif ch == 6:
            break
        else:
            print("Invalid Choice")
            

class Discount:
def CalculateDiscount: 
    rate = float(input("Enter Rate : "))
    quantity = float(input("Enter Quantity : "))

    amount = rate*quantity
    print("Amount = ",amount)

    if(amount >= 100000):
        discount = 20
    elif(amount>=50000 and amount<=99999):
       discount = 10
    else:
       discount = 5

    discountAmount = (amount*discount)/100
    netAmt = amount - discountAmount

    print("Discount = %d%% and Discount Amount = %.2f"%(discount,discountAmount))

    print("Net Amount = ",netAmt)