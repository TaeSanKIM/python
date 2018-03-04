from MulLayer import *
from AddLayer import *

apple = 100
apple_num = 2

orange = 150
orrange_num = 3

tax = 1.1

mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_total_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orrange_num)
total_price = add_total_layer.forward(apple_price, orange_price)
price = mul_tax_layer.forward(total_price, tax)

print(tax)

#backward
dout = 1

dtotal_price, dtax = mul_tax_layer.backward(dout)
dapple_price, dorange_price = add_total_layer.backward(dtotal_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
doragne, dorange_num = mul_orange_layer.backward(dorange_price)

print("Apple:", dapple, dapple_num)
print("Orange:", doragne, dorange_num)
print("Tax:", dtax)
