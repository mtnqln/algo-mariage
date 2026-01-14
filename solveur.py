from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value, LpBinary
from pulp import PULP_CBC_CMD

def solver_positions(people:list[str],
                     relations:dict[tuple[str,str],float],
                     num_per_tables:int
                     ):
    
    num_tables = round(len(people)//num_per_tables)
    tables = list(range(num_tables))

    # Problem type
    prob = LpProblem("SolverPositions",LpMaximize)

    # Variables
    TV = LpVariable("TotalValue")
    ValueBytTable = LpVariable.dicts("Table",[n for n in tables])
    x = LpVariable.dicts("Position",[(p,t) for p in people for t in tables],0,1,LpBinary) 
    y = LpVariable.dicts("AreAtSameTable",[(p,t) for p in relations.keys() for t in tables],0,1,LpBinary)

    # Objective function
    prob += lpSum([ValueBytTable[n] for n in tables])

    # Constraints
    for p in relations.keys():
        for n in tables:
            prob += y[p,n] <= x[p[0],n]
            prob += y[p,n] <= x[p[1],n]
            prob += x[p[0],n] + x[p[1],n] -1 <= y[p,n]

    for t in tables:
        prob += lpSum([x[p,t] for p in people]) <= num_per_tables 

    for n in tables:
        prob += ValueBytTable[n] == lpSum(relations[p]*y[p,n] for p in relations.keys())

    for p in people:
        prob += lpSum(x[p,n] for n in tables) == 1
    
    #Solving problem
    prob.solve(PULP_CBC_CMD(msg=False))

    #Solution and status
    print(f"Status : {LpStatus[prob.status]}")
    print(f"Objective function value : {value(prob.objective)}")
    if prob.status == 1:
            result = {}
            print("\n--- Seating Chart ---")
            for t in tables:
                seated_people = [p for p in people if value(x[p, t]) == 1.0]
                
                table_score = 0
                for pair in relations:
                    if value(y[pair, t]) == 1.0:
                        table_score += relations[pair]
                
                print(f"Table {t} (Score: {table_score}): {seated_people}")
                result[t] = seated_people
    return result




