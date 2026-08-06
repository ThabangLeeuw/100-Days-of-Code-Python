# Higher or Lower Game 🎮

A simple Python console game inspired by the "Higher or Lower" concept.  
Players guess which celebrity, brand, or entity has more followers based on randomly selected data.

---

## 📌 Project Overview
The game randomly selects two entries from a dataset (`game_data.data`) and displays their:
- **Name**
- **Description**
- **Country**

The player must guess which one has more followers.  
Correct guesses increase the score, while an incorrect guess ends the game.

---

## 🛠️ Features
- Randomized comparisons using Python’s `random.choice`.
- ASCII art for a fun visual experience (`art.logo` and `art.vs`).
- Score tracking until the player makes a wrong guess.
- Beginner-friendly code structure with functions for clarity.

---

## 📂 Project Structure
higher_lower/

│── art.py            # Contains ASCII art (logo and vs)
│── game_data.py       # Contains dataset with names, descriptions, countries, follower counts
│── main.py            # Main game logic
│── README.md          # Project documentation

## 👨‍💻 Author
Created by Imraan Thabang Leeuw
