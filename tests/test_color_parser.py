from src.color_parser import Color

def test_color_from_hex():
    color = Color.from_string("#ff5733")
    assert color is not None
    assert color.to_hex() == "#ff5733"
    assert color.to_rgb() == "rgb(255, 87, 51)"
    assert color.to_hsl() == "hsl(10.6, 100.0%, 60.0%)"

def test_color_from_rgb():
    color = Color.from_string("rgb(255, 87, 51)")
    assert color is not None
    assert color.to_hex() == "#ff5733"
    assert color.to_rgb() == "rgb(255, 87, 51)"
    assert color.to_hsl() == "hsl(10.6, 100.0%, 60.0%)"

def test_color_from_hsl():
    color = Color.from_string("hsl(14, 100%, 60%)")
    assert color is not None
    assert color.to_hex() == "#ff6232"
    assert color.to_rgb() == "rgb(255, 98, 50)"
    assert color.to_hsl() == "hsl(14.0, 100.0%, 60.0%)"

def test_invalid_color_string():
    color = Color.from_string("invalid color")
    assert color is None

def test_partial_hex():
    color = Color.from_string("#ff573")
    assert color is None

def test_partial_rgb():
    color = Color.from_string("rgb(255, 87)")
    assert color is None

def test_partial_hsl():
    color = Color.from_string("hsl(14, 100%)")
    assert color is None