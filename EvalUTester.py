import unittest
from Evaluator import Evaluator

class EvalUTester(unittest.TestCase):

    #Predicted = Actual
    def test_identical_case(self):
        print("Start identical_case test\n")
        self.evaluator = Evaluator()
        self.path_1 = ["abc","defgh","ijklmno","pqrst","uvwxyz"]
        print("Actual paths", self.path_1)
        print("Predicted path", self.path_1)
        self.evaluator.set_actual(self.path_1)
        self.evaluator.set_predicted(self.path_1)
        predicted_accuracy = self.evaluator.eval()
        actual_accuracy = 1
        self.assertEqual(predicted_accuracy,actual_accuracy)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()