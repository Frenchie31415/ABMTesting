class Evaluator:

    def eval(self):
            return self.eval_case_by_case()

    def set_actual(self, actual):
        self.actual = actual
    
    def set_predicted(self, predicted):
        self.predicted = predicted
    
    def eval(self):
        correct = 0
        incorrect = 0
        for i in range(0,len(self.actual)):
            actual = self.actual[i]
            predicted = self.predicted[i]

            if actual == predicted:
                correct = correct + 1
            else:
                incorrect = incorrect + 1
        
        return(correct / (correct + incorrect))