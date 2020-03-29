#Quadratic Example
# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print("Items: {}, {}".format(first_loop_item, second_loop_item))


Quad_Example([1, 2, 3, 4])

% time

# Items: 1, 1
# Items: 1, 2
# Items: 1, 3
# Items: 1, 4
# Items: 2, 1
# Items: 2, 2
# Items: 2, 3
# Items: 2, 4
# Items: 3, 1
# Items: 3, 2
# Items: 3, 3
# Items: 3, 4
# Items: 4, 1
# Items: 4, 2
# Items: 4, 3
# Items: 4, 4
# CPU times: user 3 µs, sys: 0 ns, total: 3 µs
# Wall time: 6.2 µs

#Log Linear Example
# O(nlogn)


def Log_Linear_Example(our_list):
    if len(our_list) < 2:
        return our_list

    else:
        mid = len(our_list) // 2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k] = left[i]
                i += 1
            else:
                our_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            our_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            our_list[k] = right[j]
            j += 1
            k += 1

        return our_list


Log_Linear_Example([56, 23, 11, 90, 65, 4, 35, 65, 84, 12, 4, 0])

% time

#Linear Example

# O(n)

def Linear_Example(our_list):
    for item in our_list:
        print ("Item: {}".format(item))

Linear_Example([1,2,3,4])

%time

#Logarithmic Example

# O(logn)

def Logarithmic_Example(number):
    if number == 0:
        return 0

    elif number == 1:
        return 1

    else:
        return Logarithmic_Example(number - 1) + Logarithmic_Example(number - 2)


Logarithmic_Example(29)

% time

#Constant Example

# O(1)

def Constant_Example(our_list):
    return our_list.pop()

Constant_Example([1,2,3,4])

%time

