import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(books: list[data.Book]) -> None:
    for idx in range(len(books) -1):
        smallest_idx = idx
        for i in range(idx + 1, len(books)):
            if books[i].title < books[smallest_idx].title:
                smallest_idx = i
        books[smallest_idx], books[idx] = books[idx], books[smallest_idx]
# Part 2
def swap_case(s: str) -> str:
    result = []
    for letter in s:
        if letter.islower():
            result.append(letter.upper())
        elif letter.upper():
            result.append(letter.lower())
        else:
            result.append(letter)
    return "".join(result)
# Part 3
def str_translate(s: str, old: str, new: str ) -> str:
    result = []
    for letter in s:
        if letter == old:
            result.append(new)
        else:
            result.append(letter)
    return "".join(result)
# Part 4
def histogram(s: str) -> dict:
    word_count = {}
    words = s.split()
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word]=1
    return word_count
