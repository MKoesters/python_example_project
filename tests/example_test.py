import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
import pytest
from src.hello_world import hello_world


def test_hello_world():
    assert hello_world() == "Hello world!"
