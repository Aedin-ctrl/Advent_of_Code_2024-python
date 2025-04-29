f = open("input.txt")
imput_code = f.read()


def main(imput_code):
    total = 0
    list1 = []
    list2 = []
    
    for i in imput_code.split("\n"):
        list1.append(i.split("   ")[0])
        list2.append(i.split("   ")[1])
    
    for i in list1:
        total += int(i) * (list2.count(i))
    
    return total
         
print("part 2", main(imput_code))