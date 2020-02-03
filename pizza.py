class Pizza:

  # Constructeur
  def __init__(self, index, slices):
    self.index = index
    self.slices = int(slices)
  
  
  # Equivalent de toString  
  def __repr__(self):
    return str(self.index) + " " + str(self.slices)
    
    
