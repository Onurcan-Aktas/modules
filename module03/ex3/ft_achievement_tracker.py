import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer",
    "Strategist", "Unstoppable", "Speed Runner",
    "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:

    num: int = random.randint(5, 10)
    
    picked: list[str] = random.sample(ACHIEVEMENTS, num)
    
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    players: dict[str, set[str]] = {}

    for name in names:
        players[name] = gen_player_achievements()
        print(f"Player {name}: {players[name]}")

    print()

    all_distinct: set[str] = set()
    for p_set in players.values():
        all_distinct = all_distinct.union(p_set)

    print(f"All distinct achievements: {all_distinct}\n")

    common: set[str] = set(ACHIEVEMENTS)
    for p_set in players.values():
        common = common.intersection(p_set)

    print(f"Common achievements: {common}\n")

    for name in names:
        others_union: set[str] = set()
        for other_name, other_set in players.items():
            if other_name != name:
                others_union = others_union.union(other_set)
                
        unique_to_player: set[str] = players[name].difference(others_union)
        print(f"Only {name} has: {unique_to_player}")

    print()

    all_possible: set[str] = set(ACHIEVEMENTS)
    for name in names:
        missing: set[str] = all_possible.difference(players[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()