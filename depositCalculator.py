deposit = float(input())
term = int(input())
year_add_percent = float(input())

sum_total = deposit + term * ((deposit * year_add_percent / 100) / 12)
print(sum_total)

