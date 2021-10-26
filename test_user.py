import unittest
from user import User

class Test_user(unittest.TestCase):
    '''
    A test class that describes a testcase for the user class's behavior.
    '''

    def setUp(self):      
        self.new_user_info = User("Valentino","Junior", "1234")
       


    def tearDown(self):
        '''
        Tear down method cleans up after each test case has run
        '''
        User.users_entry = []
        

    def test__init(self):
        '''
        After each test case has completed, the tear down method cleans up.
        '''
        
        self.assertEqual(self.new_user_info.first_name,"Valentino")
        self.assertEqual(self.new_user_info.last_name,"Junior")
        self.assertEqual(self.new_user_info.password,"1234")

    def test_save_users(self):
        '''
        It is done to check whether the item has been stored in the users list.
        '''
        self.new_users.save_user()
        self.assertEqual(len(User.users_entry),1)

    

  


if __name__ == '__main_':
    unittest.main()