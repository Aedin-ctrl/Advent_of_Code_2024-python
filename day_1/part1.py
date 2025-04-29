with open("input.txt", "r") as file:
    input_code = file.read().strip()

lines = input_code.splitlines()
print(lines)



# part 1
def part1(imput_code):
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
# part 2
def part2(imput_code):
    total = 0
    list1 = []
    list2 = []
    
    for i in imput_code.split("\n"):
        list1.append(i.split("   ")[0])
        list2.append(i.split("   ")[1])
    
    for i in list1:
        total += int(i) * (list2.count(i))
    
    return total
        
                
print("part 1", part1(imput_code)) 
print("part 2", part2(imput_code))