from copy import deepcopy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for (color, count) in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        removed_balls = random.sample(self.contents, num_balls)
        for ball in removed_balls:
            self.contents.remove(ball)
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        copied_hat = deepcopy(hat)
        removed_balls = Counter(copied_hat.draw(num_balls_drawn))  # red red red green blue
        successful_experiments += successful_experiment(expected_balls, removed_balls)

    return successful_experiments / num_experiments  # probability


def successful_experiment(expected_balls, removed_balls):
    for (expected_color, expected_count) in expected_balls.items():
        if removed_balls[expected_color] < expected_count:
            return 0
    return 1


if __name__ == "__main__":
    print(experiment(Hat(blue=3, red=2, green=6), {"blue": 2, "green": 1}, 4, 3000))
