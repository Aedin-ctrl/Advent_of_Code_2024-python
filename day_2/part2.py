f = open("input.txt")
imput_code = f.read()

# part 2

def check(lst):
    difs = []
    
    for i in range(len(lst) - 1):
        diff = int(lst[i+1]) - int(lst[i])
        difs.append(diff)
        
    if all((1 <= num <= 3) or (-3 <= num <= -1) for num in difs):
        if all(num > 0 for num in difs) or all(num < 0 for num in difs):
            return True
    
def main(imput_code):
    total = 0
    
    for line in imput_code.strip().split("\n"):
        lst = line.strip().split(" ")
        
        if check(lst):
            total += 1
        else:
            for i in range(len(lst)):
                new_list = lst[:i] + lst[i+1:]
                if check(new_list):
                    total += 1
                    break 
        
    return total

print("part 2", main(imput_code))