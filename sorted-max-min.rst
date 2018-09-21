import operator

# Implement your function below.
def most_frequent(given_list):
    max_item = None
    max_count = -1
    mydic = {}
    for i in given_list:
        if i not in mydic:
            mydic[i] = 1
        else:
            mydic[i] += 1

        if mydic[i] > max_count:
            max_count = mydic[i]
            max_item = i

    a = sorted(mydic.items(), key=lambda elm: elm[1])
    b = max(mydic.items(), key=operator.itemgetter(1))[0]
    c = min(mydic.items(), key=operator.itemgetter(1))[1]

    return max_count


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]

# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print(most_frequent(list1))
