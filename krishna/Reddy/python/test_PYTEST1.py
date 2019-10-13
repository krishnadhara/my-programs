import pytest

# how to execute setup,teardown,setupclass,teardownclass parally
@pytest.yield_fixture(scope="module")    # setup and teardown execution decorater
def setup_teardown_class():              #(o/p=  setup_class ,m1,  m2 ,m3 ,teaddown_class )
    print("setup_class")
    yield
    print("teardown_class")
@pytest.yield_fixture()    # setup and teardown execution decorater
def setup_teardown():      #(o/p=  setup ,m1,teaddown  ,setup,  m2 ,teaddown , setup,  m3 ,teaddown )
    print("setup")
    yield
    print("tierdown")

def test_m1(setup_teardown_class,setup_teardown):
    print("m1")

def test_m2(setup_teardown_class,setup_teardown):
    print("m2")

def test_m3(setup_teardown_class,setup_teardown):
    print("m3")