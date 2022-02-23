from copy import deepcopy
import random

class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.contents = []
        for (k, v) in kwargs.items():
            if len(kwargs) > 0:
                self.contents.append("".join((k + ",") * v).split(","))
        self.contents = [string for ball_list in self.contents for string in ball_list if (string != "")]

    def draw(self, nr_of_balls_to_draw):
        if nr_of_balls_to_draw > len(self.contents):
            return self.contents
        else:
            removed_balls = random.sample(self.contents, nr_of_balls_to_draw)
            for ball in removed_balls:
                self.contents.remove(ball)
            return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_contents = []
    for (k, v) in expected_balls.items():
        if len(expected_balls) > 0:
            expected_balls_contents.append("".join((k + ",") * v).split(","))
    expected_balls_contents = [string for ball_list in expected_balls_contents for string in ball_list if
                               (string != "")]

    # count how many times COUNT we get at least 2 red balls and 1 green ball
    # 1. draw num_balls_drawn from the hat num_experiments times
    # 2. count how many expected_balls in the remaining balls, add to count
    count = 0
    copied_hat = deepcopy(hat)

    for num in range(num_experiments):
        removed_balls = copied_hat.draw(num_balls_drawn)
        remaining_balls = copied_hat.contents

        if set(expected_balls).issubset(remaining_balls):
            count += 1
        else:
            count += 0
        print(expected_balls_contents, removed_balls, remaining_balls)
    probability = count / num_experiments


    return probability  # probability  # expected_balls_contents, removed_balls, remaining_balls  #


if __name__ == "__main__":
    # hat1 = Hat(red=3, blue=2)
    print(experiment(Hat(blue=4, red=2, green=6), {"blue": 2, "red": 1}, 4, 3000))
