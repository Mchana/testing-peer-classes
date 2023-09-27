from lib.diary import Diary
import pytest 

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.lock = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.lock == True:
            raise Exception("Go away!")
        else:
            return self.diary.read()

    def lock(self):
        self.lock = True

    def unlock(self):
        self.lock = False