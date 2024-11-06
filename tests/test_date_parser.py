from datetime import datetime
from src.date_parser import DateManager

def test_from_string_valid_date():
    date_str = "12/25/2020"
    date_manager = DateManager.from_string(date_str)
    assert date_manager is not None
    assert date_manager.date == datetime(2020, 12, 25)

def test_from_string_invalid_date():
    date_str = "invalid date"
    date_manager = DateManager.from_string(date_str)
    assert date_manager is None

def test_from_string_european_date():
    date_str = "25/12/2020"
    date_manager = DateManager.from_string(date_str)
    assert date_manager is not None
    assert date_manager.date == datetime(2020, 12, 25)

def test_to_iso():
    date_manager = DateManager(datetime(2020, 12, 25))
    assert date_manager.to_iso() == "2020-12-25"

def test_to_us():
    date_manager = DateManager(datetime(2020, 12, 25))
    assert date_manager.to_us() == "12/25/2020"

def test_to_european():
    date_manager = DateManager(datetime(2020, 12, 25))
    assert date_manager.to_european() == "25/12/2020"

def test_to_long():
    date_manager = DateManager(datetime(2020, 12, 25))
    assert date_manager.to_long() == "December 25, 2020"

def test_to_short():
    date_manager = DateManager(datetime(2020, 12, 25))
    assert date_manager.to_short() == "Dec 25, 2020"