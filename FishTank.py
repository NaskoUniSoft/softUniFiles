long = int(input())
wide = int(input())
height = int(input())
percent_busy = float(input())

volume_fish_tank = long * wide * height
volume_liters = volume_fish_tank / 1000

converted_percent_busy = percent_busy / 100
liters_needed = volume_liters * (1 - converted_percent_busy)
print(liters_needed)