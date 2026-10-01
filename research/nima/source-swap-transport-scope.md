# The actual retained swap fixes spectators—but only in its source sector

## Source operation found

`BoundaryGeneratedQuestions.agda` already supplies the comparison

    swap-filler : Filler fourQ fourQ
    (x,y) -> (y,x).

The retained image certificate in `RetainedComparisonSeries.agda` is
(0,2,1,3), with labels0=00,1=01,2=10,3=11. Thus this actual witness swaps1 and2
and fixes0 and3. It is the spectator-preserving operation, not the double swap.
The existing source also proves its square is the identity.

This is stronger than an arbitrary connection example: a specific retained
comparison has supplied the operation. Its scope must nevertheless be preserved.

## The pointing constraint matters

A source `Filler a b` is an equivalence carrying the distinguished value of a
to that of b. The distinguished value of fourQ is00, label0. Endofillers of this
fixed package therefore fix0. Their underlying finite permutation group has
six elements, the stabilizer of0.

The competing flat lift (12)(03) moves0 and is not an endofiller of this fixed
package. Conjugating the actual swap by admissible pointed relabellings gives
exactly the three transpositions among1,2,3. They supply a transport on the
ordered edges between these three unmarked states. Every ordered triangle has
nonidentity holonomy: a loop starting at i swaps the other two unmarked states.
It fixes both i and the distinguished value0.

So this **specified pointed swap sector** has genuine retained permutation
route effects. The marked value alone does not detect them; the full equivalence
does. This is not a claim about physical curvature or the rung4 reference metric.

## Two scope controls prevent a false global conclusion

First, the general fixed-package Filler signature admits all six pointed
permutations, including identity and3-cycles. It does not require every supplied
comparison to be the swap or an involution. The chosen swap orbit is a concrete
sector, not the uniquely selected generator of all comparisons.

Second, comparing packages Q_i and Q_j with different distinguished values asks
for g(i)=j. Both the endpoint swap and the double swap satisfy that boundary.
Therefore the double swap's failure as an endofiller of fourQ does not rule it
out for boundary-changing comparisons.

The source distinction is now explicit:

- operation inside the fixed pointed package: the retained involutive swap
  sector fixes spectators and has the checked nontrivial loops;
- comparison between differently pointed packages: the boundary condition alone
  still permits both previously classified lifts.

The Boolean distinguished value is not identified here with the physical rung4
reference. Nor are the12 carrier arrows automatically all supplied by the six
ordered unmarked edges of this pointed sector.

## Next source identification

Determine whether the intended carrier arrow is an operation inside a fixed
pointed package or a comparison between different boundary packages. Then supply
its actual retained filler. Replacing that filler by truth-of-existence erases
exactly the operation needed to decide the loop question.

Thus there is now a source-backed nonflat candidate sector, but no justified
selection of transport for the full carrier or the complete tower.

## Verification

    python research/nima/checkers/check_source_swap_transport_scope.py
    python research/aspect/scc/scc.py check nima-source-swap-transport-scope

The checker reads the actual Agda swap definition and its finite image
certificate, records their hashes, enumerates admissible pointed permutations,
checks all six unmarked triangle loops, and tests the moving-boundary hostile.
This is an exact finite audit of existing source, not a fresh Agda compilation.
Result: `research/nima/results/source-swap-transport-scope.json`.
