# Guessing Game

## Original Project

This project started as **Game Glitch Investigator**, a number guessing game built in Modules 1–3. The original game was intentionally shipped with bugs: incorrect hints, a secret number that reset on every submission, hardcoded ranges that ignored the selected difficulty, and a broken Enter key submission. The goal was to find and fix those bugs, separate game logic into a testable module, and get a full pytest suite passing.

---

## Title and Summary

**Guessing Game** is a number guessing game with two ways to play: manually, where you submit guesses and receive hints, or automatically, where a built-in AI agent solves the game for you using binary search. The project exists to answer a simple question — can a programmatic strategy consistently outperform a random human guesser? It turns out the answer is yes on efficiency, but never on certainty, because the secret number is always random.

---

## Architecture Overview

The system has four main layers:

- **Streamlit UI (`app.py`)** — handles difficulty selection, session state, the manual guess form, and the AI agent trigger button.
- **Game Logic (`logic_utils.py`)** — pure Python functions for parsing guesses, validating boundaries, comparing to the secret, and updating the score. No UI code lives here.
- **AI Agent (`ai_agent.py`)** — reads `strategy.txt` as its knowledge base, then runs a binary search loop. Each round it calculates a midpoint, clamps it to the valid range as a guardrail, submits the guess to `check_guess`, updates its bounds based on the hint, and repeats until it wins.
- **Knowledge Base (`strategy.txt`)** — a plain text file that defines the binary search algorithm, per-difficulty ranges, and the rules the agent must follow (integers only, stay in range, no repeats, use floor division). This is the RAG component: the agent is implemented to follow these rules exactly.

The flow is: user selects difficulty → secret is generated → user clicks "Let AI Play" or submits guesses manually → game logic evaluates each guess → hints feed back into the next decision → full history displayed at the end.

---

## Setup

**Requirements:** Python 3.10+

```bash
# 1. Clone the repository
git clone https://github.com/samuelsleshi2/CodePath-AI-Guesser-Agent-Capstone.git
cd CodePath-AI-Guesser-Agent-Capstone

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python -m streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

To run the test suite:

```bash
python -m pytest tests/ -v
```

---

## Sample Interactions

### Example 1 — AI Agent on Hard difficulty (range 1–100, secret = 73)

User selects **Hard** and clicks **Let AI Play**.

| Round | Guess | Result   |
|-------|-------|----------|
| 1     | 50    | Too Low  |
| 2     | 75    | Too High |
| 3     | 62    | Too Low  |
| 4     | 68    | Too Low  |
| 5     | 71    | Too Low  |
| 6     | 73    | Win      |

The secret number is **73**. Each round also shows the agent's reasoning, for example:
> "Range is 51 to 100. Midpoint: (51 + 100) // 2 = 75."

---

### Example 2 — AI Agent on Easy difficulty (range 1–20, secret = 2)

The secret number is **2**. User selects **Easy** and clicks **Let AI Play**.

| Round | Guess | Result   |
|-------|-------|----------|
| 1     | 10    | Too High |
| 2     | 5     | Too High |
| 3     | 2     | Win      |

The agent reads the Easy mode range (1–20) from `strategy.txt` and solves it in 3 guesses.

---

### Example 3 — Manual play on Normal difficulty (range 1–50, secret = 36)

The secret number is **36**. User selects **Normal**, types guesses into the form, and receives hints:

- Guess `25` → "Go HIGHER!"
- Guess `40` → "Go LOWER!"
- Guess `33` → "Go HIGHER!"
- Guess `36` → Correct!

---

## Design Decisions

The main design decision was giving the user both modes — manual and AI — in the same game so you can directly compare them. Playing manually shows how quickly a random approach runs out of guesses. Watching the AI play shows how a structured strategy handles the same problem in far fewer rounds.

The agent was built without an external AI API by design. Binary search is a deterministic algorithm: it does not need a language model to reason about midpoints. Instead, `strategy.txt` acts as the documented specification that the Python code follows exactly. This keeps the project free to run, fully testable, and honest about what the "AI" is actually doing.

The trade-off is that the agent has no adaptability — it always uses binary search regardless of any pattern in the secret numbers. That is the right trade-off here because the secret is always randomly generated, so there is no pattern to exploit.

---

## Testing Summary

The test suite covers 48 cases across two files:

- `tests/test_game_logic.py` — validates boundary checking, hint correctness, difficulty ranges, input parsing, and multi-step guess sequences.
- `tests/test_ai_agent.py` — validates the binary search midpoint calculation, clamping guardrails, strategy file loading, reasoning text output, and end-to-end game runs for all three difficulties.

What worked well: separating game logic from the UI made every core behavior unit-testable without needing to interact with Streamlit at all. The binary search tests are entirely deterministic, so they never flake.

What did not work as expected: the original goal was for the AI to be strictly more efficient than a human player. In practice, the agent is more *consistent* — it always solves the game in at most 7 guesses on Hard — but a lucky human can win in 1 guess. Because the secret is random, no algorithm can guarantee fewer guesses than a lucky random pick. The best a strategy can do is minimize the worst case, not beat every outcome.

---

## Reflection

This project taught me that AI is very good at following instructions. The `strategy.txt` file is essentially a specification, and the agent executes it perfectly every time. But "following instructions perfectly" is not the same as "being better than humans." A human can guess randomly and win on the first try. The agent never will, because it always starts from the midpoint.

That gap — between optimal strategy and unpredictable outcome — is something I did not expect going in. It changed how I think about AI systems: they are powerful tools for enforcing consistent, well-defined behavior, but they operate within the same constraints of uncertainty that everything else does. When the input is random, even a perfect algorithm cannot guarantee a perfect result.

## Loom Walkthrough Link:
https://www.loom.com/share/ac961de819b140b9af4dd948d8bcdb5c