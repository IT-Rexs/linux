#from main import get_users

#def test_users():
 #   users = get_users()
  #  #assert len(users) > 0
   # #assert ('Jane', 'Smith', 25) in users
   # print("Test is succcessful")
import unittest
from main import get_users

class TestDB(unittest.TestCase):

    def test_get_users(self):
        users = get_users()
        self.assertTrue(len(users) > 0)
        self.assertTrue((2,'Jane', 'Smith', 25) in users)

if __name__ == '__main__':
    unittest.main()
