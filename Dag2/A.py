max_colors = {'red': 12, 'green': 13, 'blue': 14}

def extract_colors_and_numbers(game_data):
    parts = [part.strip() for part in game_data.split(';')]
    moves = [move.strip() for part in parts for move in part.split(',')]

    valid_moves = True
    for move in moves:
        count, color = move.split()
        if int(count) > max_colors.get(color, 0):
            valid_moves = False
            break

    return valid_moves

def calculate_score(valid_games):
    return sum(game_number if is_valid else 0 for _, game_number, is_valid in valid_games)

with open("D:\Github\Advent_of_code_2023\Dag2\Input.txt", "r") as input_data:
    games_data = [game.strip().split(':') for game in input_data.readlines()]

all_moves = [(extract_colors_and_numbers(game[1]), int(game[0].split()[-1]), extract_colors_and_numbers(game[1])) for game in games_data]

score = calculate_score(all_moves)

print(f"Total score: {score}")