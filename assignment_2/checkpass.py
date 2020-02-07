#!/usr/bin/env python3
from linked_list import LinkedList
import sys


def checkpass(file, new_password):
    # open the txt file
    password_file = open(file, 'r+')
    passwords = password_file.read().split()
    passwords_table = [LinkedList() for _ in range(62)]

    # storing passwords and the reversed_passwords in passwords_table (hash table)
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

        last_char = password[-1]
        if last_char.islower():
            index = ord(last_char) - 61
            passwords_table[index].insert_at_end(password[-2::-1])
        elif last_char.isupper():
            index = ord(last_char) - 55
            passwords_table[index].insert_at_end(password[-2::-1])
        else:
            index = ord(last_char) - 48
            passwords_table[index].insert_at_end(password[-2::-1])

    # check if new_password is valid
    # 1. check length (valid length: 6-12)
    length = len(new_password)
    if length < 6 or length > 12:
        print("INVALID")
        return
    
    # 2. check alnum
    if new_password.isalnum() != True:
        print("INVALID")
        return

    # 3. check duplicate
    first_char = new_password[0]
    if first_char.islower():
        index = ord(first_char) - 61
        check1 = passwords_table[index].check_duplicate(new_password[1::])
    elif first_char.isupper():
        index = ord(first_char) - 55
        check1 = passwords_table[index].check_duplicate(new_password[1::])
    else:
        index = ord(first_char) - 48
        check1 = passwords_table[index].check_duplicate(new_password[1::])
    if check1:
        print("INVALID")
        return

    # 4. check reverse duplicate
    last_char = new_password[-1]
    if last_char.islower():
        index = ord(last_char) - 61
        check2 = passwords_table[index].check_duplicate(new_password[-2::-1])
    elif last_char.isupper():
        index = ord(last_char) - 55
        check2 = passwords_table[index].check_duplicate(new_password[-2::-1])
    else:
        index = ord(last_char) - 48
        check2 = passwords_table[index].check_duplicate(new_password[-2::-1])
    if check2:
        print("INVALID")
        return

    # if valid add to hash table and file
    passwords_table[index].insert_at_end(new_password)
    password_file.write(new_password+"\n")
    print("VALID")


if __name__ == "__main__":
    checkpass(sys.argv[1], sys.argv[2])
