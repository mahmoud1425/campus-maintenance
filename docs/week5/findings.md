
# Week 5 - Static Analysis Findings

## Ruff Findings

| Rule | Count | Problem | Planned Fix |
|---|---:|---|---|
| | | | |
| | || |
| | || |

## Extra Code Smells

- Poor variable names
- Duplicated logic
- Mixed calculation and printing responsibilities
- Too many responsibilities in one function

## Hidden Bug

ProcessAll does not handle scholarship students (type 3).
The fee variable may retain a previous student's fee if the scholarship
student follows another student. If a scholarship student is processed
first, fee may not be initialized.
