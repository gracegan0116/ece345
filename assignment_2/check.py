def check (string):
    length = len(string)
    # check the length of the password which will be 6 to 12 characters long
    if length < 6 or length > 12:
        return False
    # Version1, directly use the python function
    # if string.isalnum() != True:
    #     return False
    
    # Version2, compare each character in the string
    count = 0
    for item in string:
        if (item > "0" and item < "9") or (item > "A" and item < "Z") or (item > "a" and item < "z"):
            count = count + 1
    if count == length:
        return True
    return False    

if __name__ == "__main__":
    input_str = input("Enter your password : ")
    result = check(input_str)
    print(result)