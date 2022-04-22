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
        assert 2+2 == 4

    def test_2(self):
        assert 2+2 == 5, f"Ошибка при сложении"

    def test_3(self):
        assert 2+2 == 4
        assert 2+2 == 5, "Ошибка при сложении"


    def test_4(self):
        assert 1/0 == 1, f"Равенство не выполняется"


