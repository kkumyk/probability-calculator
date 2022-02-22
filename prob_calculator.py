import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.contents = []
        for (k, v) in kwargs.items():
            if len(kwargs) > 0:
                self.contents.append("".join((k+",")*v).split(","))
        self.contents = [string for ball_list in self.contents for string in ball_list if (string != "")]
        print(self.contents)




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == "__main__":
    hat1 = Hat(red=3, blue=2)
