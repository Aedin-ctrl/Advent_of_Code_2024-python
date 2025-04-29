f = open("input.txt")
imput_code = f.read()

# part 2

def check(list):
    ...
    
def main(imput_code):
    total = 0
    
    for i in imput_code.split("\n"):
        lst = i.split(" ")
        
        difs = []
        
        for i in range(len(lst) - 1):
            diff = int(lst[i+1]) - int(lst[i])
            difs.append(diff)
            
        if all((1 <= num <= 3) or (-3 <= num <= -1) for num in difs):
            if all(num > 0 for num in difs) or all(num < 0 for num in difs):
                total += 1
            
    return total

print("part 2", main(imput_code))