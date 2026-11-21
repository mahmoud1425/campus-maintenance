# Task C1 — Completed Code Smells Table

| Code Smell | Before Refactoring | Improvement |
|---|---|---|
| Long Method / Multiple Responsibilities | Invoice calculation, text formatting, file writing, and printing were handled together. | Separated fee calculation using policy classes and used a writer for file output. |
| Conditional Logic | `if/elif` statements selected the fee calculation based on student type. | Replaced conditional fee calculation with separate policy classes. |
| Magic Numbers | Fee rates and service fees were hard-coded inside calculations. | Introduced named constants and class attributes for fee values. |
| Poor Resource Management | The file was opened and closed manually. | Used `with open(...)` to handle the file safely. |

