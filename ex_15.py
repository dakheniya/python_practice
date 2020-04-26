def reverse():
    string = str(input("Enter your string: "))
    split = string.split(" ")
    split.reverse()
    new_string = str(" ".join(split))
    return new_string

reverse()