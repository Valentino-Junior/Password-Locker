
from credential import Credential
from user import User
import random
import string


 #credential methods
def create_credential(site_name, user_name, password ):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(site_name, user_name, password )
    return new_credential



def save_credential(credential):
    '''
    Funtion to save the credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(site_name):
    '''
    Function to find a credential
    '''
    return Credential.locate_account(site_name)

def check_existing_credentials(account_name):
    '''
    Function to check whether a credential exists
    '''
    return Credential.credential_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()



#Users method
def create_user(first_name, last_name, password):
    '''
   To generate a new user credential, use this function.
    '''
    new_user = User(first_name, last_name, password)
    return new_user

def save_users(user):
    '''
    The user credential is saved using this function.
    '''
    user.save_users()


def main():
    # print('WELCOME TO PASSWORD LOCKER!!')
    # name = input('Please enter your name: ')
    # print(f"Hello {name}, Please use these short codes to either sign up or login to your account.") 
    # user_shortcuts = input("lg - login sn- sign up ").upper()
   
    
    # if user_shortcuts == 'lg':
    #     print('Enter username: ')
    #     lg_shortcut = input()
    #     print('Enter password: ')
    #     sn_shortcut = input()

    #     print('lOGIN SUCCESSFUL')

    print("HELLO, WELCOME TO PASSWORD LOCKER.")
    usr_name = input("Please enter your name:")

    while True:
        print('*'*60)
        print(f"Hello {usr_name}, Kindly use these short codes to either sign up or login to your account.") 
        print("lg - log into your account")
        print("sn - sign up to new users")
        short_code = input("Enter short code:").upper()

        if short_code == 'sn':
        
            print("Enter  first_name: ")
            fst_name = input()

            print("Enter  last_name: ")
            lst_name = input()

            print("Enter password")
            fpin = input()
            print('*' *60)

            

            print("You've successfully completed the registration process.",)
            print("Kindly, proceed by logging into your account",)
            print('\n')
            print('*' *60)    

            print("Enter your username")
            username = input()
           
            print("Enter your password")
            pin = input()
            if f"{fst_name }. {lst_name} == username and fpin == pin":
                print(f"{username}, you've succesfully logged into your account")
                print('\n')

                print('*' *60)

                pass
                while True:
                    print("Use these short codes: sc - Save credentials \n, cc - Create new credentials \n, dc - display credentials \n, lc - locate saved credential \n, del - delete credentials \n, ex - exit the account", "magenta")

                    short_code = input().upper()

                    if short_code == 'cc':
                        print(" Create New Credentials")
                        print("-"*20)

                        print(" Input Site Name: ")
                        site_name = input()

                        print(" Input User Name: ")
                        user_name = input()

                        

                        print("Would you prefer a password that is customized for you?, respond by  YES or NO")
                        password = input().lower()
                        if password == 'YES':
                            print("What length do you want your password to be?")
                            password_length = int(input())
                            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                            pass_length = "".join(random.choice(chars) for i in range(password_length))
                       
                        elif password == 'NO':
                            print("Enter the password you would like to use.")
                            pass_length= input()

                        else:
                            print("Wrong input, enter yes or no",)

                        save_credential(create_credential(site_name, user_name, pass_length)) #Create and save credentials
                        print('\n')
                        print('-'*30)
                        print(f"{user_name}, your new credential has successfully been created", )
                        print('-'*30)
                        print('\n')

                    elif short_code == 'sc':
                        print("Save Existing credentials")
                        print("-"*10)

                        print(" Input Site Name: ")
                        site_name = input()

                        print(" Input User Name: ")
                        user_name = input()


                        print("Input Password: ")
                        password = input()

                        
                    
                        save_credential(create_credential(site_name, user_name, password)) #Create and save credentials
                        print('\n')
                        print(f"{site_name} credentials successfully saved")
                        print('\n')


                    elif short_code == 'dc':
                        if display_credentials():
                            print("The following is a list of all of your credentials.")
                            print('\n')

                            for credential in display_credentials():
                                print(f"{credential.account_name}")
                                print("-"*30)
                                print(f"Username: {credential.first_name} {credential.last_name}")
                                print(f"Password: {credential.user_password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have any stored credentials.")
                            print('\n')

                    elif short_code == 'lc':
                        print("Please type the name of the site you're looking for into the below.\n")

                        search_site = input("Site Name: ")
                        if check_existing_credentials(search_site):
                            search_site = find_credential(search_site)
                            print(f"{search_site.first_name} {search_site.last_name}")
                            print("-"*20)

                            print(f"Password: {search_site.user_password}")

                        else:
                            print("These credentials aren't available.")
                            print('\n')

                    elif short_code == 'del':
                        print("Please type the name of the site you wish to remove below.\n")
                        site_delete = input()
                        if check_existing_credentials(site_delete):
                            site_delete = find_credential(site_delete)
                            delete_credential(site_delete)

                            print("Credentials were successfully removed.")

                        else:
                            print("There are no credentials.")


                    elif short_code == "ex":
                        print("THANK YOU FOR USING PASSWORD LOCKER AND WELCOME BACK AGAIN!!",)
                        print('\n')
                        print('-'*20)
                        break
#                     else:
#                         print("I really didn't get that")
#             else:
#                 print("Login credentials are invalid.")
#                 print('\n')

#         elif short_code == 'lg':
#             print("Please Enter your name")
#             inputname = input()

#             print("Enter Your Password")
#             inputpass = input()

#             print("The login information you submitted seems not to be valid. Before you can log in, you must first register an account.")
#             print('\n')
   

        
# if __name__ == '__main__':
#     main()