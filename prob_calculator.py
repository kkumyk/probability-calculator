import copy
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
    pass

#
# if __name__ == "__main__":
#     hat1 = Hat(red=3, blue=2)
#     print(hat1.draw(2))
