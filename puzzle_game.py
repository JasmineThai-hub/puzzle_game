from solver import *
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from constants import *
import json
from button import Button


def draw_tile(screen, number, x, y):
    # Draw the border
    border_rect = pygame.Rect(x * TILE_SIZE - BORDER_SIZE // 2, y * TILE_SIZE - BORDER_SIZE // 2, TILE_SIZE + BORDER_SIZE, TILE_SIZE + BORDER_SIZE)
    pygame.draw.rect(screen, BORDER_COLOR, border_rect)

    # Draw the tile inside the border
    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, TILE_COLOR, rect)

    # Draw the number on the tile
    text = FONT.render(str(number), True, TEXT_COLOR)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def draw_puzzle(screen, puzzle):
    screen.fill(BACKGROUND_COLOR)
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            number = puzzle[y * BOARD_SIZE + x]
            if number:  # Don't draw the empty tile (0)
                draw_tile(screen, number, x, y)

def move_tile(puzzle, direction):
    # Convert linear puzzle to 2D for easier navigation
    puzzle_2d = [list(puzzle[i:i+BOARD_SIZE]) for i in range(0, len(puzzle), BOARD_SIZE)]
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if puzzle_2d[y][x] == 0:  # Empty tile found
                # Swap based on direction
                if direction == "down" and y < BOARD_SIZE - 1:
                    puzzle_2d[y][x], puzzle_2d[y+1][x] = puzzle_2d[y+1][x], puzzle_2d[y][x]
                elif direction == "up" and y > 0:
                    puzzle_2d[y][x], puzzle_2d[y-1][x] = puzzle_2d[y-1][x], puzzle_2d[y][x]
                elif direction == "right" and x < BOARD_SIZE - 1:
                    puzzle_2d[y][x], puzzle_2d[y][x+1] = puzzle_2d[y][x+1], puzzle_2d[y][x]
                elif direction == "left" and x > 0:
                    puzzle_2d[y][x], puzzle_2d[y][x-1] = puzzle_2d[y][x-1], puzzle_2d[y][x]
                return sum(puzzle_2d, [])

def generate_puzzle():
    global puzzle, solved_puzzle

    solved_puzzle = slide_solved_state(n)

    # Shuffle the solved puzzle
    puzzle = solved_puzzle
    for _ in range(shuffle_num):  # Shuffle with shuffle_num moves
        _, puzzle, _ = random.choice(list(slide_neighbours(n)(puzzle)))

    print("Generated Puzzle:")
    slide_print(puzzle)

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

def give_up():
    global puzzle, solved_puzzle, is_solving, current_path_index, path
    heuristic = slide_wd(n, solved_puzzle)
    solver = IDAStar(heuristic, slide_neighbours(n))
    path, moves, bound, nodes_evaluated = solver.solve(puzzle, lambda p: p == solved_puzzle)

    print("\nSolution:")
    for p in path:
        slide_print(p)
        print("")
        contents = ", ".join({-1: "Left", 1: "Right", -4: "Up", 4: "Down"}[move[1]] for move in moves)

    print("Number of steps:", len(path) - 1)
    print("Nodes evaluated:", nodes_evaluated)
    movesList = contents.split(', ')
    puzzle_str = ' '.join(map(str, puzzle))
    save_solution_to_file(puzzle_str, movesList)
    print("Saved to solved.json!")

    # Set the flag and reset the index
    is_solving = True
    current_path_index = 0


is_solving = False
current_path_index = 0
path = []
def main():
    global puzzle, solved_puzzle, is_solving, current_path_index, path
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))  # Add extra space for buttons
    pygame.display.set_caption("Puzzle Solver")

    buttons = [
        Button(10, HEIGHT + 10, 100, 30, "Give Up", give_up),
        Button(WIDTH - 110, HEIGHT + 10, 100, 30, "New Puzzle", generate_puzzle)
    ]
    solved_puzzle = slide_solved_state(n)

    # Shuffle the solved puzzle
    puzzle = solved_puzzle
    for _ in range(shuffle_num):  # Shuffle with shuffle_num moves
        _, puzzle, _ = random.choice(list(slide_neighbours(n)(puzzle)))

    print("Generated Puzzle:")
    slide_print(puzzle)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not is_solving:  # Skip inputs if currently solving
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        puzzle = move_tile(puzzle, "up")
                    elif event.key == K_DOWN:
                        puzzle = move_tile(puzzle, "down")
                    elif event.key == K_LEFT:
                        puzzle = move_tile(puzzle, "left")
                    elif event.key == K_RIGHT:
                        puzzle = move_tile(puzzle, "right")
                for button in buttons:
                    button.handle_event(event)

        if is_solving:
            if current_path_index < len(path):
                puzzle = path[current_path_index]
                draw_puzzle(screen, puzzle)
                pygame.display.flip()
                current_path_index += 1
                pygame.time.wait(solve_speed)
            else:
                is_solving = False

        else:
            draw_puzzle(screen, puzzle)
            for button in buttons:
                button.draw(screen)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
