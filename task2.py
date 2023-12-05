from collections import Counter


def group_and_count(list_version):
    counter = Counter(tuple(item) for item in list_version)
    result = [[key[0], key[1], count] for key, count in counter.items()]
    return result


if __name__ == '__main__':
    with open("./input/list_version.txt", "r") as file:
        List_version = file.read().split('\n')
    lst = []
    for i in List_version:
        new_lst = i.split(' ')
        lst.append([new_lst[0], int(new_lst[1])])

    groups = group_and_count(lst)
    print(groups)
