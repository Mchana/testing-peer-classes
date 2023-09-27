from unittest.mock import Mock
from lib.secret_diary import SecretDiary
import pytest

def test_diary_locked_initially():
    diary1 = Mock()
    secret1 = SecretDiary(diary1)
    with pytest.raises(Exception) as e:
        secret1.read()
    assert str(e.value) == "Go away!"

def test_diary_unlocked():
    diary2 = Mock()
    diary2.read.return_value = "not secret"
    secret2 = SecretDiary(diary2)
    secret2.unlock()
    assert secret2.read() == "not secret"

def test_diary_locking_method():
    diary3 = Mock()
    secret3 = SecretDiary(diary3)
    secret3.unlock()
    secret3.lock()
    with pytest.raises(Exception) as e:
        secret3.read()
    assert str(e.value) == "Go away!"