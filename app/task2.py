from collections import Counter


def group_and_count(list_version):
    """
    Group and count occurrences of lists in a list.

    Args:
        list_version (list): A list of lists to be processed.

    Returns:
        list: A list of lists, each containing the first and second elements of a unique list
              and their respective counts.
    """
    counter = Counter(tuple(item) for item in list_version)
    result = [[key[0], key[1], count] for key, count in counter.items()]
    return result


if __name__ == '__main__':
    with open("input/list_version.txt", "r") as file:
        List_version = file.read().split('\n')
    lst = []
    for i in List_version:
        new_lst = i.split(' ')
        lst.append([new_lst[0], int(new_lst[1])])

    groups = group_and_count(lst)
    print(groups)
