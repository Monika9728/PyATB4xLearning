# continue statement skips the current iteration of a loop
# and moves to next iteration


for number in range(0, 10):
    if number % 2 == 0:
        continue  # the number divided by 2 are skipped and the loop is being continued
    else:
        print(number)
# pass is a keyword that can be used in functions,class and objects
# however, # continue is a keyword that can't be used in functions,class and objects
