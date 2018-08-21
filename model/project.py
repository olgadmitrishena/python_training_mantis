from sys import maxsize

class Project:


    def __init__(self, id=None, name=None, description=None, status=None, view_state=None):
        self.name = name
        self.id = id
        self.description = description
        self.view_state = view_state
        self.status = status


    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)


    def __repr__(self):
        return "%s" % self.name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize