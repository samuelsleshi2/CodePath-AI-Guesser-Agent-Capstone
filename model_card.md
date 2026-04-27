## Responsible AI Reflection

**What are the limitations or biases in your system?**

The agent's biggest limitation is also its defining feature: it only knows what `strategy.txt` tells it. It has no intuition, no emotional reasoning, and no ability to draw on experience outside of the formula it was given. A human player might guess a number they have a feeling about, notice a pattern from a previous game, or take a risk based on context. The agent cannot do any of that. It always starts from the midpoint, always updates its bounds mechanically, and always follows the same path for the same secret. That consistency is a strength for reliability, but it is a limitation when it comes to flexibility or creativity.

**Could your AI be misused, and how would you prevent that?**

This particular agent cannot be meaningfully misused. Its instructions are to stay within a defined integer range and follow binary search rules — there is no mechanism for it to do anything outside of that scope. The guardrails built into `clamp_guess` and `check_guess` make it structurally impossible for the agent to guess out of bounds or submit a non-integer. The agent is constrained by both its instructions and its code, so misuse is not a realistic concern here.

**What surprised you while testing your AI's reliability?**

The most surprising result was that the AI was not always more efficient than a human. Before testing, the assumption was that a systematic algorithm would always outperform a random guesser. In reality, a human can get lucky and guess the secret on the first try, while the agent always needs at least a few rounds because it has to narrow down from the midpoint. The AI is more *reliable* — it will never take more than 7 guesses on Hard — but it is not always *faster*. That distinction between reliability and speed was not obvious going in.

**Describe your collaboration with AI during this project.**

AI was used throughout this project as a development collaborator. The most helpful suggestion was the binary search implementation itself — the idea of using `strategy.txt` as a knowledge base to define the algorithm and guardrails (stay within the difficulty range, only guess integers) gave the project a clear structure and made the agent's behavior predictable and testable. There were no harmful or dangerous suggestions during development.