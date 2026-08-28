# Prime Innovation Towers Are Overlapping Charts of One Seam State, Not Additive Energy Sectors

## One prime gives a complete chart

For a prime \(p\), put \(L_p=\log p\). The cumulative innovation transform
partitions a seam state \(g\in L^2(0,\infty)\) into intervals

\[
I_{p,k}=[kL_p,(k+1)L_p).
\]

After translating each interval to the base window, the transform
\(\mathcal B_p\) is an isometry:

\[
\|g\|^2
=\sum_{k\ge0}\|g|_{I_{p,k}}\|^2.
\]

Thus one complete prime tower already contains the entire seam norm.

## Naive all-prime addition is a type error

For two primes \(p\) and \(q\),

\[
\|\mathcal B_pg\|^2=\|g\|^2
\quad,\quad
\|\mathcal B_qg\|^2=\|g\|^2.
\]

Adding the two chart energies gives \(2\|g\|^2\), not a finer measurement of
the source. Summing over all primes duplicates the same seam state infinitely
many times.

The prime index labels coordinate presentations, not orthogonal physical
sectors.

## Canonical common refinement

Let \(\mathbb P\) denote the primes. At finite height \(R\), collect all
prime-power boundaries

\[
\mathcal E_R=
\{k\log p:p\in\mathbb P,\ k\ge0,\ k\log p\le R\}.
\]

This set is finite. Sorting its distinct values produces a partition of
\([0,R]\) into consecutive refinement cells. Restricting \(g\) to these cells
gives one lossless refinement chart.

Every prime-specific interval is a disjoint union of refinement cells.
Therefore each \(\mathcal B_p\) is obtained from the refinement chart by an
isometric merge operation. Conversely, splitting recovers the refinement.
The transition between two prime charts factors through this common carrier
and preserves the seam norm.

## Consequence for the moving-seam current

The continuous ternary current \(\mathcal K_L(z)\) can telescope over any
finite refinement:

\[
\mathcal K_R(z)-\mathcal K_0(z)
=\sum_j
\left(
\mathcal K_{L_{j+1}}(z)-\mathcal K_{L_j}(z)
\right).
\]

But the mixed cells between consecutive boundaries belonging to different
prime charts are not supplied by a one-prime recursion. They require
cross-prime overlap incidence.

This identifies the exact arithmetic gate:

> Construct the mixed-prime split/merge cells that make all prime innovation
> charts descend from one common refinement, and show that their oriented
> ternary window increments agree on overlaps.

Without those cells, adding prime currents overcounts. With them, the global
object is a glued boundary state rather than an Euler sum of independent
energies.

## Relation to the multi-tower picture

What looked like many prime towers is one tower described in many valuation
charts. The needed extra structure is the overlap tower:

```text
prime-p chart  \
                common prime-power refinement -> one seam state
prime-q chart  /
```

The cross-prime coherence cells are themselves essential data. Equality of
the final scalar norms does not reconstruct their interval incidence or the
oriented moving-seam current.

## Scope

This theorem establishes the correct gluing architecture and exact finite
energy preservation. It does not prove that theta/Tate arithmetic supplies all
mixed-prime overlap morphisms, nor that the glued current is annihilated by a
completed scalar zero. Those are the next falsifiers.
