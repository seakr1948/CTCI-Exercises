def string_compression(string):
    output = ""
    count = 0
    current_letter = string[0]
    for i in range(len(string)):
        if string[i] == current_letter:
            count += 1
        else:
            output = output + current_letter + str(count)
            count = 1
            current_letter = string[i]

    output = output + current_letter + str(count)

    if len(output)<len(string):
        return output
    else:
        return string

string = "aaabbccccccaaa"

output = string_compression(string)
print(output)