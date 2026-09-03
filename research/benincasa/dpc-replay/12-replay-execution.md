# Replay 12 — replay execution defects

## Problem
A replay imported a top-level elimination and timed out; the next source lookup raised KeyError.
## Bold conjecture
A bounded dependency-free verifier can import the canonical scalar source directly.
## Named rivals
Top-level solver import; wrong namespace; direct canonical-source import.
## Risky consequence
Both certificates verify within the command bound.
## Strongest falsification
The corrected verifier completes in seconds, annihilating 692 and 1308 columns with target pairing one.
## Disposition
Retain only the corrected bounded verifier and result.
