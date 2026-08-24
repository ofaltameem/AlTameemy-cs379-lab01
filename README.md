# Lab 1: The Multi-Paradigm Tour

Full assignment: `Lab_01_The_Multi_Paradigm_Tour.md`.

## Run
```bash
gcc -O2 -o stats_c stats.c
go build -o stats_go stats.go
python verify_tour.py
```
Complete the TODO in each of `stats.py`, `stats.c`, and `stats.go`.
`verify_tour.py` runs all three against 5 fixed test vectors
(including a mode tie-break case), diffs the output, measures
executable size and cold-start latency, and prints a comparison
table. Success Token prints only if all three implementations agree
on every vector.

## Submit
1. `Lab1_Theory.pdf` (or `.md`), including your measured data table
2. `stats.c`, `stats.py`, `stats.go`
3. Screenshot/terminal output of the Success Token from `verify_tour.py`
4. Confirmation the `v1.0` git tag was pushed (see the assignment's Git Submission steps)
