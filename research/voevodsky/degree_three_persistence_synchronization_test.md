# Degree-three persistence synchronization test

## Question

Does the grade-by-grade synchronization found in multiplicative degree two extend to one- and two-dimensional persistence in multiplicative degree three?

## Claim boundary

The test covers the distinct-shell multiplicative-degree-three sector through grade 20000 over two prime fields. It does not test repeated-shell cubes, higher multiplicative degree, integral torsion, or an unbounded colimit.

## Bold conjecture

Every cycle-forming edge enters with enough same-grade squares to eliminate positive-length \(H_1\), and every relation among square fillers enters with enough same-grade cubes to eliminate positive-length \(H_2\). Thus all positive-dimensional persistence intervals have zero grade length.

## Rivals

1. Degree three is the first sector with a positive-length one-bar.
2. One-bars remain synchronized, but a positive-length two-bar appears before its cube filler.
3. Field-dependent pairings expose torsion or a reduction defect.

## Test

Enumerate every vertex, edge, square, and distinct-shell cube in multiplicative degree three with birth grade at most 20000. Reduce the filtration-compatible boundary matrix over two large prime fields, ordering equal-grade cells by increasing dimension.

For each zero reduced column in positive dimension, record its birth grade, homological degree, killing cell and death grade, or right-censored status. Separate zero-length pairs from positive-length and unpaired intervals. Verify \(d^2=0\), field agreement, and the exact census in each degree.

## Falsifier

Any positive-length or right-censored bar in degree one or two falsifies synchronization on this bounded sector. Field disagreement or broken boundary composition is an execution defect.

## Computed result

Through grade 20000 the sector contains 1924 vertices, 1739 edges, 352 squares, and 35 cubes. There are 317 reduced one-class births, each paired with a square at the same grade. There are 35 reduced two-class births, each paired with a cube at the same grade. No positive-length or right-censored bar occurs in either degree. No three-class is born.

The two fields give identical pairings and every boundary composition vanishes.

## Disposition

The synchronization conjecture survives in multiplicative degree three on the bounded domain. The first higher-dimensional test does not recover the predicted sparse persistence; it strengthens the alternative that the filtration may be positive-dimensionally trivial grade by grade. Higher multiplicative degree and an all-dimensional proof remain open.
