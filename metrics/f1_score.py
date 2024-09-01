from decorators import Metric
@Metric
class F1Score():
    def __init__(self):
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
    
    def update(self, predictions, targets):
        self.true_positives += ((predictions == 1) & (targets == 1)).sum().item()
        self.false_positives += ((predictions == 1) & (targets == 0)).sum().item()
        self.false_negatives += ((predictions == 0) & (targets == 1)).sum().item()
    
    def compute(self):
        precision = self.true_positives / (self.true_positives + self.false_positives)
        recall = self.true_positives / (self.true_positives + self.false_negatives)
        f1_score = 2 * (precision * recall) / (precision + recall)
        return f1_score