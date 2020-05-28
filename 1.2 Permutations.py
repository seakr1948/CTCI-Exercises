def check_permutation(string_1, string_2):
    chartable = {}
    for index in range(len(string_1)):
        if chartable.get(string_1[index]) == None:
            chartable[string_1[index]]=1
        else:
            chartable[string_1[index]] += 1
            
    for index in range(len(string_2)):
        if chartable.get(string_2[index]) == None:
            chartable[string_1[index]] = 1
        else:
            chartable[string_2[index]] -= 1

    for keys in chartable:
        if chartable[keys] != 0:
            print("Not a permutation")
            return
        print("Is a permutation")
        return

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

check_permutation(str1, str2)
