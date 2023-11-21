from .config import Config


def test_config():
    conf = Config("test.json")

    assert conf.fruit == "Apple"
    assert conf.size == "Large"
    assert conf.color == "Red"
