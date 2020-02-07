from assignment_2.linked_list import LinkedList


def checkpass(file, new_password):
    # open the txt file
    password_file = open(file, 'r+')
    passwords = password_file.read().split()
    passwords_table = [LinkedList() for _ in range(62)]

    # storing passwords in passwords_table (hash table)
    for password in passwords:
        first_char = password[0]
        if first_char.islower():
            index = ord(first_char) - 61
            passwords_table[index].insert_at_end(password[1::])
        elif first_char.isupper():
            index = ord(first_char) - 55
            passwords_table[index].insert_at_end(password[1::])
        else:
            index = ord(first_char) - 48
            passwords_table[index].insert_at_end(password[1::])

    # check if new_password is valid
    # 1. check duplicate
    first_char = new_password[0]
    if first_char.islower():
        index = ord(first_char) - 61
        check1 = passwords_table[index].check_duplicate(new_password)
    elif first_char.isupper():
        index = ord(first_char) - 55
        check1 = passwords_table[index].check_duplicate(new_password)
    else:
        index = ord(first_char) - 48
        check1 = passwords_table[index].check_duplicate(new_password)
    if check1:
        print('duplicate exists')
    # 2. check alnum

    # 3. check length


    # if valid add to file


if __name__ == "__main__":
    checkpass('passwords.txt', 'Fr2C6XNJbA')
