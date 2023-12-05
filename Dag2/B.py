import re

def main():
    with open("D:\Github\Advent_of_code_2023\Dag2\Input.txt", "r") as games_file:
        games = [line.strip().split(';') for line in games_file]    

    total_sum = 0

    for i, game_data in enumerate(games, start=1):
        color_counts = {"blue": 0, "red": 0, "green": 0}

        for item in game_data:
            # Use regular expression to find the numeric part after "Game"
            match = re.search(r"Game (\d+):", item)
            if match:
                item = re.sub(r"Game \d+:", "", item)
            
            counts_and_colors = item.split(',')

            for count_and_color in counts_and_colors:
                count, color = map(str.strip, count_and_color.split())
                count = int(count)

                if count > color_counts[color]:
                    color_counts[color] = count

        game_product = 1

        for color, count in color_counts.items():
            print(f"{count} {color} ", end="x ")
            game_product *= count

        print(f"= {game_product}")
        total_sum += game_product

    print("\nTotal Sum of Products:", total_sum)

if __name__ == "__main__":
    main()