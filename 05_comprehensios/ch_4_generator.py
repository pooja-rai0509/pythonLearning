#used for saving memory
#list - makes entire list in memory
#generator - its like a stream

daily_sales = [5, 10, 12, 7, 3 ,9, 15, 8]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)

nums = (num * 2 for num in range(5))
print(nums)