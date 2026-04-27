from pathlib import Path
from logic_utils import check_guess, get_range_for_difficulty

STRATEGY_PATH = Path(__file__).parent / "strategy.txt"


def load_strategy() -> str:
    return STRATEGY_PATH.read_text(encoding="utf-8")


def clamp_guess(guess: int, low: int, high: int) -> int:
    return max(low, min(high, guess))


def binary_search_guess(current_low: int, current_high: int) -> tuple[int, str]:
    guess = (current_low + current_high) // 2
    reasoning = (
        f"Range is {current_low} to {current_high}. "
        f"Midpoint: ({current_low} + {current_high}) // 2 = {guess}."
    )
    return guess, reasoning


def run_full_agent_game(secret: int, difficulty: str) -> list[dict]:
    low, high = get_range_for_difficulty(difficulty)
    current_low = low
    current_high = high
    results = []

    for _ in range(20):
        guess, reasoning = binary_search_guess(current_low, current_high)
        guess = clamp_guess(guess, current_low, current_high)
        outcome, hint_message = check_guess(guess, secret, low, high)

        results.append(
            {
                "guess": guess,
                "reasoning": reasoning,
                "outcome": outcome,
                "hint": hint_message,
            }
        )

        if outcome == "Win":
            break

        if outcome == "Too High":
            current_high = guess - 1
        elif outcome == "Too Low":
            current_low = guess + 1

        if current_low > current_high:
            break

    return results
