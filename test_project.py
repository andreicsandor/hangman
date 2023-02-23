from project import fetch_words, find_indexes, validate_name


def test_fetch_words():
    # Test function for length of list
    assert len(fetch_words(1, 1)) == 3
    # Test function for length of shorter list item
    assert 4 <= len(fetch_words(1, 2)[0]) <= 7
    # Test function for length of longer list item
    assert 8 <= len(fetch_words(2, 2)[0]) <= 15


# Test function for validity of matched character's index
def test_find_indexes():
    assert find_indexes("testing", "e") == [1]
    assert find_indexes("CS50", "P") == []


# Test function for user's name validation
def test_validate_name():
    assert validate_name("50") == False
    assert validate_name("Muppet") == True
    