def prime_checker(number):
    is_prime=True
    for i in range(2,number-1):
        if(number % i == 0):
            is_prime=False

    if(is_prime):
        print(number,"is a prime number")
    else:
        print(number,"is not a prime number")