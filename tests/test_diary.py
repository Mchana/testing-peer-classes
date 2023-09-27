from unittest.mock import Mock
from lib.diary import Diary

def test_read():
    diary1 = Diary("ham")
    assert diary1.read() == "ham"