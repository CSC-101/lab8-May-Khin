#Part 1
def groups_of_3(lista: list[int]) -> list[list[int]]:
    result = []
    temp = []
    for num in lista:
        temp.append(num)
        if len(temp) == 3:
            result.append(temp)
            temp = []
    if temp:
        result.append(temp)
    return result

