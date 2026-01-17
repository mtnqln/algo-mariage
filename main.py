from solveur import solver_positions


def main():
    people = [
        {"name": "A", "group": "work"},
        {"name": "B", "group": "family"},
        {"name": "C", "group": "work"},
        {"name": "D", "group": "work"},
        {"name": "E", "group": "family"},
        {"name": "F", "group": "family"},
    ]
    relations = {
        ("A", "B"): 3.0,
        ("A", "C"): -2.0,
        ("A", "D"): 0.0,
        ("B", "C"): 1.0,
        ("B", "D"): 2.0,
        ("C", "D"): -3.0,
    }
    positions = solver_positions(people=people, relations=relations, num_per_tables=2)
    if positions:
        print("\n--- Seating Chart ---")
        for t, v in positions.items():
            print(f"Table {t} (Score: {v[0]}): {v[1]}")


if __name__ == "__main__":
    main()
