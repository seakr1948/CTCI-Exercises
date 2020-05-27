def URLify(string):
    output = ""
    for i in range(len(string)):
        if string[i] == ' ':
            output = output + "%20"
        else:
            output = output + string[i]   
    #output = string.replace(" ","%20")
    return output

string = "Mr John Smith"
output = URLify(string)
print(output)

