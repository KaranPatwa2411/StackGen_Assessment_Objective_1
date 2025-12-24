# Intent-Based Query Router

A simple query routing system that directs user questions to the correct agent (GitHub vs. Linear) based on keyword intent.

## Setup Instructions

**Clone the repository:**
 ```bash
 git clone https://github.com/KaranPatwa2411/StackGen_Assessment_Objective_1.git
```

**Navigate to the project directory:**

```bash
cd StackGen_Assessment_Objective_1
```

**Prerequisites:**

Python 3.6 or higher.

No external libraries are required (uses standard library only).

## How to Run

1. **Interactive Mode** (Chatbot):
```bash
python main.py

```

2. **Programmatic Demo** (Pre-defined queries):
```bash
python example.py

```


3. **Run Unit Tests**:
```bash
python test.py

```



## Assumptions & Design Decisions

To keep the implementation simple while ensuring correctness, the following design decisions were made:

1. **Keyword Scoring Logic:**
Intent is determined by a scoring system. The router counts how many distinct keywords from an agent appear in the query, and the agent with the highest score wins.
2. **Substring Matching:**
Matching is based on simple substrings. This avoids complex Regex or NLP dependencies while maintaining simplicity.
3. **Tie-Breaking Strategy:**
If two agents have the same score, the **first agent** in the initialization list is selected.


4. **Mocked Responses:**
As no real API integrations were required, agents return simple, hard-coded string responses to verify that routing was successful.

## Project Structure

* `main.py`: Entry point for the interactive CLI and central agent configuration.
* `example.py`: Script demonstrating specific programmatic use cases.
* `router.py`: Contains the `QueryRouter` class and intent scoring logic.
* `agents.py`: Contains `GitHubAgent` and `LinearAgent` classes.
* `test.py`: Unit tests for routing logic and edge cases.
