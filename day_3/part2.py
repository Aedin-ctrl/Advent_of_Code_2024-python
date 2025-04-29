f = open("input.txt")
imput_code = f.read()

# part 2

def main(imput_code):
    total = 0
    include = True
    for i in imput_code.split("\n"):
        for j in i.split("mul("):
            if "," in j and ")" in j:
                num1 = j[0:j.index(",")]
                num2 = j[j.index(",") + 1:j.index(")")]
                
                if num1.isdigit() and num2.isdigit() and include:
                    total +=  (int(num1) * int(num2))
            
            if "don't()" in j:
                include = False
            if "do()" in j:
                include = True
                
    return total

print("part 2", main(imput_code))