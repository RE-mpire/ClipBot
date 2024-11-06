from src.text_analyzer import TextAnalyzer

def test_count_words():
    assert TextAnalyzer.count_words("Hello world") == 2
    assert TextAnalyzer.count_words("") == 0
    assert TextAnalyzer.count_words("One") == 1

def test_count_chars():
    assert TextAnalyzer.count_chars("Hello world") == {
        'total': 11,
        'no_spaces': 10,
        'no_whitespace': 10
    }
    assert TextAnalyzer.count_chars("") == {
        'total': 0,
        'no_spaces': 0,
        'no_whitespace': 0
    }
    assert TextAnalyzer.count_chars(" a b c ") == {
        'total': 7,
        'no_spaces': 3,
        'no_whitespace': 3
    }

def test_line_count():
    assert TextAnalyzer.line_count("Hello\nworld") == 2
    assert TextAnalyzer.line_count("") == 0
    assert TextAnalyzer.line_count("One") == 1

def test_count_paragraphs():
    assert TextAnalyzer.count_paragraphs("Hello\n\nworld") == 2
    assert TextAnalyzer.count_paragraphs("") == 0
    assert TextAnalyzer.count_paragraphs("One") == 1

def test_count_sentences():
    assert TextAnalyzer.count_sentences("Hello. World.") == 2
    assert TextAnalyzer.count_sentences("") == 0
    assert TextAnalyzer.count_sentences("One") == 1
    assert TextAnalyzer.count_sentences("...") == 1

def test_read_time():
    sentence = "a "
    assert TextAnalyzer.read_time(sentence) == "Less than a minute"
    sentence *= 180
    assert TextAnalyzer.read_time(sentence) == "1 minute"
    sentence += "a"
    assert TextAnalyzer.read_time(sentence) == "1 minute"
    sentence *= 2
    assert TextAnalyzer.read_time(sentence) == "2 minutes"

