# Rock Paper Scissors (Python)

A simple, interactive command-line implementation of the classic **Rock, Paper, Scissors** game built with Python.

## 🎮 Features
* **Interactive Menu:** Easy navigation to play, check scores, or reset.
* **Score Tracking:** Keeps track of Player wins, Computer wins, and Ties during the session.
* **Input Validation:** Handles typos and invalid choices gracefully.
* **Dictionary Logic:** Uses an efficient mapping system to determine winners.

## 🛠️ Requirements
* **Python 3.x**

## 🚀 How to Run
1.  **Clone the repository** (or download the script):
    ```bash
    git clone https://github.com/akramraza007/rock_paper_scissors.git
    ```
2.  **Navigate to the folder**:
    ```bash
    cd rock_paper_scissors
    ```
3.  **Run the game**:
    ```bash
    python rock_paper_scissors.py
    ```

## 🕹️ How to Play
1.  Run the script to open the main menu.
2.  Select **Option 1** to start a round.
3.  Type your move: `Rock`, `Paper`, or `Scissor`.
4.  The computer will randomly select its move, and the winner will be announced!
5.  Check your total stats by selecting **Option 2**.

## 🧠 Game Rules
The winner is decided based on these standard rules:
* **Rock** smashes **Scissor**
* **Paper** covers **Rock**
* **Scissor** cuts **Paper**

## 🖥️ Sample Output

Here is a look at a typical gameplay session in the terminal:

```text
🎮 Welcome to Rock, Paper, Scissor Pro!

--- MENU ---
1. Play a Round 🕹️
2. View Scores 📊
3. Reset Scores 🔄
4. Exit to Chatbot 🚪
Select an option (1-4): 1

Enter Rock, Paper, or Scissor: Rock
🤖 Computer is thinking...
Result: Rock vs Scissor
🎉 You Win! Rock beats Scissor.

--- MENU ---
1. Play a Round 🕹️
2. View Scores 📊
3. Reset Scores 🔄
4. Exit to Chatbot 🚪
Select an option (1-4): 1

Enter Rock, Paper, or Scissor: Paper
🤖 Computer is thinking...
Result: Paper vs Scissor
💀 Computer Wins! Scissor beats Paper.

--- MENU ---
1. Play a Round 🕹️
2. View Scores 📊
3. Reset Scores 🔄
4. Exit to Chatbot 🚪
Select an option (1-4): 2

🏆 --- SCOREBOARD ---
👤 User Score: 1
🤖 Comp Score: 1
🤝 Ties: 0
---------------------

--- MENU ---
1. Play a Round 🕹️
2. View Scores 📊
3. Reset Scores 🔄
4. Exit to Chatbot 🚪
Select an option (1-4): 4
Are you sure you want to exit the game? (y/n): y
Thanks for playing the game...👋
```