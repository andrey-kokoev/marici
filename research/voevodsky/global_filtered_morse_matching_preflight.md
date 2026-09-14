# Global filtered Morse matching preflight

## Question

Can one cell-level matching explain both component mergers across grades and same-grade cancellation of every positive-dimensional persistence birth?

## Claim boundary

This is a bounded preflight on distinct-shell sectors of multiplicative degrees two through five at grade 20000. It tests a deterministic greedy matching, not yet an all-dimensional theorem.

## Proposed matching

In a fixed sector, order cells by grade, dimension, direction tuple, and base. Process dimensions upward. For each unmatched \(k\)-cell, match it with the least unmatched incident \((k+1)\)-cell.

The required filtration behavior differs by degree:

- a vertex--edge pair may cross grades and represents the death of a connected-component class;
- every pair whose lower cell has positive dimension must have equal grades, so it represents a zero-length positive-dimensional persistence interval.

After reversing matched Hasse arrows, the resulting directed graph must be acyclic. Every positive-dimensional cell must be paired; unmatched vertices represent connected components at the finite cutoff.

## Bold conjecture

The same deterministic rule yields an acyclic matching in every tested sector, leaves only vertices unmatched, and pairs every positive-dimensional lower cell at equal grade.

## Rivals

1. Matrix persistence synchronization cannot be realized by a cell-level matching.
2. Greedy choices create a gradient cycle despite correct homology.
3. A positive-dimensional cell remains unmatched in degree five.
4. A positive-dimensional pair crosses grades, revealing hidden positive persistence.

## Test

Construct full face posets through grade 20000 in multiplicative degrees two through five. Run the matching without sector-specific exceptions. Check face incidence, uniqueness, gradient acyclicity, complete pairing of positive-dimensional cells, and grade equality for every matched pair above degree zero. Compare the number of unmatched vertices with absolute \(H_0\) at the cutoff.

## Computed result

The greedy rule fails in every tested sector. In degree two it leaves 16 positive-dimensional cells unmatched and produces 73 positive-dimensional cross-grade pairs, although its gradient graph is acyclic. In degrees three through five it additionally creates gradient cycles. The unmatched-vertex counts disagree with absolute \(H_0\).

This does not contradict the persistence computations: matrix reduction can use linear combinations that a naive incidence matching cannot realize, and low-degree vertex choices can consume edges needed for same-grade higher cancellation.

## Disposition

The bold conjecture is rejected. Global synchronization is not explained by unconstrained upward greedy matching. The failure localizes the next constructor: positive-dimensional same-grade pairs must be reserved before vertex--edge component pairs, followed by an explicit gradient-acyclicity test. The first failure data are retained rather than treated as homological counterevidence.
