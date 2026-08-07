# Python Coding Tasks and Python Mini Projects

A collection of Python programming exercises completed through **Codewars**, alongside two terminal-based mini games: a **Mini Bingo Game** and a **Mini Guessing Game**. These projects were created to strengthen problem-solving skills, Python fundamentals, and object-oriented programming through practical application.

---

## Contents

* Requirements
* Installation
* Usage
* Project Structure
* Overview
* Features
* Example Gameplay
* Notes
* Future Improvements
* Licence

---

## Requirements

* **Python:** Version 3.8 or later (Python 3.6+ may also work, but Python 3.8+ is recommended)
* **Recommended IDE:** PyCharm (although any Python-compatible IDE or text editor can be used)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Python_Coding_Tasks_and_Python_Mini_Project
```

---

## Usage

Run the Codewars practice file:

```bash
python Codewars_Practice.py
```

Run the Mini Bingo Game:

```bash
python Mini_Bingo_Game.py
```

Run the Mini Guessing Game:

```bash
python Mini_Guessing_Game.py
```

> **Note:** Most Codewars solutions are designed to be called individually rather than executed directly. All completed kata solutions have passed the official Codewars test suite.

---

## Project Structure

```text
Python_Coding_Tasks_and_Python_Mini_Project/
│
├── Codewars_Practice.py       # Collection of Codewars kata solutions
├── Mini_Bingo_Game.py         # Terminal-based Bingo game
├── Mini_Guessing_Game.py      # Terminal-based number guessing game
├── README.md
└── LICENSE
```

---

## Overview

This repository serves as a personal Python practice project aimed at improving:

* Problem-solving skills
* Python programming fundamentals
* Writing clean and modular code
* Object-oriented programming
* Algorithmic thinking
* User input validation and control flow

It combines coding challenge solutions from Codewars with small interactive terminal games that demonstrate practical Python development and reinforce core programming concepts.

---

## Features

### 🧩 Codewars Practice (`Codewars_Practice.py`)

A growing collection of Python solutions covering a wide range of programming concepts.

#### 🔹 8 kyu – Python Fundamentals

Includes exercises involving:

* String manipulation
* Basic arithmetic
* Conditional logic
* Dictionary usage
* Simple classes (e.g. `Hero`, `User`)
* Beginner algorithms

#### 🔹 7 kyu – Intermediate Programming

Includes topics such as:

* Number and digit manipulation
* Array and list transformations
* String parsing
* Mathematical algorithms
* Binary conversion
* Data validation and filtering

#### 🔹 6 kyu – Advanced Problem Solving

Includes more complex programming challenges involving:

* Pattern matching and encoding (`duplicate_encode`)
* Queue simulations
* Sorting and reconstruction algorithms
* Binary parity checking
* Chessboard validation and FEN conversion
* Custom data structures (e.g. `WordDictionary`, `Potion`, `Robot`)

---

### 🎮 Mini Bingo Game (`Mini_Bingo_Game.py`)

A terminal-based interactive Bingo simulation where users can customise the game before playing.

#### Features

* Choose the bingo card size
* Select the range of possible numbers
* Choose how many numbers will be drawn
* Automatically generate a random bingo card
* Draw numbers sequentially
* Detect matching numbers in real time
* Display current progress throughout the game
* End the game when:

  * Every number has been matched (**BINGO!**), or
  * All draws have been completed

---

### 🎯 Mini Guessing Game (`Mini_Guessing_Game.py`)

A simple terminal-based number guessing game where players attempt to guess a randomly generated number within a specified range.

#### Features

* Randomly generates a number between **1 and 100**
* Validates user input and handles invalid entries gracefully
* Detects empty input and non-numeric values
* Checks that guesses fall within the valid range
* Provides hints indicating whether each guess is too high or too low
* Allows players to quit the game at any time by entering `q`
* Reports the number of guesses taken when the game ends
* Reinforces loops, conditional statements, input validation and random number generation

---

## Example Gameplay

### Mini Bingo Game

```text
Your Bingo Card:
[3, 18, 7, 22]

Number drawn: 7
✓ Match found!

Current score: 1 / 4
```

### Mini Guessing Game

```text
Welcome to the guessing game. Guess the correct number to win.

Try guessing the positive integer between 1 and 100 (type q to quit): 50
Sorry too low.

Try guessing the positive integer between 1 and 100 again (type q to quit): 75
Sorry too high.

Try guessing the positive integer between 1 and 100 again (type q to quit): 68
Congratulations you have guessed the number in 3 guesses.
```

---

## Notes

* This repository is intended for learning and practice rather than production use.
* Solutions prioritise readability, maintainability and understanding while exploring different approaches to solving programming problems.
* New Codewars kata are added as programming skills continue to develop.
* The mini games provide practical experience with user interaction, program flow and input validation.
* The repository demonstrates progressive learning through increasingly challenging exercises and projects.

---

## Future Improvements

Potential future additions include:

* Solving higher-difficulty Codewars kata (5 kyu and above)
* Organising Codewars solutions into multiple modules
* Adding automated unit tests using `pytest`
* Improving documentation and inline comments
* Adding comprehensive type hints throughout the project
* Creating additional terminal-based Python mini projects
* Refactoring the games into reusable classes and modules

---

## Licence

This project is licensed under the MIT Licence. Feel free to use, modify and adapt it for learning purposes.
