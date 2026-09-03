# DPC: A16 persistence and all-even induction

## Problem

Do exact persistence through A16 and parity preservation prove all-even survival of the twelve filtered classes?

## Bold conjecture

Finite path persistence plus parity-orbit transport excludes every later same-grade killer.

## Named rivals

Later generators in the same parity sector may kill a class; filtered quotient maps may fail injectivity; or a colon/saturation theorem may supply the missing no-killer result.

## Risky consequences and strongest falsification

All 48 A16 paths remain nonzero. The twelve mixed paths agree exactly. Filtered ranks at grades six through eight are 1,074, 3,590, and 7,415.

The finite tests do not establish injectivity. No colon/saturation theorem or direct-sum decomposition excludes later same-parity killers.

## Disposition

The bold induction conjecture is rejected. The twelve classes persist on every tested path through A16, but all-even survival remains open.

The first missing object is an injectivity theorem for squared-axis multiplication on the grade-bounded quotient. An equivalent acceptance test is

\[
(\operatorname{im}d_1:x^2)=\operatorname{im}d_1,
\qquad
(\operatorname{im}d_1:y^2)=\operatorname{im}d_1
\]

in each relevant grade and parity sector.

## Verification

- `research/voevodsky/check_cosmology_filtered_A16_persistence_induction.py` — exit 0
- `research/voevodsky/results/cosmology_filtered_A16_persistence_induction.json`
