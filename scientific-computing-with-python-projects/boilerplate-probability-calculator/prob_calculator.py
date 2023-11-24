import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **bals):
        self.contents = []
        for k, v in bals.items():
            self.contents += [k]*v
    def draw(self, num): 
        res = []

        n = min(num, len(self.contents))

        for _ in range(n):
            index = random.randrange(0, len(self.contents))
            item = self.contents.pop(index)
            res.append(item)
        return res
    
def eval_experiment(expected_balls, draw):
    counter = Counter(draw)
    for ball, count in expected_balls.items():
        if counter.get(ball, 0) < count:
            return False
    return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0

    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        draw = copy_hat.draw(num_balls_drawn)
        count += eval_experiment(expected_balls, draw)

    return count/num_experiments

