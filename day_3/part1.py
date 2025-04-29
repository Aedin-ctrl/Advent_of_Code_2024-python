f = open("input.txt")
imput_code = f.read()

# part 1 
   
def main(imput_code):
    total = 0
    
    for i in imput_code.split("\n"):
        for j in i.split("mul("):
            if "," in j and ")" in j:
                num1 = j[0:j.index(",")]
                num2 = j[j.index(",") + 1:j.index(")")]
                
                if num1.isdigit() and num2.isdigit():
                    total +=  (int(num1) * int(num2))
                
    return total

print("part 1", main(imput_code)) 