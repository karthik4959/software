from word import WordCounter

wordcounter = WordCounter

# Test case for the uppercase count function
def test_count_uppercase():
    text = "Hello, World" # Input for the test
    expected_result = 3 # Expected result
    result = wordcounter.count_uppercase(text)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"