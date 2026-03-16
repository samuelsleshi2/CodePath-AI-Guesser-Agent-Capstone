# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The point of the game is to guess the right number before you run out of guesses] Describe the game's purpose.
- [I found several bugs, some of which include no correct answer being present, the ranges being mixed up, and the session state being messed up when trying to start a new game.] Detail which bugs you found.
- [I fixed the ranges to make them accurate to the game difficulty, I fixed the session bugs, I made sure the secret was possible to guess in each of the game difficulties, I fixed the error where the enter button wasn't submitting a guess, and I made sure that the hints were accurate.] Explain what fixes you applied.

## 📸 Demo

- [![alt text](image.png)] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
