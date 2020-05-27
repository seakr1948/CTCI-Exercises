def unique_string(string):
    unique_char = {}
    for index in range(len(string)):
        if unique_char.get(string[index]) == None: # base case If there is nothing in hash table, put it in
            unique_char[string[index]] = 1
        else:
            print("Not Unique")
            return 
    print("Unique")
    return 

test_1 = "abc"
test_2 = "test"

unique_string(test_1)
unique_string(test_2)






