class Musculoskeletal_System:
  # Constructor
  def __init__(self, var01):
    self.cell_kind = var01

  # A simple function
  def move(self):
    if (self.cell_kind in ["muscles","bones"]):
      return True
    else:
      return False
