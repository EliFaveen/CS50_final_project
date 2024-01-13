from project import search_name,char_age,check_correct_args
import pytest
import datetime

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()

def test_search_name():
#     sys.argv[1] = "wizards.cs"
#     assert search_name("lily") == "Lily Potter house is Gryffindor"
#     assert search_name("LiLy") == "Lily Potter house is Gryffindor"
#     assert search_name("bob") == "no character found"
#     assert search_name("Draco") == "Draco Malfoy house is Slytherin"
    with pytest.raises(SystemExit):
        search_name("e")

def test_char_age():
    today = datetime.date.today()
    year = today.year
    age = year - 2005
    assert char_age(2005) == age
    age = year - 2015
    assert char_age(2015) == age

