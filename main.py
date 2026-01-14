from solveur import solver_positions


def main():
    people = ["A", "B", "C", "D", "E", "F", "G"]
    relations = {
        ("A", "B"): 3.0,
        ("A", "C"): -2.0,
        ("A", "D"): 0.0,
        ("B", "C"): 1.0,
        ("B", "D"): 2.0,
        ("C", "D"): -3.0,
    }
    solver_positions(people=people, relations=relations, num_per_tables=2)


if __name__ == "__main__":
    main()
