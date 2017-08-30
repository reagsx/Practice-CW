
print("Please provide the following details:")
name = input("Enter your name: ")
department = input("Enter your department: ")
college = input("enter your department: ")

print("-----------------------")
print("Name       : " + name)
print("Department : " + department)
print("College    : " + college)

def len_int(x):
    try:
        val = int(x)
    except ValueError:
        print("Please input a number")
    else:
        print(len(str(abs(val))))

def str_cmp(x, y):
    if x.lower() == y.lower():
        return True
    else:
        return False

def str_anagram(x, y):
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def six_by_seven(x):
    if x % 42 == 0:
        return 'Universe'
    elif x % 6 == 0:
        return 'Good'
    elif x % 7 == 0:
        return 'Food'
    else:
        return 'oops'

for i in range(1,101):
    print(str(i) + " : " + six_by_seven(i))


for i in range(1,1001):
    num_bin = bin(i)[2:]
    if str(i)[::-1] == str(i) and num_bin[::-1] == num_bin:
        print(str(i) + " " + str(num_bin))
        
        
def product(x):
    v = 1
    for i in x:
        v *= i
    return v

def nth_lowest(x, y=2):
    return sorted(x)[y-1]





