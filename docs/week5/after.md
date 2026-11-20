# Week 5 - Before and After Refactoring

## Before / After Comparison

| Aspect | Before Refactoring | After Refactoring |
|---|---|---|
| Code structure | One function handled several responsibilities | Responsibilities separated into smaller functions |
| Naming | Short, unclear variable and function names | More descriptive names |
| Student types | Numeric type values | `StudentType` Enum |
| Course data | Dictionaries | `Course` dataclass |
| Default arguments | Mutable list default | Immutable default |
| Scholarship handling | Scholarship case could leave fee unassigned in `ProcessAll` | Scholarship case handled explicitly |
| Reporting | Calculation mixed with printing | Calculation and reporting separated |
| Static analysis | Ruff and Pylint issues present | Issues checked again after refactoring |

## Pairing Reflection

Working on the refactoring helped us understand how small changes can improve code readability and maintainability. We used tests to check that the refactored code preserved the expected behavior of the original code. We also identified and addressed the scholarship handling bug. The process highlighted the value of testing and static analysis before considering a refactoring complete.

# Week 5 - After Refactoring

## Before / After

| Metric | Before (`legacy_fees.py`) | After (`fees.py`, `grades.py`) |
|---|---|---|
| Ruff errors | 5 | 0 |
| Pylint score | 4.86/10 | 10.00/10 |
| Pylint messages | 15 | 0 |
| Tests passing | no characterization tests | 16/16 |

## Pairing Reflection

