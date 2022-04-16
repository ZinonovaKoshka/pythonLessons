import pytest

@pytest.fixture(scope="class", autouse=True)
def resource_setup_start():
    print("FirstTest class started")
    yield
    print("All tests in FirstTest finished")

@pytest.fixture(scope="function", autouse=True)
def resource_setup():
    print("Test start")
    yield  # Все что до ключевого слова yield выполнится до теста, а то что после выполнится после теста
    print("Test finished")


class TestFirst:

    def test_1(self):
        print("Test №1")

    def test_2(self):
        print("Test №2")

    def test_3(self):
        print("Test №3")



