class Score(object):
    def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points
    
    def __eq__(self, other):
      return((self.goals * 3 + self.points) == (other.goals * 3 + other.points))

    def __gt__(self, other):
      return((self.goals * 3 + self.points) > (other.goals * 3 + other.points))

    def __lt__(self, other):
      return((self.goals * 3 + self.points) < (other.goals * 3 + other.points))

    def __ge__(self, other):
      return((self.goals * 3 + self.points) >= (other.goals * 3 + other.points))

    def __le__(self, other):
      return((self.goals * 3 + self.points) <= (other.goals * 3 + other.points))

    def __add__(self, other):
      return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
      return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
      self.goals += other.goals
      self.points += other.points
      return self

    def __isub__(self, other):
      self.goals -= other.goals
      self.points -= other.points
      return self

    def __str__(self):
      return str('{} goal(s) and {} point(s)'.format(self.goals, self.points))
    
