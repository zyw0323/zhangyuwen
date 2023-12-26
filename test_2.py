import random
import pytest
import yaml

@pytest.mark.flaky(reruns=6,reruns_delay=2)
def test_example():
    print(3)
    assert random.choice([True,False])

# def test_simple_assume(x, y):
#     pytest.assume(x == y)
#     pytest.assume(True)
#     pytest.assume(False)

@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True
