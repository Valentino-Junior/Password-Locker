import unittest
from credential import Credential

class Test_credential(unittest.TestCase):
    '''
    A test class that describes a testcase for the credential class's behavior.
    
    '''

    def setUp(self):
        
        
        
        self.new_credential_info = Credential("Telegram","Valentino Junior","123456")
        


    def tearDown(self):
        '''
        Tear down method that does clean up after each test case has run
        '''
        Credential.credential_entry = []
        

    def test__init(self):
        '''
        These test is to evaluate whether the credential objects were created successfully.
        '''
        self.assertEqual(self.new_credential_info.site_name,"Telegram")
        self.assertEqual(self.new_credential_info.user_name,"Valentino Junior")
        self.assertEqual(self.new_credential_info.password,"12345")

    def test_save_credential(self):
        '''
        Test to check if the object is saved into the credentials list
        '''
        self.new_credential_info.save_credential()
        self.assertEqual(len(Credential.credential_entry),1)


    def test_delete_credential(self):
        '''
        These test is meant to see whether we can remove credentials from our credentials list.
        '''
        self.new_credential_info.save_credential()
        test_credentials = Credential("Telegram","Valentino Junior","123456")
        test_credentials.save_credential()

        self.new_credentials.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)

    def test_find_credentials(self):
        '''
        This is a test instance to see whether we can discover credentials by searching for the site name.
        '''
        self.new_credentials.save_credential()
        test_credentials = Credential("Telegram","Valentino Junior","123456")
        test_credentials.save_credential()

        found_credentials = Credential.find_by_account_name("Instagram")
        self.assertEqual(found_credentials.account_name, test_credentials.account_name)

    def test_credentials_exist(self):
        '''
        Test whether the credentials object actually exists
        '''
        self.new_credentials.save_credential()
        test_credentials = Credential("Telegram","Valentino Junior","123456")
        test_credentials.save_credential()

        credentials_exists = Credential.credential_exist("Instagram")
        self.assertTrue(credentials_exists)

    def test_display_credentials(self):
        '''
        These is a test that dislays all credentials that are present in the list
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_entry)





if __name__ == '__main__':
    unittest.main()
        