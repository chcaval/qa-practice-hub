import pytest

@pytest.fixture
def numbers():
    data = [1,2,3]
    
    yield data # test get here
    
    print("\n--- SETUP: creating list ---")
    data.clear()
    
def test_first_number(numbers):
    assert numbers[0] == 1
    
def test_list_length(numbers):
    assert len(numbers) == 3
    
    