# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It had an option to guess a correct number, with a submit button. There was a hint provided to either guess higher or lower. There was also a sidebar to select game difficulty

- List at least two concrete bugs you noticed at the start  

The enter button doesn't work to submit a guess, I thought it would work. Also, the game will tell you to keep going higher or lower even if you have reached the min/max limits, I thought there would eventually be a correct answer or the game would stop you once you guess a number past one of the limits. There also does not seem to be a correct answer at all, I have never gotten a correct guess

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI suggested that I use st.form() with form_submit_button to make sure the submissions for the guesses registered correctly. I verified this by adding it to the code and then running the project and trying it out and it worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI told me to run tests with pytest tests, but that didn't work because I needed to tell my compiler to look for the module named "pytest". So eventually when I ran python -m pytest tests the tests finally ran properly without a module error.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

By running the project and testing out what was causing the bug. If it works fine, it is fixed, if there is even something slightly off, it is not fixed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

One test makes sure that the game starts a new game after losing. It sets status to playing, attempts to 0, then asserts that status equals playing and attempts equals 0. This showed me that my code was able to manage states properly, and that the game understands the difference between a new game from winning and from losing.

- Did AI help you design or understand any tests? How?

It helped me design that test I just described. I understood the concept of what needed to be tested, I just didn't get the syntax, since I am used to testing in Java, not Python. So Copilot was able to help me get my idea down onto the code.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
