a=[1,3,2]
max_num=a[0]

for i in a:
    if i>max_num:
        max_num=i
print("maximum elemets is",max_num)


# Start: max_element = 10

# First element → i = 10
# 10 > 10? → No → max stays 10

# Second element → i = 45
# 45 > 10? → Yes → max becomes 45

# Third element → i = 2
# 2 > 45? → No → max stays 45

# Fourth element → i = 99
# 99 > 45? → Yes → max becomes 99

# Fifth element → i = 56
# 56 > 99? → No → max stays 99

# Sixth element → i = 78
# 78 > 99? → No → max stays 99
