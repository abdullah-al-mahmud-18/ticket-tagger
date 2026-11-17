from ticket_tagger.text import clean_text


def test_normal_text():
    assert clean_text(" normaL   TeXt ") == "normal text"


def test_empty():
    assert clean_text("") == ""
