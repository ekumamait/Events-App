import unittest
from registration.signup import Registration

class RegistrationTests(unittest.TestCase):

    def setUp(self):
        self.register = Registration()

    def tearDown(self):
        pass

    def test_form(self):
        self.assertIsInstance(self.register, Registration)

    def test_create_username(self):
        self.register.username("Jane Doe")
        self.assertEqual(self.register.details["username"], "Jane Doe")

    def test_validate_user_name(self):
        with self.assertRaises(KeyError):
            self.register.username("")    

    def test_create_useremail(self):
        self.register.email("jane@mail.com")
        self.assertEqual(self.register.details["email"], "jane@mail.com")

    def test_validate_user_email(self):
        with self.assertRaises(KeyError):
            self.register.email("")    

    def test_add_category(self):
        self.register.category("vip")    
        self.assertEqual(self.register.details(("category"), "vip")

    def test_validate_category(self):
        with self.assertRaises(KeyError):
            self.register.category("")

    def test_add_ordinary_guest(self):
        self.register.username("James Safari")
        self.register.email("james@mail.com")
        self.register.category("ordinary")
        self.assertEqual(len(self.register.ordinary_list), 1)        

    def test_add_vip_guest(self):
        self.register.username("Tom Jones")
        self.register.email("tom@mail.com")
        self.register.category("vip")
        self.assertEqual(len(self.register.vip_list), 1)

    @unittest.skip("WIP")
    def test_unknown_methods(self):
        self.assertEqual(self.register.some_methods(), 1)    
