# Photon as electron/positron cuts: exact first test

## Frozen operation

Use electron ABCDEA and positron AEDCBA, with their existing metric and labels. Enumerate every contiguous two-arrow or three-arrow path in each. Retain the owning seed and occurrence history. Match endpoints only when their registered labels already agree; introduce no new vertex identifications.

This is a combinatorial cut test. Open paths are not themselves affine isometry generators. For the geometric closure comparison, retain the original source generators rather than pretending an open path is an admitted generator.

## Enumeration

Ten paths per seed give 100 ordered pairs. Twenty have matching endpoints. They fall into four directed classes (three if seed-owner exchange is ignored):

| Electron path | Positron path | Matches | Result |
|---|---|---:|---|
| ABC | AEDC | 5 rotations | Parallel routes A -> C, lengths 2 and 3 |
| ABCD | AED | 5 rotations | Parallel routes A -> D, lengths 3 and 2 |
| ABC | CBA | 5 rotations | Closed backtracking return, lengths 2 and 2 |
| ABCD | DCBA | 5 rotations | Closed backtracking return, lengths 3 and 3 |

The unequal-length cuts do **not** match as consecutive paths around a new closed loop: they have the same start and end, hence are parallel alternatives. Their undirected support remains the original pentagon. Subtracting their oriented chains recovers its cyclic boundary, but subtraction is not a new primitive path or a supplied filling witness.

The equal-length paths close by backtracking. Their oriented support chains cancel, while their distinct arrow occurrences and histories remain retained.

## Continuation test

Reuse the endpoint incidence convention K[b,a]=1 iff target(a)=source(b), without prescribing a desired mode:

- parallel 2/3 routes: characteristic polynomial lambda^5, with K^3=0;
- 2/2 backtracking: lambda^2(lambda^2-2);
- 3/3 backtracking: lambda^2(lambda^4-3lambda^2+1).

None has the factor lambda^2+lambda+1 associated with the prior conjugate photon-mode pair. This rejects that specific mode construction for these cuts; it does not claim that every possible composite photon construction fails.

## Same processor, same closure

Every nonempty cut vertex set closes to all five original vertices under the inherited forward/inverse generators. Running the unchanged assembler with both generators preserves the complete electron four-simplex, including its existing interface role. No distinct final shape emerges from these cut choices.

## Result

The first meaning of “half electron, half positron” tested here produces either parallel complementary routes or backtracking returns—not a separate assembled photon shape. A different result would require an explicit additional gluing/comparison operation, with its label identifications and retained information specified.

No new spin, charge, projection or particle-dependent stopping rule was introduced.

## Verification

Ten exact checks pass, retaining all twenty matched pairs and their continuation matrices.

```sh
python research/strominger/checkers/check_half_electron_positron_seeds.py
```

Result: `research/strominger/results/half_electron_positron_seeds.json`.
