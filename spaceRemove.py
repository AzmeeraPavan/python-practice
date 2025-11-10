s="12n21"
print(s)
def palam (s):
    with_out_space=s.replace(" ",'')
    print(with_out_space)
    small_letter=with_out_space.lower()
    print(small_letter)
    invert=small_letter[::-1]
    print(invert)
    if invert == small_letter:
        print("palendram :",invert)
    else:
        print(" not palendram :",invert)
palam(s)


