import unittest
from Distance import distance
from Invite_customer import invite_customer
from Print import print_cust

class Test(unittest.TestCase):

    def test_distance(self):

        test_dist = distance(54.180238,-5.920898)
        self.assertEqual(int(test_dist), 96)


    def test_invite_customer(self):

        test_list = invite_customer("customer_list.txt",100)
        for i in test_list:
            self.assertLess(i[2],100)


    def test_print(self):

        us_test_list = invite_customer("customer_list.txt",100)
        s_test_list = us_test_list

        print_cust(s_test_list,"customer_list.txt",100, "output.txt")
        self.assertListEqual(s_test_list,sorted(us_test_list))







if __name__ == '__main__':
    unittest.main()
