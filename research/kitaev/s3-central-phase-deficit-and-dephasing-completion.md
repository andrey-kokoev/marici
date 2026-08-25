# Central phase deficit and the one-port dephasing completion

Owner: `marici.Kitaev`

## Three nested control targets

The two-flux-port Lie algebra forces three distinct targets apart:

1. within-block conjugation requires `direct_sum_a su(d_a)`, dimension 28;
2. complete sector dephasing requires central controls separating all eight
   labels;
3. arbitrary blockwise phase control requires the full eight-dimensional
   center.

The two-port surface passes the first target, fails the second by one
collision, and has a three-dimensional deficit for the third.

## Exact missing directions

The available central trace rank is five.  A basis for its missing covectors,
in `(A,B,C,D,E,F,G,H)` coordinates, is

\[
(1,-1,0,-1,1,0,0,0),
\]

\[
(1,1,-1,0,0,-1,1,0),\qquad
(1,1,-1,0,0,-1,0,1).
\]

Three additional endpoint quadratures are necessary and sufficient for full
central rank eight.

## Dephasing needs only one

The five available central eigenvalue coordinates give seven distinct sector
signatures, with the unique collision `G~H`.  Thus the two-port surface cannot
kill `G`--`H` coherence.  One additional imaginary three-cycle endpoint
quadrature is necessary and sufficient.  After adding it, the separating
central rank is six.

The first exact generator found had integer sector eigenvalues

\[
(-18,-6,-3,-9,-5,-15,-12,0).
\]

and gave a valid but nonminimal 19-branch twirl.  A saturated-lattice successor
attains the sharp eight-branch minimum with eigenvalues

\[
(-8,1,2,3,6,7,20,5),
\]

whose residues modulo eight are all distinct.

## Correction boundary

Projective control suffices only for within-block depolarization.  Complete
inter-sector dephasing additionally requires central sector separation.  The
corrected inventory is gauge quadratures, the transposition and three-cycle
flux ports, and one imaginary three-cycle endpoint quadrature.

This is still a finite control theorem, not a source-local pulse, leakage, or
fault-tolerance theorem.  It instantiates Nima and Benincasa's
channel-relative faithfulness gate: one family is faithful for projective
conjugation but not for dephasing until a separately typed port is added.

## Verification

Run:

```text
uv run --with sympy --with numpy python -u research/kitaev/checkers/check_s3_two_flux_lie_control.py
```

Thirteen gates pass in schema v2.  Excitement 10/10, confidence 10/10,
realized information gain 10/10.
