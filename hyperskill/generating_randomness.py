from random import randint

binary_str_len = 100
binary_str_list = list()
third_binary_list = list()
first_three_randnum_list = list()
idx_list = list()
correct_symbol_counter = 0
virtual_money = 1000
binary_set = {"0", "1"}

triad = {"000", "001", "010", "011", "100", "101", "110", "111"}
triad_dict = dict.fromkeys(triad)

for i in triad_dict:
    triad_dict[i] = [0,0]

print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")
print("Print a random string containing 0 or 1:\n")

while len(binary_str_list) <= binary_str_len - 1:
    temp_str_list = list(input())
    temp_str_list = [int(x) for x in temp_str_list if x == '0' or x == '1']

    binary_str_list += temp_str_list

    if len(binary_str_list) <= binary_str_len:
        print(f"Current data length is {len(binary_str_list)}, {binary_str_len - len(binary_str_list)} symbols left")
        print("Print a random string containing 0 or 1:\n")

binary_str_list = [str(x) for x in binary_str_list]

print("Final data string:")
final_data_string = "".join(binary_str_list)
print(final_data_string)
print()


for i in range(len(final_data_string)):
    if i + 3 >= len(final_data_string):
        pass
    else:
        triad_key = final_data_string[i] + final_data_string[i + 1] + final_data_string[i + 2]
        triad_val = final_data_string[i + 3]
        # print(f"{triad_key}, {triad_val}")

        if int(triad_val) == 0:
            triad_dict[triad_key][0] += 1
        elif int(triad_val) == 1:
            triad_dict[triad_key][1] += 1
#print dictionary
# for i in sorted(triad_dict.keys()):
    # print(f"{i}: {triad_dict[i][0]},{triad_dict[i][1]}")

#####
# Now we start second stage of program where we create new string of 0's and 1's
# where the first 3 numbers are randomly chosen, then every number after that
# is calculated using the first string
#####

### In this portion we get the 2nd user binary string
print(f"You have ${virtual_money}.  Every time the system successfully predicts your next press, you lose $1.")
print(f"Otherwise, you earn $1.  Print \"enough\" to leave the game.  Let's go!")
print()
print("Print a random string containing 0 or 1:")

second_input = input()

while second_input != "enough":
    ##check if second_input string is binary or not
    second_input_set = set(second_input)
    if second_input_set != binary_set:
        print("\nPrint a random string containing 0 or 1:")
        second_input = input()
        print("hi")
        continue
     
    second_input_list = list(second_input)
    # print(second_input_list)
    ### In this portion, we generate 3rd binary string by prediction numbers based on 1st

    index = 0

    while len(third_binary_list) != (len(second_input_list) - 3):
        triad_str = "".join(second_input_list[index:index + 3])
        # print(triad_str)

        #now we check triplet binary value against dictionary, and predict next value
        # print(f"The triplet value {triad_str} has values {triad_dict[triad_str][0]} for 0, and {triad_dict[triad_str][1]} for 1.")

        #calculate probability of next number, and append it to the list
        if int(triad_dict[triad_str][0]) == int(triad_dict[triad_str][1]):
            third_binary_list.append(randint(0,1))
        elif int(triad_dict[triad_str][0]) > int(triad_dict[triad_str][1]):
            third_binary_list.append(0)
        elif int(triad_dict[triad_str][0]) < int(triad_dict[triad_str][1]):
            third_binary_list.append(1)
            # print(third_binary_list)
        index += 1
        # print(f"third_binary_list is: {third_binary_list}")
    for x in range(0,3):
        first_three_randnum_list.append(randint(0,1))
    # print(f"the random 3 numbers to be included at beginning of prediction string are {first_three_randnum_list}")
    # print(f"third binary list is {third_binary_list}")
    third_binary_list = first_three_randnum_list + third_binary_list
    prediction_result = "".join([str(x) for x in third_binary_list])
    print("prediction:")
    print(prediction_result.strip())
    # print(third_binary_list)



    ##In this portion, we check the accuracy of second user-input string against
    # 3rd string which predicted future values
    second_input_list = [int(x) for x in second_input_list]
    for i in range(len(third_binary_list) - 3):
        if second_input_list[i + 3] == third_binary_list[i + 3]:
            correct_symbol_counter += 1
        
    virtual_money = virtual_money + ((len(second_input_list) - 3) - correct_symbol_counter) - correct_symbol_counter
    print()
    print(f"Computer guessed right {correct_symbol_counter} out of {len(second_input_list) - 3} symbols ({round((correct_symbol_counter / (len(second_input_list) - 3) * 100), 2)} %)")
    print(f"Your capital is now ${virtual_money}")
    # print(len(second_input_list))
    # print(len(third_binary_list))
    first_three_randnum_list.clear()
    third_binary_list.clear()
    correct_symbol_counter = 0
    print()
    print("Print a random string containing 0 or 1:")
    second_input = input()
    
print("Game over!")