# Write another program that prompts for a list of numbers as above and at the
# end prints out both the maximum and minimum of the numbers instead of the average.

max_value = None
min_value = None

while True:

    s_num = input("Enter a number: ", )

    if s_num == "done":
        print("max: ", max_value)
        print("min: ", min_value)
        break

    try:
        i_num = int(s_num)
    except:
        print("error, please enter a valid number")
        continue

    if max_value == None or max_value < i_num:
        max_value = i_num

    if min_value == None or min_value > i_num:
        min_value = i_num
