year_tax = int(input())

basket_shoes = year_tax - year_tax * 40/100
basket_shirt = basket_shoes - basket_shoes * 20/100
basket_ball = 25/100 * basket_shirt
basket_accessories = 1/5 * basket_ball
total_price = year_tax + basket_accessories + basket_ball + basket_shoes + basket_shirt

print(total_price)