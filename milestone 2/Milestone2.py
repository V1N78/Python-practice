ps5_game = 119.99

num_ps5_games = int(input("How many PS5 games?: "))

ps5_total = num_ps5_games * ps5_game

total_cost = ps5_total

print("Your order costs: ${}".format(total_cost))

print("""Order summary - you ordered:
{0} PS5 games for ${1}""".format(num_ps5_games, ps5_total))