chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken_menu = chicken_menu * count_chicken_menu
price_fish_menu = fish_menu * count_fish_menu
price_vegan_menu = vegan_menu * count_vegan_menu

total_sum = price_vegan_menu + price_fish_menu + price_chicken_menu
price_desert = total_sum * 20/100
price_delivery = 2.50
total_sum = total_sum + price_desert + price_delivery
print(total_sum)