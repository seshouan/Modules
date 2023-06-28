# set flag to continue or exit the number chaining
continue_flag = True
start =0
end = 0

# while the flag is True, continue the chaining
while continue_flag:
    # reset the starting point and output for chaining
    start += end
    output = ""

    # capture the upper limit to chain to
    end = int(input("How many numbers?"))

    # perform the chaining
    for num in range (start, start+end):
        output += "-" + str(num)
    
    # cleanup the prepended chain link
    output = output[1:]

    # print the chained numbers
    print(output)

    # determine whether to continue or not
    continue_choice = input("Would you like to continue? (y/n) ")
    if continue_choice.lower() == "n":
        continue_flag = False
    elif continue_choice.lower() != "y":
        print("Improper response; I presume you want to stop")
        continue_flag = False
