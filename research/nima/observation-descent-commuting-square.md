# Observation maps commuting with carrier descent

## Fixed choices

Use the explicit stabilizer-indicator realization G_r=10I+J on the first r
probes f0,...,f_(r-1). Label carriers A={0,1,2,3}, B={0,4,5,6} with shared
reference0. Descent removes the highest label. These are the previously chosen
probe realization and witness ordering, not a uniqueness claim.

Let psi=sum c_i f_i. Define potential readouts

    q_i = <f_i-f0,psi> = 10(c_i-c0), i=1,...,6 when present.

Define O_r using only the labels still present. For r>=7 there are six readouts;
at r=6,5,4 there are five, four, three respectively.

The carrier restriction R_r sends c_i to c_i+c_(r-1)/(r+9) for surviving i.
The added term cancels in c_i-c0. Therefore O_(r-1) R_r = D_r O_r exactly,
where D_r is identity while all observed labels survive and otherwise deletes
the last readout. This verifies the kernel factorization condition directly.

## Readout metric and hidden state

For n readouts, the contrast Gram is M_n=10(I_n+J_n). The least-norm state
realizing q has norm q^T M_n^-1 q, where

    M_n^-1 = I_n/10 - J_n/[10(n+1)].

Any component orthogonal to the observed contrast span is additional hidden
state. The readout norm is the minimum compatible carrier norm; it is not the
norm of every carrier state with those readouts.

This replaces the coefficient interpretation in comparison-to-carrier-tower-
embedding.md for the original potential prototype. Its M-weighted update is
valid for expansion coefficients. Potential readouts instead use M^-1 and
comparison direction M*r.

At six-to-five readout descent, write s=sum(q1,...,q5). Then

    B6(q) = B5(q1,...,q5) + (3/35)*(q6-s/6)^2.

The raw record q6 reconstructs comparison values. The orthogonal budget record
is sqrt(3/35)*(q6-s/6); it measures the additional norm required by the sixth
readout. These are distinct record normalizations for the same lost scalar.

## Which comparisons descend?

A comparison row ell descends through readout deletion precisely when all its
coefficients on deleted readouts vanish. Direct enumeration of the existing
144 arrow-pair and nine state-pair rows gives:

| Target rung | Readouts retained | Original slots computable from them |
|---:|---:|---:|
| 11,10,9,8,7 | 6 | 153 |
| 6 | 5 | 78 |
| 5 | 4 | 27 |
| 4 | 3 | 0 |

At 7->6, retaining q6 as a record reconstructs every original comparison.
For the 78 descending rows, metric-orthogonal comparison projections also
commute with D. Indeed the surviving components of M6*ell equal M5*ell_low,
and the mismatch and denominator agree. The remaining 75 rows require
record-dependent updates rather than an autonomous low-rung comparison.

At rung4 this chosen ordering has retained all of A and removed B's three
nonreference labels. No original cross-carrier slot is autonomously evaluable.
Its data survive in records. Other witness orders can leave a different mix
of A and B and require their own slot census.

## Structural result

The observation square now connects the carrier geometry and the scalar
comparison data, with a metric derived from that same observation map.
The collection of all 153 comparisons does not close on the reduced live
readouts at lower rungs. Retained records supply the missing information.
This supports a record-augmented tower rather than identifying a complete
comparison programme with a bare four-coordinate rung.

Physical dynamics, clock, particle assignments, and GeV normalization are still
not fixed by this construction. Earlier Euclidean spectra do not transfer to
the inverse-metric readout update without recalculation.

## Verification

    python research/nima/checkers/check_observation_descent_square.py

Exact rational checks on every carrier basis vector verify all adjacent
squares. Additional checks enumerate surviving slots, reconstruct all 153
comparison values with a record, verify the quotient norm split, and test
commutation of all surviving updates at 7->6 on a specified nonzero seed.
The general update commutation also follows from the matrix identities above.
