from copy import deepcopy
import random
from collections import Counter


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
    total_counts = 0
    for num in range(num_experiments):
        copied_hat = deepcopy(hat)
        removed_balls = copied_hat.draw(num_balls_drawn)
        remaining_balls = copied_hat.contents
        print("remaining_balls", remaining_balls)
        filtered_balls = [b for b in remaining_balls if b in set(expected_balls_contents)]
        n = Counter(filtered_balls)
        filtered_dict = dict(n)
        print("filtered dict", sorted(filtered_dict.values()))
        print("expected_balls", sorted(expected_balls.values()))

        minus_ball_pairs = [a - b for a, b in zip(sorted(filtered_dict.values()), sorted(expected_balls.values()))]
        negative_count = 0
        for b in minus_ball_pairs:
            if b < 0:
                negative_count += 1
            if negative_count == 0:
                total_counts += 1

    # print(expected_balls_contents, removed_balls, remaining_balls)
    print("count:", total_counts)
    print("expected_balls_contents", expected_balls_contents)
    print("remaining_balls", remaining_balls)
    print("filtered_balls", filtered_balls)

    probability = total_counts / num_experiments

    return probability  # probability  # expected_balls_contents, removed_balls, remaining_balls  #


if __name__ == "__main__":
    print(experiment(Hat(blue=3, red=2, green=6), {"blue": 2, "green": 1}, 4, 3000))
