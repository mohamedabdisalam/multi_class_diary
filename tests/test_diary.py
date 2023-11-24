from lib.diary import *

def test_diary_initialises():
    diary = Diary("")
    assert isinstance(diary, Diary)

def test_time_to_read_diary():
    diary = Diary("one two three four")
    actual = diary.reading_time(4)
    expected = 1
    assert actual == expected

def test_give_a_chunk_of_text_that_we_can_read():
    diary = Diary("one two three four five")
    actual = diary.find_best_entry_for_reading_time(5, 1)
    expected = "one two three four five"
    assert expected == actual