import readline
import random
import sys
import re

# Uncomment this for testing
# random.seed("debug")


def try_read():
    try:
        return input()
    except EOFError:
        return None


def generate_lines():
    line = try_read()
    while line and line != "exit":
        yield line
        line = try_read()


class Die:
    count = 0
    sides = 0

    def __init__(self, count, sides):
        self.count = count
        self.sides = sides

    def roll(self):
        return sum([random.randint(1, self.sides) for _ in range(self.count)])

    def render(self):
        return str(self.count) + "d" + str(self.sides)


class Roll:
    dice = []
    modifier = 0

    def __init__(self, modifier, *dice):
        self.dice = dice
        self.modifier = modifier

    def eval(self):
        roll = [d.roll() for d in self.dice]
        return roll, sum(roll) + self.modifier


def parse_roll(roll: str):
    dice_re = r"(\d+)d(\d+)"
    mod_re = r"\s*\+\s*(\d+)"
    def extract_die(m): return Die(
        count=int(m.group(1)), sides=int(m.group(2)))
    dice = [extract_die(match) for match in re.finditer(dice_re, roll)]
    mod_match = re.search(mod_re, roll)
    mod = int(mod_match.group(1)) if mod_match else 0
    return Roll(mod, *dice)


def parse_query(query: str):
    rolls = [r.strip() for r in re.split(';|:|,', query)]
    return [parse_roll(roll) for roll in rolls]


def print_roll(roll: Roll, results: list, total: int):
    modifier = " + " + str(roll.modifier) if roll.modifier > 0 else ""
    print("\t" + " ".join(d.render() for d in roll.dice) + modifier + ":")
    print(
        "\t\t" + " + ".join([f"({result})" for result in results]) + f" + {roll.modifier}")
    print(f"\t\t= {total}")


def eval_query(query: str):
    rolls = parse_query(query)
    for roll in rolls:
        results, total = roll.eval()
        print_roll(roll, results, total)


# Query:
# 1d4 2d6 1d8 + 9 ; 9d2 1d5 8d5 +2

# Roll
# 1d4 2d6 1d8 + 9

# Die
# 1d4

def main():
    # If there are arguments, use them as the query. Otherwise read from stdin
    if len(sys.argv) > 1:
        queries = [" ".join(sys.argv)]
    else:
        queries = map(str.rstrip, generate_lines())

    for query in queries:
        eval_query(query)


if __name__ == "__main__":
    main()
