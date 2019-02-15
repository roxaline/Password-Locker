import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credential("uwabikiramariya8","twitter","roxaline","uwabikiramariya8")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.view_password,"uwabikiramariya8")
        self.assertEqual(self.new_credential.account,"github")
        self.assertEqual(self.new_credential.login,"roxaline")
        self.assertEqual(self.new_credential.password,"uwabikiramariya8")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saves into
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        """
        test_save_multiple_credential to check if one can save multiple credentials
        """
        self.new_credential.save_credential()
        test_credential = Credential("uwabikiramariya8","test","login","uwabikiramariya8")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_contact to test if we can remove credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential ("uwabikiramariya8","test","login","uwabikiramariya8") # new credential
        test_credential.save_credential()

        self.new_credential.del_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

    def test_display_all_credentials(self):
        """
        test_display_all_credentials to returns a list of all credentials saved
        """
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()
