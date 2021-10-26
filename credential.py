# class Credential:
#     """
#     Instances of user account credentials are created by this class.
#     """

#     credential_entry = []

#     def __init__(self, site_name, user_name, password ):
#         self.site_name = site_name
#         self.user_name = user_name
#         self.password = password
        

#     def save_credential(self):
#         """
#         The save contact method saves credential objects in the credential array.
#         """
#         Credential.credential_entry.append(self)


#     def delete_credential(self):
#         '''
#         Delete a credential from the list using this method.
#         '''
#         Credential.credential_entry.remove(self)

#     @classmethod
#     def display_credential(cls):
#         """
#         The credential array is returned by this function.
#         """
#         return cls.credential_entry


#     @classmethod
#     def locate_account(cls, account_name):
#         '''
#         A method that accepts a site name and returns the credentials for that site.
#         '''
#         for credential in cls.credential_entry:
#             if credential.account_name == account_name:
#                 return credential