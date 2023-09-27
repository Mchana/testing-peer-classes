class Diary:
    def __init__(self, contents):
        self.contents = contents

    def read(self):
        print (self.contents)
        return self.contents