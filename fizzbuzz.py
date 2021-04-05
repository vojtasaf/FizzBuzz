for i in range(1, 101):
    fizzOrBuzz = False
    if i % 3 == 0:
        print("Fizz", end="")
        fizzOrBuzz = True
    if i % 5 == 0:
        print("Buzz", end="")
        fizzOrBuzz = True
    if (not fizzOrBuzz):
        print(i, end="")
    print()