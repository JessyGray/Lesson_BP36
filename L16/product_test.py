from lesson16_class.Product import Product

p1 = Product("pr1", 9.9, "u1","1001",True)
p2 = Product("pr2", 19.9, "u2","1002",False)
p3 = Product("pr3", 29.9, "u3","1003",True)
p4 = Product("pr4", 119.9, "u4","1004",False)

print(p1)
print(p1.get_name())
# print(p1.__name)
p1.set_name("product1")
print(p1)
print(p1.get_price())
p1.set_price(-100)
print(p1.get_price())
products = [p1,p2,p3,p4]

def inc_10_per(products:list[Product]):
    for p in products:
        p.set_price(round(p.get_price()*1.1,2))


print(products)
inc_10_per(products)
print(products)

"""
add checks getters setters in any two classes from hw15
"""