def sort_anagrams(list_of_strings):
    container = []
    j=0
    while j < len(list_of_strings):
        i = 1
        rev_list = [list_of_strings[j]]
        while i < len(list_of_strings):
            if sorted(list_of_strings[j]) == sorted(list_of_strings[i]):
                rev_list.append(list_of_strings[i])
            i += 1
        container.append(rev_list)
        for e in rev_list:
            list_of_strings.remove(e)
    return container
