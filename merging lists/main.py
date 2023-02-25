def merge_sorted_lists(list1, list2):
    i = 0
    j = 0 
    result = []

    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result += list1[i:]
    result += list2[j:]

    return result
