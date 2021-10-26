class Credential:
    """
    a class that creates new user credentials
    """

    credential_array = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        Credential objects are saved in credential array via the save contact function.
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        The credential array is returned by this function.
        """
        return cls.credential_array