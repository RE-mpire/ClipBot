from src.line_parser import LineParser

parser = LineParser()

def test_remove_duplicate_lines():
    lines = '\n'.join(['foo', 'bar', 'foo', 'baz', 'bar'])
    parsed_lines = parser.remove_duplicates(lines)
    assert parsed_lines == 'foo\nbar\nbaz'
    
    lines = '\n'.join(['foo1', 'foo2', 'bar1', 'baz1'])
    parsed_lines = parser.remove_duplicates(lines)
    assert parsed_lines == 'foo1\nfoo2\nbar1\nbaz1'

    lines = ""
    parsed_lines = parser.remove_duplicates(lines)
    assert parsed_lines == ""

def test_remove_empty_lines():
    lines = '\n'.join(['foo', '', 'bar', 'baz', ''])
    parsed_lines = parser.strip_empty_lines(lines)
    assert parsed_lines == 'foo\nbar\nbaz'

    lines = '\n'.join(['foo', 'bar', 'baz'])
    parsed_lines = parser.strip_empty_lines(lines)
    assert parsed_lines == 'foo\nbar\nbaz'

    lines = ""
    parsed_lines = parser.strip_empty_lines(lines)
    assert parsed_lines == ""


def test_sort_lines():
    lines = '\n'.join(['foo', 'bar', 'baz'])
    parsed_lines = parser.sort_lines(lines)
    assert parsed_lines == 'bar\nbaz\nfoo'

    lines = '\n'.join(['1', '2', '3'])
    parsed_lines = parser.sort_lines(lines)
    assert parsed_lines == '1\n2\n3'

    lines = ""
    parsed_lines = parser.sort_lines(lines)
    assert parsed_lines == ""

def test_to_list():
    lines = '\n'.join(['foo', 'bar', 'baz'])
    parsed_lines = parser.to_list(lines)
    assert parsed_lines == 'foo\nbar\nbaz'

    lines = 'eggs, milk, bread'
    parsed_lines = parser.to_list(lines)
    assert parsed_lines == 'eggs\nmilk\nbread'

    lines = ""
    parsed_lines = parser.to_list(lines)
    assert parsed_lines == ""

def test_to_csv():
    lines = '\n'.join(['foo', 'bar', 'baz'])
    parsed_lines = parser.to_csv(lines)
    assert parsed_lines == 'foo, bar, baz'

    lines = 'eggs, milk, bread'
    parsed_lines = parser.to_csv(lines)
    assert parsed_lines == 'eggs, milk, bread'

    lines = ""
    parsed_lines = parser.to_csv(lines)
    assert parsed_lines == ""

