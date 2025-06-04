# 🃏 War Card Game (Python)

This is a simple Python implementation of the classic **"War" card game** for two players. The game is played using a standard 52-card deck, and each round players draw cards to battle it out — highest card wins! If cards are tied, a "war" occurs!

---

## 📦 Features

- Object-oriented design using classes for `Card`, `Deck`, and `Player`
- Implements game logic with shuffling, drawing, war mechanics
- Game ends when one player runs out of cards or max rounds are reached
- Prevents infinite loops with a `MAX_ROUNDS` limit

---

## 🧠 Game Rules (Simplified)

- Both players draw one card per round.
- The player with the higher card value wins the round and takes both cards.
- If values tie, a "war" happens:
  - Each player places 5 cards face-down and draws one face-up.
  - The face-up cards are compared again.
  - Winner takes all cards on the table.
- Game continues until one player runs out of cards or max rounds reached.

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Save the code in a file called `war_game.py`.
3. Run the game from your terminal:

```bash
python war_game.py
````

---

## 📄 Code Structure

### `Card` class

Represents a playing card with suit, rank, and value.

### `Deck` class

Creates and shuffles the 52-card deck and deals cards.

### `Player` class

Manages each player’s hand and card operations (add/remove).

### Main Game Loop

Handles the game logic, round progression, war declaration, and victory conditions.

---

## 📈 Sample Output

```
Round 1  
Round 2  
WAR!  
Player One unable to declare war  
Player Two Wins!!  
```

---

## 🛑 Limitations

* Infinite loop protection via `MAX_ROUNDS = 10000`
* Doesn't handle UI or multiplayer input — strictly CLI
* Not suitable for production; intended for learning and simulation

---

## ✅ Possible Improvements

* Add GUI or web interface
* Allow user input for player names or moves
* Improve war logic for edge cases
* Add round-by-round logging or replay functionality

---

## 💡 Inspired By

This is based on the traditional "War" card game played with physical cards. It's a fun way to apply Python OOP concepts!

---
