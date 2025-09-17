def stripuneven(x: int): # Function to illustrate lambda usage
    numbers = list(range(0, x))
    even = []
    for num in numbers:
        try:
            if num % 2 == 0:
                even.append(num)
        except:
            print("No even numbers left.")
    print(even)
    return 0

stripuneven(29)

list(filter(lambda x: x%2 == 0, range(0, 29))) # Using lambda and filter to achieve the same result in one line.