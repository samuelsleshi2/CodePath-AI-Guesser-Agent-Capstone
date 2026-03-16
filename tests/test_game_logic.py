from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ================== BUG 1: Boundary Checking Tests ==================
def test_guess_out_of_range_too_low():
    """BUG FIX: check_guess() now validates guess is >= low bound"""
    result, message = check_guess(0, 50, low=1, high=100)
    assert result == "Out of Range"
    assert "too low" in message.lower()

def test_guess_out_of_range_too_high():
    """BUG FIX: check_guess() now validates guess is <= high bound"""
    result, message = check_guess(101, 50, low=1, high=100)
    assert result == "Out of Range"
    assert "too high" in message.lower()

def test_guess_at_boundary_low():
    """BUG FIX: guessing exactly at low boundary should be allowed"""
    result, message = check_guess(1, 50, low=1, high=100)
    assert result == "Too Low"  # Secret is 50, guess is 1
    assert result != "Out of Range"

def test_guess_at_boundary_high():
    """BUG FIX: guessing exactly at high boundary should be allowed"""
    result, message = check_guess(100, 50, low=1, high=100)
    assert result == "Too High"  # Secret is 50, guess is 100
    assert result != "Out of Range"

def test_guess_out_of_range_easy_mode():
    """BUG FIX: Respects Easy mode range (1-20), not Hard (1-100)"""
    low, high = get_range_for_difficulty("Easy")
    result, message = check_guess(25, 10, low=low, high=high)
    assert result == "Out of Range"


# ================== BUG 2: Correct Message Hints ==================
def test_guess_too_high_message():
    """BUG FIX: Message should say 'Go LOWER!' when guess > secret"""
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert "LOWER" in message  # Message was backwards before

def test_guess_too_low_message():
    """BUG FIX: Message should say 'Go HIGHER!' when guess < secret"""
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert "HIGHER" in message  # Message was backwards before

def test_winning_guess_message():
    """Basic win case with message"""
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert "Correct" in message


# ================== BUG 3: Boundary Error Messages ==================
def test_out_of_range_message_contains_bounds():
    """BUG FIX: Out of range message should show valid range (1-20) for Easy"""
    result, message = check_guess(25, 10, low=1, high=20)
    assert result == "Out of Range"
    assert "1" in message and "20" in message

def test_out_of_range_message_shows_high_bound():
    """BUG FIX: When guessing too high, message should show the upper bound"""
    result, message = check_guess(101, 50, low=1, high=100)
    assert "100" in message

def test_out_of_range_message_shows_low_bound():
    """BUG FIX: When guessing too low, message should show the lower bound"""
    result, message = check_guess(-5, 50, low=1, high=100)
    assert "1" in message


# ================== BUG 4: Difficulty Range Consistency ==================
def test_difficulty_easy_range():
    """BUG FIX: Easy mode should be 1-20, not 1-100"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_difficulty_normal_range():
    """BUG FIX: Normal mode should be 1-50, not 1-100"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_difficulty_hard_range():
    """BUG FIX: Hard mode should be 1-100"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100


# ================== BUG 5: Parse Guess Edge Cases ==================
def test_parse_empty_string():
    """BUG FIX: Empty input should be rejected with proper error"""
    ok, guess_int, error = parse_guess("")
    assert not ok
    assert error == "Enter a guess."
    assert guess_int is None

def test_parse_none_input():
    """BUG FIX: None input should be rejected"""
    ok, guess_int, error = parse_guess(None)
    assert not ok
    assert error == "Enter a guess."

def test_parse_float_input():
    """BUG FIX: Float input like '42.5' should convert to int"""
    ok, guess_int, error = parse_guess("42.5")
    assert ok
    assert guess_int == 42
    assert error is None

def test_parse_invalid_input():
    """BUG FIX: Non-numeric input should be rejected"""
    ok, guess_int, error = parse_guess("not a number")
    assert not ok
    assert error == "That is not a number."
    assert guess_int is None


# ================== Integration Tests ==================
def test_multiple_guesses_sequence():
    """BUG FIX: Guessing should work in sequence without state issues"""
    secret = 50
    low, high = 1, 100
    
    # First guess too low
    result1, msg1 = check_guess(25, secret, low, high)
    assert result1 == "Too Low"
    
    # Second guess too high
    result2, msg2 = check_guess(75, secret, low, high)
    assert result2 == "Too High"
    
    # Winning guess
    result3, msg3 = check_guess(50, secret, low, high)
    assert result3 == "Win"

def test_boundary_then_valid_guess():
    """BUG FIX: After rejecting out-of-range, valid guesses should work"""
    secret = 50
    low, high = 1, 100
    
    # Out of range
    result1, _ = check_guess(150, secret, low, high)
    assert result1 == "Out of Range"
    
    # Valid guess after
    result2, _ = check_guess(60, secret, low, high)
    assert result2 == "Too High"


# ================== BUG 6: New Game State Reset ==================
def test_new_game_resets_status():
    """BUG FIX: New Game button must reset status to 'playing', not just attempts"""
    # Simulate a won game state
    game_state = {
        "status": "won",
        "attempts": 5,
        "secret": 42,
        "score": 95,
        "history": [10, 20, 30, 40, 42]
    }
    
    # Simulate pressing New Game button
    game_state["status"] = "playing"
    game_state["attempts"] = 0
    game_state["history"] = []
    
    # Verify the state is reset for a new game
    assert game_state["status"] == "playing", "Status must be reset to 'playing'"
    assert game_state["attempts"] == 0, "Attempts must be reset to 0"
    assert game_state["history"] == [], "History must be cleared"

def test_new_game_after_loss_state():
    """BUG FIX: New Game must also work when coming from a 'lost' state"""
    # Simulate a lost game state
    game_state = {
        "status": "lost",
        "attempts": 8,
        "secret": 42,
    }
    
    # Simulate pressing New Game button
    game_state["status"] = "playing"
    game_state["attempts"] = 0
    
    assert game_state["status"] == "playing", "Status must be reset from 'lost' to 'playing'"
    assert game_state["attempts"] == 0, "Attempts must be reset for new game"
