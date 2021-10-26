class Credential:
    """
    a class that creates new user credentials
    """

    credential_array = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email