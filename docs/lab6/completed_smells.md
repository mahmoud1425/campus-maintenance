# Task C1 — Completed Code Smells Table

| Smell | Where | Principle it breaks |
|---|---|---|
| Long if/elif chain on `kind` | Loop body and after the loop in `make_invoice` | OCP: a new student type means editing the function |
| One function does too much | `make_invoice` calculates, formats, writes a file and prints | SRP: more than one reason to change |
| Magic numbers (1200, 0.5, 2000, 5000) | Hard-coded inside the calculations | Readability / maintainability |
| File opened without `with` | `open(...)` / `f.close()` in `make_invoice` | Poor resource management; also DIP (disk is hard-wired) |
| Fee calculated per course | Inside the `for` loop, though only total hours matter | Needless complexity |
