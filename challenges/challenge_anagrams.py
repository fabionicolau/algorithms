def bubble_sort(string):
    string = list(string.replace(" ", "").lower())
    n = len(string)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if string[j] > string[j + 1]:
                string[j], string[j + 1] = string[j + 1], string[j]
    return "".join(string)


def is_anagram(first_string, second_string):
    is_true = False
    if not first_string or not second_string:
        is_true = False
    elif bubble_sort(first_string) == bubble_sort(second_string):
        is_true = True

    return (
        bubble_sort(first_string),
        bubble_sort(second_string),
        is_true,
    )
