print("This Program will be find your prime number.") # Title msg.
while True:
    try:
        n = int(input("Enter a Number: "))
        # if n == 0 and n < 0:
        if n >= 0:
            break
        print("Can't Enter Nagative number.")
    except:
        print("Enter Just Number, Nothing else.")
prime_list = []

for i in range(2, n+1):
    prime_yeah = True
    for j in range(2, i):
        if i % j == 0:
            prime_yeah = False
            break
    if prime_yeah:
        prime_list.append(i)

if prime_list:
    print("Here is your all prime Number for", n, ":", ", ".join(map(str, prime_list)))
else:
    print("We can't found prime number for your input number.")


# The First Live test in frist exam-week from ostad.
