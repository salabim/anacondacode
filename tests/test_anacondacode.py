import os
import sys
from pathlib import Path
import itertools
import pandas as pd
import numpy as np

if __name__ == "__main__":  # to make the tests run without the pytest cli
    file_folder = Path(__file__).parent
    top_folder = (file_folder / ".." / "anacondacode").resolve()
    sys.path.insert(0, str(top_folder))
    os.chdir(file_folder)
    print(f"{file_folder=} {top_folder=}")

import pytest

def string_to_list_of_lists(s):
    c0=s.split("\n$$$\n")
    c1=[l.splitlines() for l in c0]
    data = [l for l in itertools.zip_longest(*c1)]
    return data

def string_to_df(s):
    data = string_to_list_of_lists(s)
    return pd.DataFrame(data[1:], columns=data[0])

def string_to_np(s):
    data = string_to_list_of_lists(s)
    return np.array(data)

from anacondacode import runner
from anacondacode import remove_output


def test_list_of_lists():
    data=string_to_list_of_lists("""\
x=10
y=8
$$$
output=x+y""")
    assert runner(data)==18

def test_df():
    data=string_to_df("""\
x=10
y=8
$$$
output=x+y""")
    assert runner(data)==18

def test_np():
    data=string_to_np("""\
x=10
y=8
$$$
output=x+y""")
    assert runner(data)==18

def test_module():
    data=string_to_list_of_lists("""\
import math
                                
# module = utils

def cube_root(x):
    return math.pow(x, 1/3)                                
                                                                
$$$
from utils import cube_root
output=cube_root(5832)""")
    assert runner(data) == pytest.approx(18)

def test_no_output():
    remove_output()

    data=string_to_list_of_lists("""\
x=10
y=8
$$$
x+y""")
    assert runner(data) is None


if __name__ == "__main__":
    pytest.main(["-vv", "-s", "-x", __file__])
