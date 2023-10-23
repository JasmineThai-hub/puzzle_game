from solver import *
from constants import *
import json

def generate_puzzle():
    global puzzle
    # Ask for the user's input
    input_str = input("Enter the puzzle (e.g., '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0'): ")
    puzzle = [int(x) for x in input_str.split()]
    return input_str


def give_up():
    global puzzle, solved_puzzle
    print("Solving puzzle")

    heuristic = slide_wd(n, solved_puzzle)
    solver = IDAStar(heuristic, slide_neighbours(n))
    path, moves, bound, nodes_evaluated = solver.solve(puzzle, lambda p: p == solved_puzzle)

    print("\nSolution:")
    for p in path:
        slide_print(p)
        print()
        contents = ", ".join({-1: "Left", 1: "Right", -4: "Up", 4: "Down"}[move[1]] for move in moves)


    print("Number of steps:", len(path) - 1)
    print("Nodes evaluated:", nodes_evaluated)

    movesList = contents.split(', ')
    for move in movesList:
        print(f'{move.lower()}')
        print(f'{move.lower()}')
    return movesList

def save_solution_to_file(puzzle_str, movesList):
    """
    Saves the solution to the 'solved.json' file.
    """
    data = {}
    try:
        with open('solved.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # If file not found or empty, we'll create it

    data[puzzle_str] = movesList  # Add/Update the puzzle solution

    with open('solved.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    global puzzle, solved_puzzle
    solved_puzzle = slide_solved_state(n)
    puzzle_str = generate_puzzle()
    movesList = give_up()
    save_solution_to_file(puzzle_str, movesList)



if __name__ == "__main__":
    main()
