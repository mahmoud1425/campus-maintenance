
# Week 5 - Static Analysis Findings

## Ruff Findings

| Rule | Count | Problem | Planned Fix |
|---|---:|---|---|
| F401 | 2 | Unused imports | Remove imports |
| I001 | 1 | Imports not sorted | Organize imports |
| B006 | 1 | Mutable default argument | Use immutable default |
| F841 | 1 | Unused local variable | Remove tmp |

## Pylint Findings

| Rule | Count | Problem | Planned Fix |
|---|---:|---|---|
| C0114 | 1 | Missing module docstring | Add module documentation |
| C0116 | 3 | Missing function docstrings | Add function documentation |
| W0102 | 1 | Dangerous mutable default | Use safe default |
| R0913 | 1 | Too many arguments | Reduce parameters |
| R0917 | 1 | Too many positional arguments | Simplify function interface |
| C0121 | 2 | Boolean/None comparisons | Use proper comparisons |
| W0613 | 1 | Unused argument | Remove unused argument |
| W0612 | 1 | Unused variable | Remove tmp |
| C0103 | 1 | Invalid function name | Use snake_case |
| E0606 | 1 | Possibly unassigned fee | Fix scholarship handling |
| W0611 | 2 | Unused imports | Remove imports |

## Extra Code Smells

- Poor variable names (d, t, y, s, disc, x)
- Duplicated logic in ProcessAll
- Mixed calculation and printing responsibilities
- Too many responsibilities in calc

## Hidden Bug

ProcessAll does not handle scholarship students (type 3).
The fee variable may retain a previous student's fee if a scholarship
student follows another student. If a scholarship student is processed
first, fee may not be initialized.
