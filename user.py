class User:
    """
    a class that generates new user instances 
    """

    users_array = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def save_user_details(self):
        """
        This method saves user info into user_array
        """
        User.users_array.append(self)

    @classmethod
    def display_users(cls):
        """
        The class array is returned by this function.
        """
        return cls.users_array