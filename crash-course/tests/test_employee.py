import pytest
from employee import Employee

@pytest.fixture
def emp():
    emp = Employee('Elias', 'rojas', 40000)
    return emp

def test_give_default_raise(emp):
    emp.give_raise()
    assert emp.salary == 45000

def test_give_custom_raise(emp):
    emp.give_raise(5630)
    assert emp.salary == 45630
