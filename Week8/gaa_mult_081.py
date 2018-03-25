class Score(object):
    def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points
    
    def __mul__(self, other):
      return Score(self.goals * other, self.points * other)

    def __rmul__(self, other):
      return Score(self.goals * other, self.points * other)

    def __imul__(self, other):
      self.goals = self.goals * other
      self.points = self.points * other
      return self


    def __str__(self):
      return str('{} goal(s) and {} point(s)'.format(self.goals, self.points))
    
