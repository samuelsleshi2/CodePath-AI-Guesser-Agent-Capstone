from ai_agent import clamp_guess, load_strategy, binary_search_guess, run_full_agent_game


# ================== clamp_guess ==================

def test_clamp_within_range():
    assert clamp_guess(50, 1, 100) == 50

def test_clamp_too_low_snaps_to_low():
    assert clamp_guess(0, 1, 100) == 1

def test_clamp_too_high_snaps_to_high():
    assert clamp_guess(150, 1, 100) == 100

def test_clamp_at_boundary_low():
    assert clamp_guess(1, 1, 100) == 1

def test_clamp_at_boundary_high():
    assert clamp_guess(100, 1, 100) == 100

def test_clamp_easy_mode_range():
    assert clamp_guess(25, 1, 20) == 20


# ================== load_strategy ==================

def test_load_strategy_returns_nonempty_string():
    content = load_strategy()
    assert isinstance(content, str)
    assert len(content) > 100

def test_load_strategy_contains_binary_search():
    content = load_strategy()
    assert "binary search" in content.lower()

def test_load_strategy_contains_all_difficulties():
    content = load_strategy()
    assert "Easy" in content
    assert "Normal" in content
    assert "Hard" in content

def test_load_strategy_contains_integer_rule():
    content = load_strategy()
    assert "integer" in content.lower() or "INTEGER" in content


# ================== binary_search_guess ==================

def test_binary_search_guess_hard_first_guess():
    guess, _ = binary_search_guess(1, 100)
    assert guess == 50

def test_binary_search_guess_normal_first_guess():
    guess, _ = binary_search_guess(1, 50)
    assert guess == 25

def test_binary_search_guess_easy_first_guess():
    guess, _ = binary_search_guess(1, 20)
    assert guess == 10

def test_binary_search_guess_floor_division():
    # (26 + 50) // 2 = 38, not 38.0
    guess, _ = binary_search_guess(26, 50)
    assert guess == 38
    assert isinstance(guess, int)

def test_binary_search_guess_single_value():
    guess, _ = binary_search_guess(37, 37)
    assert guess == 37

def test_binary_search_guess_reasoning_contains_bounds():
    _, reasoning = binary_search_guess(26, 50)
    assert "26" in reasoning and "50" in reasoning

def test_binary_search_guess_reasoning_contains_result():
    guess, reasoning = binary_search_guess(1, 100)
    assert str(guess) in reasoning


# ================== run_full_agent_game ==================

def test_run_full_agent_game_wins_hard():
    results = run_full_agent_game(secret=50, difficulty="Hard")
    assert results[-1]["outcome"] == "Win"

def test_run_full_agent_game_wins_easy():
    results = run_full_agent_game(secret=10, difficulty="Easy")
    assert results[-1]["outcome"] == "Win"

def test_run_full_agent_game_wins_normal():
    results = run_full_agent_game(secret=37, difficulty="Normal")
    assert results[-1]["outcome"] == "Win"

def test_run_full_agent_game_last_guess_equals_secret():
    results = run_full_agent_game(secret=42, difficulty="Hard")
    assert results[-1]["guess"] == 42

def test_run_full_agent_game_result_has_required_keys():
    results = run_full_agent_game(secret=50, difficulty="Hard")
    for step in results:
        assert "guess" in step
        assert "reasoning" in step
        assert "outcome" in step
        assert "hint" in step

def test_run_full_agent_game_guesses_stay_in_range_hard():
    results = run_full_agent_game(secret=1, difficulty="Hard")
    for step in results:
        assert 1 <= step["guess"] <= 100

def test_run_full_agent_game_guesses_stay_in_range_easy():
    results = run_full_agent_game(secret=15, difficulty="Easy")
    for step in results:
        assert 1 <= step["guess"] <= 20

def test_run_full_agent_game_max_guesses_hard():
    # Binary search on 1-100 always solves in at most 7 guesses
    for secret in [1, 2, 50, 99, 100]:
        results = run_full_agent_game(secret=secret, difficulty="Hard")
        assert len(results) <= 7

def test_run_full_agent_game_max_guesses_normal():
    for secret in [1, 25, 50]:
        results = run_full_agent_game(secret=secret, difficulty="Normal")
        assert len(results) <= 6

def test_run_full_agent_game_max_guesses_easy():
    for secret in [1, 10, 20]:
        results = run_full_agent_game(secret=secret, difficulty="Easy")
        assert len(results) <= 5

def test_run_full_agent_game_reasoning_nonempty():
    results = run_full_agent_game(secret=50, difficulty="Hard")
    for step in results:
        assert len(step["reasoning"]) > 0
