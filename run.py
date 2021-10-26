
from credential import Credential
from user import User
import random


def main():
    print('WELCOME TO PASSWORD LOCKER!!')
    name = input('Please enter your name:')


    while True:
        print(f"Hello {name}, Please use these short codes to either sign up or login to your account.") 
        user_shortcuts = input("lg - login","sn- sign up").upper()
        
        
if __name__ == '__main__':
    main()