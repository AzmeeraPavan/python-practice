def comparingtwoindexvalue(a, b):
    pointfora =0
    pointforb = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            pointfora +=1

        elif b[i] > a[i]:
            pointforb +=1


    if pointfora > pointforb:
        result = f" A win {pointfora} point . List B has {pointforb}"
    elif pointforb > pointfora:
        result = f" B wins with {pointforb} points. List A has {pointfora} points."
    else:
        result = f"It's a tie! Both have {pointfora} points."

    return result



# define lists first
lista = [1, 2, 3]
listb = [3, 2, 3]

# call function
final = comparingtwoindexvalue(lista, listb)
print(final)
