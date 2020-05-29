def OneAway(string_1, string_2):
    chartable = {}
    counter = 0

    diff = abs(len(string_1)-len(string_2))
    if diff != 0:
        counter += diff
    
    for i in range(len(string_1)):
        if chartable.get(string_1[i])==None:
            chartable[string_1[i]] = 1
        else:
            chartable[i] += 1
    
    for i in range(len(string_2)):
        if chartable.get(string_2[i]) == None:
            counter += 1
    
    if counter > 1:
        print(string_1 + ", " + string_2 + " - > False")
        return
    else:
        print(string_1 + ", " + string_2 + " - > True")
        return


str1 = ["pale", "pales", "pale", "pale"]
str2 = ["ple", "pale", "bale", "bake"]

for i in range(len(str1)):
    OneAway(str1[i], str2[i])

