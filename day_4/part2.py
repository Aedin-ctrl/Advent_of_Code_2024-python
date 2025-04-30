f = open("input.txt")
txt = f.read()

# part 2

def main(txt):
    total = 0
    txt = txt.splitlines()
    
    for row_dex, row in enumerate(txt):
        for col_dex, char in enumerate(row):
            check_string = []
            if char == "A" and row_dex > 0 and row_dex < len(txt) - 1 and col_dex > 0 and col_dex < len(txt) - 1:
                
                if txt[row_dex - 1][col_dex - 1] == "M" and txt[row_dex + 1][col_dex + 1] == "S":
                    if txt[row_dex + 1][col_dex - 1] == "M" and txt[row_dex - 1][col_dex + 1] == "S":
                        total += 1
                    elif txt[row_dex + 1][col_dex - 1] == "S" and txt[row_dex - 1][col_dex + 1] == "M":
                        total += 1
                
                elif txt[row_dex - 1][col_dex - 1] == "S" and txt[row_dex + 1][col_dex + 1] == "M":
                    if txt[row_dex + 1][col_dex - 1] == "M" and txt[row_dex - 1][col_dex + 1] == "S":
                        total += 1
                    elif txt[row_dex + 1][col_dex - 1] == "S" and txt[row_dex - 1][col_dex + 1] == "M":
                        total += 1
                
            # Honestly idk wtf im doing
    return total

print("part 2", main(txt)) 