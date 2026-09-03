# Replay 06 — dependency backend

## Problem
Bare system Python was tried for a SymPy-dependent checker.
## Bold conjecture
A dependency-free exact backend can replace unavailable SymPy.
## Named rivals
Governed uv environment; system Python; dependency-free Fraction/CRT backend.
## Risky consequence
The replacement must reproduce both exact certificates.
## Strongest falsification
Dependency-free replay annihilates 692 and 1308 columns with target pairing one.
## Disposition
Use the dependency-free backend. The obsolete SymPy checker was deleted.
