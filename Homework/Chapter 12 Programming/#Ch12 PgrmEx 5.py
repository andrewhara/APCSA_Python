#Ch12 PgrmEx 5

def main():
    lst = []
    num_elements = int(input("How many elements do you want in the list?"))
    total = 0
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}:"))
        lst.append(value)
        total += sum(lst)
    print(total)
    
def sum(list):
    sum_of_rest = 0
    if len(list) == 1:
        return list[0]
    else:
        sum_of_rest += sum(list[1:]) #recursive step
    return sum_of_rest
        
main()
