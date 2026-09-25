# Tic-Tac-Toe AI

A Python-based console Tic-Tac-Toe game developed using the **Minimax algorithm** as part of Task 2 of the **CodSoft Artificial Intelligence Internship**.

## 📌 Project Overview

This project is an interactive Tic-Tac-Toe game where a human player competes against an AI opponent.

The player uses **X**, while the AI uses **O**. The AI uses the **Minimax algorithm** to evaluate possible moves and select the best available move.

The project demonstrates the use of **game-playing algorithms, recursion, decision-making, and search techniques** in Artificial Intelligence.

## ✨ Features

* Human vs AI gameplay
* AI decision-making using the Minimax algorithm
* 3 × 3 Tic-Tac-Toe board
* Win detection for both player and AI
* Draw detection
* Input validation
* Prevention of moves on occupied positions
* Handling of invalid inputs
* Replay-ready game structure
* Replay option after each game
* Clear console-based interface

## 🧠 Minimax Algorithm

The **Minimax algorithm** is a decision-making algorithm commonly used in two-player games.

In this project:

* The AI (`O`) acts as the **maximizing player**.
* The human player (`X`) acts as the **minimizing player**.
* The algorithm explores possible future moves.
* Each possible game state receives a score.
* The AI selects the move with the highest possible score while assuming that the opponent will make the best possible counter-move.

### Scoring

```text
AI Win     → Positive score
Human Win  → Negative score
Draw       → 0
```

The algorithm also considers the depth of the game state so that the AI prefers faster wins and delays losses when possible.

## 🛠️ Technologies Used

* **Python 3**
* `math` module
* Functions
* Conditional statements
* Loops
* Recursion
* Lists
* Minimax algorithm
* Console input/output

## ⚙️ How It Works

1. The game initializes an empty 3 × 3 board.
2. The player is assigned `X`.
3. The AI is assigned `O`.
4. The player selects a position from 1 to 9.
5. The AI evaluates the available moves using Minimax.
6. The best move is selected by the AI.
7. The board is updated after each move.
8. The game checks for a win or draw after every move.
9. The game ends when either player wins or the board becomes full.
10. After the game ends, the player can choose to play another round or exit.

## ▶️ How to Run

### 1. Open the project folder

```text
Task-2-Tic-Tac-Toe-AI
```

### 2. Open the terminal

Make sure the terminal is inside the project folder.

### 3. Run the program

```bash
python tic_tac_toe.py
```

## 🎮 Board Positions

The player selects positions using the following layout:

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

For example, entering `1` places `X` in the top-left position.

## 📷 Sample Gameplay

```text
=============================================
        TIC-TAC-TOE AI
=============================================
You are X
AI is O

Board positions:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Your turn (X).
Enter your position (1-9): 1

AI is thinking...
```

The game continues until the player wins, the AI wins, or the match ends in a draw.

## 📁 Project Structure

```text
Task-2-Tic-Tac-Toe-AI
│
├── tic_tac_toe.py
└── README.md
```

## 🎯 Learning Outcome

Through this project, I learned how to implement a game-playing AI using the **Minimax algorithm** and gained practical understanding of recursion, game-state evaluation, decision-making, and search techniques in Artificial Intelligence.

## 🏆 Internship Task

**Task:** Task 2 – Tic-Tac-Toe AI
**Program:** CodSoft Artificial Intelligence Internship

## 👩‍💻 Author

**Renesa Pal**
