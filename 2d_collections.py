# 2D list of lists
num_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"],
]

# Other valid combinations of nested collections:
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#")]
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {"*", 0, "#"}]
tuple_of_lists = ([1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"])
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
tuple_of_sets = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {"*", 0, "#"})
set_of_tuples = {
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#"),
}

# Sets cannot contain mutable, unhashable elements such as lists or sets.
# A set of tuples is valid because tuples are hashable when their elements are.

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()