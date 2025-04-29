f = open("input.txt")
imput_code = f.read()


# part 1
def main(imput_code):
    total = 0
    list1 = []
    list2 = []
    
    for i in imput_code.split("\n"):
        list1.append(i.split("   ")[0])
        list2.append(i.split("   ")[1])
        
    list1.sort()
    list2.sort()   
    
    for i, j in enumerate(list1):
        total += abs(int(j) - int(list2[i]))
    
    return total
                
print("part 1", main(imput_code)) 