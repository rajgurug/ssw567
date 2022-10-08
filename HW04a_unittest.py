from HW04a_function import no_of_commit_in_repository
import unittest
class test_rep(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(no_of_commit_in_repository('rajgurug', 'trajguru567', 'rajguru7337', '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'),'Repo: trajguru567 Number of commits: 8',"The repository is in the github account")

    def testcase2(self):
        self.assertNotEqual(no_of_commit_in_repository('rajgurug', 'trajguru567', 'rajguru7337', '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'), 'Repo: trajguru567 Number of commits: 2',"This repository has 2 in the github account")

    def testcase3(self):
        self.assertEqual(no_of_commit_in_repository('rajgurug', 'SSW567_classify_triangle_2', 'rajguru7337','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'), 'Repo: SSW567_classify_triangle_2 Number of commits: 3', "The repository is in the github account")




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()






