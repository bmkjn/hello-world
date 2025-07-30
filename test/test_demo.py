import pytest
# because python only looks for modules in the current directory, we need to add the current directory to the path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from demo import area_of_circle 

def test_area_of_circle():
    assert area_of_circle(5) == pytest.approx(78.54, rel=1e-2)
    assert area_of_circle(0) == 0
    assert area_of_circle(-1) == pytest.approx(3.14, rel=1e-2)

def test_area_of_circle_invalid():
    with pytest.raises(TypeError):
        area_of_circle("string")
    with pytest.raises(TypeError):
        area_of_circle(None)

