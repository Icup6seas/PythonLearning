

# bits = [False, True, False, False, True, False, False, True]
my_string = "HelloMyNameIsChris"


# bits = [b for b in bits if b == True]

# bits = [1 if b == True else 0 for b in bits]


# print(bits)

my_string = "".join([s if s.islower() else " " + s for s in my_string])[1:]

print(my_string)
