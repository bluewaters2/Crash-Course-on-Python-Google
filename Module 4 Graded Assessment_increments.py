def increments(start, end):
    l = []
    start += 2
    end += 2
    while start<=end:
        l.append(start)
        start += 1
    return l # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
