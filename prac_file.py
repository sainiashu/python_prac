import  pytest

def add_number(a,b):
    return  a+b

@pytest.mark.parametrize('a,b, expected',[
    (1,2,3),
    (2,3,5),
    (2,3,7)

])
def test_add_numbers(a,b,expected):
    assert add_number(a,b) == expected