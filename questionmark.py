# read in input

# determine if there are 3 question marks between every pair of numbers that add up to 10
# slice the string, check for numbers, store the position of the numbers that add up to 10, check the string between
# the positions for question marks and count them
# if the number is 3, print true, else print false

input = "arrb6???4xxbl5???eee5"

pos = []
num2 = 0
for position, letter in enumerate(input):
    try:
        letter = int(letter)
        num1 = int(letter)
        sum = num1 + num2
        pos.append(position)
        num2 = num1
    except ValueError:
        pass

# interesting use of zip to get the slices from the positions in the list
# first tried [input[x:y+1] for x,y in pos] but that threw an error
# idea behind this is to create two lists, the first is the original list without the last element, the second is the
# original list without the first element
# zipping these two lists together, we get a list of tuples that contain element 1+2, 2+3, 3+4 and so on
print(pos)
print(pos[:-1], pos[1:])
print(list(zip(pos[:-1], pos[1:])))
slices = [input[x:y+1] for x,y in zip(pos[:-1], pos[1:])]

result = []
for slice in slices:
    if int(slice[0]) + int(slice[-1]) == 10:
 #       print(slice)
        questionmarks = slice.count("?")
        if questionmarks == 3:
            result.append("true")
        else:
            result.append("false")
    else:
        continue

if "false" in result or result == None:
    print("false")
else:
    print("true")