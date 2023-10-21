# Documentation for 4x4 Puzzle Solver with Pygame

## Overview

The `4x4 Puzzle Solver` is an interactive game that allows users to play with a 4x4 sliding puzzle and seek a solution from the solver when needed. The game is built using the `pygame` library.

## Table of Contents
1. [Imports and Initial Setup](#imports-and-initial-setup)
2. [Classes](#classes)
3. [Game Functions](#game-functions)
4. [Main Game Loop](#main-game-loop)

## 1. Imports and Initial Setup

**Imports**
- `pygame`: Used for rendering the game interface and handling events.
- `solver`: Contains utilities for solving the puzzle (e.g., IDA* algorithm).
- `constants`: Contains constants like button color, background color, shuffle_num (how many shuffles from solved state)

**Initial Setup**
- Pygame is initialized.
- Button constants are defined for styling and font.
- 

## 2. Classes

### `Button`

This class represents an interactive button displayed on the screen.

#### Attributes:
- `rect`: A `pygame.Rect` object representing the button's rectangle.
- `text`: The text displayed on the button.
- `action`: The function to be executed when the button is pressed.
- `hovered`: A boolean indicating if the mouse is hovering over the button.

#### Methods:
- `handle_event(event)`: Checks if the button is being hovered or clicked and updates the state accordingly.
- `draw(screen)`: Renders the button on the provided `screen`.

## 3. Game Functions

### Puzzle Rendering:

- `draw_tile(screen, number, x, y)`: Draws a tile with a specific number at a given position `(x, y)` on the `screen`.
  
- `draw_puzzle(screen, puzzle)`: Renders the entire puzzle on the screen.

### Puzzle Interaction:

- `move_tile(puzzle, direction)`: Moves the empty tile in the specified direction (up, down, left, right) if the move is valid. Returns the updated puzzle.

### Puzzle Generation:

- `generate_puzzle()`: Generates a shuffled 4x4 puzzle.

### Solver Interaction:

- `give_up()`: Invokes the solver (from the `solver` module) to find a solution to the current puzzle state. The solution is displayed step-by-step on the screen.

## 4. Main Game Loop

The `main()` function establishes the primary game loop, handling user inputs and game rendering:

- Sets up the display window and the buttons for "Give Up" and "New Puzzle".
  
- The primary game loop listens for user events:
  - Quit the game.
  - Move tiles using arrow keys.
  - Interact with buttons.
  
- If the user gives up, the game enters the "solving" state, displaying each move of the solution in sequence.
  
- Draws the current puzzle state and buttons on each iteration.

## How to Run:
1. Ensure all dependencies (Pygame and solver) are correctly installed.
2. Run the script. you can execute python puzzle_game.py in the terminal.
3. Enjoy!