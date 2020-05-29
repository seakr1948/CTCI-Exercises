def check_permutation(string):
    chartable = {}
    # Counts all characters and puts them in a hashtable
    print(string)
    for index in range(len(string)):
        if chartable.get(string[index]) == None:
            chartable[string[index]]=1
        else:
            chartable[string[index]] += 1

    # Identifies which strings can be palindromes based on string 
    # length and char counts
    if len(string) % 2 == 0:

        for keys in chartable:
            if (chartable[keys] % 2) != 0:
                print("Is not a Palindrome")
                return  
        print("Is A Palindrome")

    else: 
        odd_counter = 0
        for keys in chartable:
            if (chartable[keys] % 2) != 0:
                odd_counter += 1
        if odd_counter > 1:
            print("Not a Palindrome")
        else:
            print("Is a Palindrome")
    print("")

stringlist = ["amanaplanacanalpanama","strawwarts", "atoyotasatoyota",
           "man", "Chandooorgmakesyouawesome", "dammitimmad", "topspot",
            "borroworrob", "godsaveevasdog", "neverafoottoofareven"]

for test in stringlist:
    check_permutation(test)
