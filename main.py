limit = 1000
cont = 1

while cont <= limit:
    if cont % 3 == 0 and cont % 5 == 0:
        print("Fizzbuzz")
    elif cont % 3 == 0:
         print("Fizz")
    elif cont % 5 == 0:
         print("Buzz")
    else:
         print(cont)
    cont = cont + 1

