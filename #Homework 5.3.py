#Homework 5 Task 3

def merge_lists(list1, list2):
    merged = list1.copy()

    for item, quantity in list2.items():
        if item in merged:
            merged[item]+= quantity
        else:
            merged[item] = quantity
    return merged

list1 = {"milk": 2, "bread":1, "eggs": 12}
list2 = {"bread": 2, "cheese":1, "milk":1}

result = merge_lists(list1, list2)
print(result)
