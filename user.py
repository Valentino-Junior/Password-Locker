class User:
    """
    a class that generates new user instances 
    """

    users_entry= []

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user_details(self):
        """
        This method saves user info into user_array
        """
        User.users_entry.append(self)

    @classmethod
    def display_users(cls):
        """
        The class array is returned by this function.
        """
        return cls.users_array