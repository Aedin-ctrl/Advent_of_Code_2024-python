f = open("input.txt")
imput_code = f.read()

# part 1 

def main(imput_code):
    word = "XMAS"
    drow = "SAMX"
    
    total = 0
    imput_code = imput_code.splitlines()
    
    for row_dex, row in enumerate(imput_code):
        for col_dex, col in enumerate(row):
            check_string = []
            if col == word[0] or col == drow[0]:
                # check right
                if col_dex <= len(row)-len(word): 
                    check_string = row[col_dex:col_dex+len(word)]
                    if check_string == word or check_string == drow:
                        total += 1
                        
                # check down
                if row_dex <= len(imput_code)-len(word): 
                    check_string = "".join(imput_code[row_dex + i][col_dex] for i in range(len(word)))
                    if check_string == word or check_string == drow:
                        total += 1
                
                # Check diagonal down-right
                if row_dex <= len(imput_code) - len(word) and col_dex <= len(row) - len(word):
                    check_string = "".join(imput_code[row_dex + i][col_dex + i] for i in range(len(word)))
                    if check_string == word or check_string == drow:
                        total += 1

                # Check diagonal down-left
                if row_dex <= len(imput_code) - len(word) and col_dex >= len(word) - 1:
                    check_string = "".join(imput_code[row_dex + i][col_dex - i] for i in range(len(word)))
                    if check_string == word or check_string == drow:
                        total += 1
    return total

print("part 1", main(imput_code)) 