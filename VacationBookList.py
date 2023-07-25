pages_in_book = int(input())
pages_read_per_hour = int(input())
day_for_reading = int(input())

hours_for_book = pages_in_book // pages_read_per_hour
hours_per_day = hours_for_book // day_for_reading
print(hours_per_day)