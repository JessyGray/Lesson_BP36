def product_sum(price_unit:float, units: float, name_of_product: str)->tuple[float,str]:
    return price_unit*units, name_of_product


res1 = product_sum(7.10, 2, "milk")
res2 = product_sum(6.9, 1, "bread")
res3 = product_sum(120.5, 1.5, "meat")
print(res1) #(14.2, 'milk')
print(res2) #(6.9, 'bread')
print(res3) #(180.75, 'meat')
print(f"your bought {res1[1]}, {res2[1]}, {res3[1]}, "
      f"total sum is {(res1[0]+res2[0]+res3[0]):.2f} NIS")