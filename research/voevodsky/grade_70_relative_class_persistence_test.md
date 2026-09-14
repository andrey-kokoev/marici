# Persistence test for the grade-70 relative class

## Question

Does the relative one-class introduced by the shell-3 edge at grade 70 become an absolute persistent one-cycle, or does the connecting morphism identify it with a pre-existing component difference?

## Claim boundary

The test is restricted to the multiplicative-degree-two distinct-shell sector through grade 2000. Persistence is computed over two prime fields. Agreement does not prove an integral persistence classification beyond the recorded unit-incidence events.

## Competing predictions

1. The edge \([10;\{3\}]\), joining vertices 10 and 14, closes an existing path and births an absolute one-class at grade 70.
2. Its endpoints lie in separate components below grade 70, so the edge kills an absolute zero-class. Its nonzero relative \(H_1\) maps to that component difference under the long exact sequence and births no absolute one-class.
3. A one-class is born at grade 70 but dies when the square \([10;\{1,3\}]\) enters at grade 105.

## Test

Enumerate every degree-two cell with grade at most 2000. Compute absolute Betti numbers immediately below and at grades 70 and 105. Run filtration-compatible boundary reduction and inspect the reduced column of \([10;\{3\}]\). If nonzero, record the vertex class it kills; if zero, identify its killing two-cell if one occurs. Independently verify the grade-105 square boundary and its relation to the grade-70 edge.

## Acceptance

Prediction 1 requires a zero reduced edge column and positive absolute \(H_1\) increment at grade 70. Prediction 2 requires a nonzero reduced edge column, a decrease of absolute \(H_0\), and no increase of absolute \(H_1\). Prediction 3 requires the persistence pair edge 70--square 105.

## Computed result

The vertices 10 and 14 are born at grades 30 and 42. Immediately below grade 70 they lie in different connected components. The shell-3 edge has a nonzero reduced boundary over both tested fields and decreases the absolute zero-th Betti number from 3 to 2, while absolute first homology remains zero.

At grade 105 the square \([10;\{1,3\}]\) does contain the grade-70 edge in its boundary, but it is not paired with that edge in persistence reduction. Absolute first homology is zero both below and at grade 105.

## Disposition

Prediction 2 survives. The relative class at grade 70 maps under the connecting morphism to the difference of two pre-existing components and kills that zero-class. It never becomes an absolute one-class. Predictions 1 and 3 are rejected for this edge. This demonstrates that frequent noncanonical relative homology cannot be counted directly as persistent topology.
