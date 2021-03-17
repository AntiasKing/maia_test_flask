import datetime

class Notification:
  read = False
  date = datetime.datetime.now()

  def __init__(self, id, msg) -> None:
    self.id = id
    self.message = msg

  def toggleRead(self):
    self.read = not self.read

  def toJSON(self):
    return {'id': self.id, 'msg': self.message, 'read': self.read, 'date': self.date}
