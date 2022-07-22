import itertools
import time

from Class.User import *


class BbruteForce:
    def __init__(self):
        self.filePath = None
        self.user = User("")

    # Set file path
    def setFilePath(self, path):
        self.filePath = path

    # Get a list of passwords from a file
    def get_list_of_passwords(self):
        with open(self.filePath, 'r') as f:
            return f.read().splitlines()

    # Give file to method and find good password
    def find_password_from_file(self, password):
        with open(self.filePath, 'r') as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False

    # Try brute force with the file
    def brute_force_with_file(self):
        list_of_passwords = self.get_list_of_passwords()
        for password in list_of_passwords:
            print("Trying password: %s" % password)
            try:
                if password == self.user.getPassword():
                    print("The password found")
                    return password
            except Exception as e:
                print(e)
                continue
        print("The password not found")

    # Try Brute force by combinaison of characters/words
    def brute_force_with_combinaison(self):
        start = time.time()
        chars = self.user.getPassword()
        attempts = 0
        for i in range(1, 9):
            for letter in itertools.product(chars, repeat=i):
                attempts += 1
                letter = ''.join(letter)
                print(letter)
                if letter == self.user.getPassword():
                    end = time.time()
                    distance = end - start
                    print("The password found after %s tries and %s seconds!" % (attempts, distance))
                    return True
        return False
