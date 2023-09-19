import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for color in balls:
      for i in range(balls[color]):
        self.contents.append(color)

  def draw(self, quantity):
    if quantity < len(self.contents):
      dBalls = []
      for i in range(quantity):
        ball = random.choices(self.contents, k=1)
        self.contents.remove(ball[0])
        dBalls.append(ball[0])

      return dBalls
    else:
      return self.contents

  def retrunballs(self, balls):
    for ball in balls:
      self.contents.append(ball)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  num_experiments = num_experiments 
  for i in range(num_experiments):
    actual_balls = hat.draw(num_balls_drawn)
    hat.retrunballs(actual_balls)
    r = 0
    for expected_ball in expected_balls:
      if expected_balls[expected_ball] <= actual_balls.count(expected_ball):
        r += 1
    if r == len(expected_balls):
      m += 1

  probability = m / num_experiments
  return probability


hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat,
                         expected_balls={
                             "blue": 2,
                             "green": 1
                         },
                         num_balls_drawn=4,
                         num_experiments=1000)

print(probability)