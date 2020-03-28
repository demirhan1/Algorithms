# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print("Items: {}, {}".format(first_loop_item, second_loop_item))


Quad_Example([1, 2, 3, 4])

% time