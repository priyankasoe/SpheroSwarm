#list of motion vectors for each discrete "step"
#atom numbering is currently arbitrary, will change later (and add start postitions)
carbon1 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
oxygen1 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen1 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen2 = [(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
carbon2 = [(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen3 = [(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen4 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen5 = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
carbon3 = [(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
hydrogen6 = [(-1,0),(-1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]

class Atom:
  def __init__(name, vectors, startPos):
    name.vectors = vectors
    name.startPos = startPos