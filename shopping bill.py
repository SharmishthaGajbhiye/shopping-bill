def calculateElectronicsGST(a, b):
    total = a + b
    return total + (total * 18 / 100)
def calculateFashionGST(c, d):
    total = c + d
    return total + (total * 13 / 100)
def calculateFoodGST(e):
    return e + (e * 7 / 100)
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount
    return final_amount
a = 100
b = 100
c = 100
d = 100
e = 100
electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)
print("Electronics after GST: Rs.", format(electronics, ".2f"))
print("Fashion after GST: Rs.", format(fashion, ".2f"))
print("Food after GST: Rs.", format(food, ".2f"))
print("Total after GST: Rs.", format(total, ".2f"))
print("Discount (20%): Rs.", format(discount, ".2f"))
print("Final payable amount: Rs.", format(final_amount, ".2f"))