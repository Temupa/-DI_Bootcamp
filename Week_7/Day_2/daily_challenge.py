matrix = [
    "7ir",
    "Tsi",
    "h%x",
    "i&$",
    "sM*",
    "$a*",
    "*t%",
    "^&!",
    ]

    
def decode_matrix(matrix):
    code = ""
    temp = []
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if matrix[x][y].isalpha():
                if len(temp)>1:
                    code += " " + matrix[x][y]
                    temp.clear()
                else:
                    code += matrix[x][y]
            else:
                temp.append(matrix[x][y])                     
    print(code)
                
decode_matrix(matrix)