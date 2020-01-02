def build_bst(my_list):
    if len(my_list) == 0:
            return "No Child"

    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print("Middle index: {}".format(middle_idx))
    print("Middle value: {}".format(middle_value))

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
