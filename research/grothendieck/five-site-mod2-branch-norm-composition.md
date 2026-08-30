# Five-site mod-two branch-norm composition

## Composition theorem

For nonempty branch subsets \(A,B\subseteq\{1,\ldots,5\}\), their mod-two
kernel norms satisfy

\[
N_A N_B=
\begin{cases}
N_{A\cup B},&A\cap B=\varnothing,\\
0,&A\cap B\ne\varnothing.
\end{cases}
\]

This follows from

\[
N_A=\prod_{i\in A}\epsilon_i,qquad \epsilon_i^2=0.
\]

Consequently every ordering of the distinct labelled deck directions in a
fixed subset \(B\) has the same product \(N_B\). The formal algebraic flags
are strictly order-independent. Repeating any direction kills the composite.

Across the 31 nonempty subsets there are 961 ordered nonempty pairs: 180
disjoint pairs compose to their union and 781 overlapping pairs compose to
zero.  The 325 ordered flags terminate with the expected profile

\[
5,20,60,120,120
\]

in codimensions one through five.

## Classification and boundary

The norm classes form the positive-degree part of the square-zero
exterior/Stanley--Reisner algebra

\[
\mathbf F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_i^2).
\]

This is a coherent formal deck-incidence shadow, not a census of nonempty
geometric branch intersections and not yet a physical composition law.
Order independence of group-algebra monomials cannot supply the
missing maps of relative pairs, boundary homotopies, or specialization
normalizations.  Nor does this finite \(\mathbf F_2\)-algebra yield an Euler
product, geometric Frobenius, or Carrier-derived arithmetic.

The geometric source census must be imposed separately: generic complex
geometry realizes only subset degrees one through three; degrees four and
five require additional external discriminants. The rank-two Kummer line is
a supported local realization with a paired selector, not an activation of
every formal monomial.

## Verification

`checkers/five_site_mod2_branch_norm_composition.py` checks every ordered
pair, every permutation of every nonempty branch subset, and every repeated
branch direction.
