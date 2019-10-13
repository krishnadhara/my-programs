import pytest
@pytest.fixture()     # setup execution decorater
def setup():          #(o/p=  setup ,m1   ,setup,  m2, setup,  m3)
    print("setup")
def test_m1(setup):
    print("m1")
def test_m2(setup):
    print("m2")
def test_m3(setup):
    print("m3")

@pytest.yield_fixture()    # setup and teardown execution decorater
def setup_teardown():      #(o/p=  setup ,m1,teaddown  ,setup,  m2 ,teaddown , setup,  m3 ,teaddown )
    print("setup")
    yield
    print("tierdown")
def test_m1(setup_teardown):
    print("m1")
def test_m2(setup_teardown):
    print("m2")
def test_m3(setupt_eardown):
    print("m3")


@pytest.yield_fixture(scope="module")    # setup and teardown execution decorater
def setup_teardown_class():              #(o/p=  setup_class ,m1,  m2 ,m3 ,teaddown_class )
    print("setup_class")
    yield
    print("teardown_class")
def test_m1(setup_teardown_class):
    print("m1")
def test_m2(setup_teardown_class):
    print("m2")
def test_m3(setup_teardown_class):
    print("m3")




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