from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value, LpBinary
from pulp import PULP_CBC_CMD
import itertools
import math


def solver_positions(
    people: list[str], relations: dict[tuple[str, str], float], num_per_tables: int
):
    # keys are sorted
    relations_clean: dict[tuple[str, str], float] = {
        tuple(sorted(k)): v for k, v in relations.items()
    }  # type: ignore
    all_combinations = set(itertools.combinations(people, 2))
    for pair in all_combinations:
        sorted_pair = tuple(sorted(pair))
        if sorted_pair not in relations_clean.keys():
            relations_clean[pair] = 0.0  # missing keys are added with 0.0 value

    relations = relations_clean

    num_tables = math.ceil(len(people) / num_per_tables)  # number of tables needed
    tables = list(range(num_tables))

    # Problem type
    prob = LpProblem("SolverPositions", LpMaximize)

    # Variables
    ValueBytTable = LpVariable.dicts("Table", [n for n in tables])
    x = LpVariable.dicts(
        "Position", [(p, t) for p in people for t in tables], 0, 1, LpBinary
    )
    y = LpVariable.dicts(
        "AreAtSameTable",
        [(p, t) for p in relations.keys() for t in tables],
        0,
        1,
        LpBinary,
    )

    # Objective function
    prob += lpSum([ValueBytTable[n] for n in tables])

    # Constraints
    for p in relations.keys():
        for n in tables:
            prob += y[p, n] <= x[p[0], n]
            prob += y[p, n] <= x[p[1], n]
            prob += x[p[0], n] + x[p[1], n] - 1 <= y[p, n]

    for t in tables:
        prob += lpSum([x[p, t] for p in people]) <= num_per_tables

    for n in tables:
        prob += ValueBytTable[n] == lpSum(
            relations[p] * y[p, n] for p in relations.keys()
        )

    for p in people:
        prob += lpSum(x[p, n] for n in tables) == 1

    # Solving problem
    prob.solve(PULP_CBC_CMD(msg=False))

    # Solution and status
    print(f"Status : {LpStatus[prob.status]}")
    print(f"Objective function value : {value(prob.objective)}")
    if prob.status == 1:
        result = {}
        for t in tables:
            seated_people = [p for p in people if value(x[p, t]) == 1.0]

            table_score = 0
            for pair in relations:
                if value(y[pair, t]) == 1.0:
                    table_score += relations[pair]
            result[t] = (table_score, seated_people)
        return result
