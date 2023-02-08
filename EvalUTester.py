import unittest
from Evaluator import Evaluator

class EvalUTester(unittest.TestCase):

    #Predicted = Actual
    def test_0_identical_case(self):
        print("Start identical_case test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["abc","defgh","ijklmno","pqrst","uvwxyz"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_1)
        self.evaluator.set_actual(self.path_1)
        self.evaluator.set_predicted(self.path_1)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 1
        self.assertEqual(predicted_accuracy,actual_accuracy,"The predicted and actual are identitical")
        print("Finish identical_case test\n")

    #Predicted != Actual (Same length)
    def test_1_diffent_paths_same_length_case(self):
        print("Start diffent_paths_same_length test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["abc","defgh","ijklmno","pqrst","uvwxyz"]
        self.path_2 = ["def","abcfg","pqrstmn","uvwxy","pqgrst"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_2)
        self.evaluator.set_actual(self.path_1)
        self.evaluator.set_predicted(self.path_2)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 0
        self.assertEqual(predicted_accuracy,actual_accuracy,"The predicted and actual are different but of the same lengths")
        print("Finish diffent_paths_same_length test\n")

    #Predicted != Actual (Same length)
    def test_2_diffent_paths_different_length_case(self):
        print("Start diffent_paths_different_length test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["abc","defgh","ijklmno","pqrst","uvwxyz"]
        self.path_2 = ["defe","abcfgg","pqrstmdn","uvwsxy","pqgrtst"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_2)
        self.evaluator.set_actual(self.path_1)
        self.evaluator.set_predicted(self.path_2)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 0
        self.assertEqual(predicted_accuracy,actual_accuracy,"The predicted and actual are different with different lengths")
        print("Finish diffent_paths_different_length test\n")

    def test_3_more_predicted_paths_case(self):
        print("Start more_predicted_paths test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["defe","defgh"]
        self.path_2 = ["defe"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_2)
        self.evaluator.set_actual(self.path_1)
        self.evaluator.set_predicted(self.path_2)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 0
        self.assertEqual(predicted_accuracy,actual_accuracy,"There is more predicted than actual paths")
        print("Finish more_predicted_paths test\n")

    def test_4_more_actual_paths_case(self):
        print("Start more_actual_paths test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["defe","defgh"]
        self.path_2 = ["defe"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_2)
        self.evaluator.set_actual(self.path_2)
        self.evaluator.set_predicted(self.path_1)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 0
        self.assertEqual(predicted_accuracy,actual_accuracy,"There is more predicted than actual paths")
        print("Finish more_actual_paths test\n")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()