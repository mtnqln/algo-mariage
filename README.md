**Algo Mariage**

- **Description:** A small Python project that solves a seating/placement problem: given a set of people and pairwise relation scores, assign people to tables to maximize the total satisfaction (sum of relation scores for pairs seated at the same table).

- **Key idea:** The solver models the problem as a binary integer linear program (ILP) using `pulp`. Pairs that sit together contribute their relation score; the ILP places people on tables subject to table capacity constraints and one-seat-per-person.

**Requirements**

- Python 3.8+
- `pulp` (for the ILP solver)
- `networkx` (optional not implemented now, used in `graph.py` for graph-based solution)

Install dependencies:

With uv :
```bash
uv sync
```
or pip : 
```bash
pip install -r requirements.txt
```

**Usage**

- Edit the input (people and relations) in [main.py](main.py). Run the solver with:

```bash
python main.py
```

The default example in `main.py` demonstrates 4 people and pairwise relation scores.

**Repository structure**

- [main.py](main.py): small runner that calls the solver with a sample input.
- [solveur.py](solveur.py): the ILP-based solver. Uses `pulp` to maximize table scores.
- [graph.py](graph.py): weighted graph based solution (incomplete).

**Notes & next steps**

- The ILP formulation is in `solveur.py`. You can adapt `num_per_tables` or input formats to test other scenarios.

**License**


