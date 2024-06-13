""" # 1. Exercise: List Manipulation
Objective: Create a function merge_and_sort_lists(list1, list2) that takes two
lists as parameters, merges them, and returns a new list that is sorted in ascending
order.
Description: This exercise helps to understand how to manipulate lists, merge them,
and sort the elements. They will use methods like .extend() or + for merging and
.sort() for sorting."""


def merge_and_sort_lists(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list


my_list = merge_and_sort_lists([1, 8, 3], [4, 2, 9])
print(my_list)


""" # 2. Exercise: Set Operations
Objective: Develop a function set_operations(set1, set2) that returns a tuple
containing results of union, intersection, and difference between two sets.
Description: Through this task, you will learn about set operations. They will apply
methods such as .union(), .intersection(), and .difference() on sets. """


def set_operations(set1, set2):
    return set1.union(set2), set1.intersection(set2), set1.difference(set2)


my_tuple = set_operations({1, 8, 2}, {4, 2, 9})
print(my_tuple)


"""# 3. Exercise: Loop Through Numbers
Objective: Implement a function count_even_numbers(n) that returns the count of
even numbers from 1 to n (inclusive) using a loop.
Description: This function introduces students to looping constructs in Python. It
requires implementing a loop to iterate through a range of numbers and applying a
conditional statement to count even numbers."""


def count_even_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    return count


print(count_even_numbers(11))


"""# 4. Exercise: Dictionary Lookup
Objective: Write a function add_new_entry(dictionary, key, value) that adds a
new key-value pair to the provided dictionary and returns the updated dictionary.
Description: This exercise helps students learn how to manipulate dictionaries,
including adding new entries. They will also deal with checking if a key already
exists."""


def add_new_entry(dictionary, key, value):
    dictionary[key] = value
    return dictionary


print(add_new_entry({1: "a", 2: "b"}, 3, "c"))


"""# 5. Exercise: Array Indexing
Objective: Construct a function find_element(array, index) that returns the
element at the specified index from the array. If the index is out of bounds, it should
return None.
Description: This task uses the array data structure (students can use lists in Python
as a substitute). They will learn about indexing and handling exceptions related to
index errors."""


def find_element(array, index):
    if index >= len(array):
        return None
    return array[index]


print(find_element([1, 2, 3, 4, 5], 5))
print(find_element([1, 2, 3, 4, 5], 3))
