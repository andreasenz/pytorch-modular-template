from decorators import Metric
@Metric
class Accuracy():
    def __init__(self):
        self.correct = 0
        self.total = 0

    def update(self, predictions, targets):
        self.correct += (predictions == targets).sum().item()
        self.total += len(targets)

    def compute(self):
        return self.correct / self.total