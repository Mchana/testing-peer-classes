from unittest.mock import Mock
import pytest 
from lib.diary import Diary
from lib.secret_diary import SecretDiary

def test_read_when_locked():
    diary = Diary("secret")
    secretdiary = SecretDiary(diary)

    with pytest.raises(Exception) as e:
        secretdiary.read()
    assert str(e.value) == "Go away!"

def read_when_unlocked():
    diary1 = Diary("not secret")
    secretdiary1 = SecretDiary(diary1)
    secretdiary1.unlock()

    assert secretdiary1.read() == "not secret"