
def rotate_image(image = []):
    M = len(image)
    N = len(image[0])
    new_image = [['' for i in range(M)] for j in range(N)]

    for i in range(N):
        start = 0
        for j in range(M-1,-1,-1):
            new_image[i][start] = image[j][i]
            start += 1
    print_2d_array(new_image)

def print_2d_array(array = []):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print("")
    print("\n")

image = [["-","-","^","-","-"],
         ["-","-","|","-","-"],
         ["-","-","|","-","-"],
         ["-","-","|","-","-"],
         ]

print_2d_array(image)

rotate_image(image)