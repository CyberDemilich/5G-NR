class Core5G():
  def __init__(self):
    self.amfs = [AMF(1), AMF(2)]
    self.upfs = [UPF(1), UPF(2)]
    self.gnbs = [GNB(1), GNB(2)]

class AMF():
  def __init__(self, id: int):
    self.id = id

class UPF():
  def __init__(self, id: int):
    self.id = id

class GNB():
  def __init__(self, id: int):
    self.id = id

if __name__ == "__main__":
  core = Core5G()