# Entry 486 — The Generic Interior Odd Cokernel Has One Flat Residual Line

Entries 483--484 close the two endpoint gates for the extensive odd Bockstein
tail. Benincasa Entry 485 then proves that naive coefficientwise reduction
modulo the quartic is not a chain map. The complementary invariant computed
here is the interior fiber of the complete orbit-completed exact cokernel
before adding the missing Gauss--Manin/Koszul correction.

## Generic-point census

Specialize the target at fixed values

\[
b=0,2,3,
\]

all away from \(b=\pm1\), but retain every source polynomial jet before
evaluation.  This is essential: substituting into a chosen quotient basis
would lose the differential-operator relations.

For total source cutoffs \(D=12,16,20,24\), all three generic points give the
same stable dimensions:

\[
\dim C_{0,-}=2,
\qquad
\dim C^{(1)}_-=3.
\]

There is therefore no cutoff-growing interior tail.  However, the dual-number
fiber is not flat: a flat lift of a two-dimensional special fiber would have
dimension four.

Over \(\mathbb Q[u]/(u^2)\), the dimensions determine the finite module type

\[
\boxed{
C_-^{\rm gen}\simeq
\mathbb Q[u]/(u^2)\oplus\mathbb Q
}
\]

at the level of the tested generic fibers: one special class lifts flatly and
one is killed at first order.

## Interpretation

Entry 474 already distinguishes the roles in the stable normal form.  The
full \(a\)-tail lifts through first order, whereas the odd resonance supplies
the failed endpoint class.  After generic evaluation collapses polynomial
orbits, this identifies the surviving flat summand with one interior
quartic-tail direction and the length-one summand with the reduced resonant
direction.

Thus the endpoint calculations remove the **growing** obstruction, but the
uncorrected complete odd cokernel does not reduce to the matrix-factorization
line. One flat odd coefficient line remains throughout the interior.

This line cannot be removed by a functor supported only at \(b=\pm1\), since
it is detected at three points of the complement. Entry 485 identifies why a
map to the Cayley--Menger module is not yet available: the relative-de-Rham
Gauss--Manin/Koszul correction is missing. The next gate is to construct that
correction and test whether it absorbs the flat line or maps it to the odd
part of the quartic carrier. Discarding it solely to match the desired
rank-one target would be fitted.

No new carrier geometry is indicated; the remaining datum is an interior
quartic-tail coefficient map.

The executable audit is
`research/voevodsky/check_soft_axis_generic_interior_odd_cokernel.py`.
