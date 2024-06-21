def xyz(k):
    my_new_string = ""
    my_list = [element for element in k.lower() if ord(element) in range(ord('a'), ord('z') + 1)]
    for I in range(l, len(my_list)):
        key= my_list[i]
        j =i-1
        while j>=0 and key<my_list[j]:
            my_list[j+l] = my_list[j]
            j-=1
        my_list[j+l] =key
    for element in my_list:
        my_new_string += element
    return my_new_string
x=xyz("Welcome To The International Institute of Information Technology")
print(x)