from live_content_parser import main


def test__main__happy_path():
    assert main.main() == 0
