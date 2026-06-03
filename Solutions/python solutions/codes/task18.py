def first_even():
    limit = 10
    if limit > 0:
        for i in range(limit):
            if i % 2 == 0:
                print("First even number:", i)
                break
    else:
        print("Invalid range")
first_even()