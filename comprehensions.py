# gewone manier;
prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

dbl_prizes = [ prize*2 for prize in prizes]
print(dbl_prizes)

nums = [1,2,3,4,5,6,7,8,9,10]
sqared_even_nums = []
for num in nums:
    if (num ** 2) % 2 == 0:
        sqared_even_nums.append(num ** 2)

print(sqared_even_nums)

sqared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]

print(sqared_even_nums)
