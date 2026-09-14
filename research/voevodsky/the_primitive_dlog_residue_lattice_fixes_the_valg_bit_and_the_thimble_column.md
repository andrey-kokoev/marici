# The primitive dlog residue lattice fixes the v_alg bit and the thimble column

## Integral normalization of the v_alg quotient line

The source-selected rank-one quotient

\[
\langle e_6,v_{\rm alg}\rangle/\langle e_6\rangle
\]

has exact logarithmic connection form

\[
\alpha_{\rm alg}=d\log D,
\qquad
D=(E^2-X_1X_2)(E^2+X_1X_2).
\]

The two irreducible divisor components occur with multiplicity one. Therefore the logarithmic residues of \(d\log D\) are

\[
(1,1).
\]

Their gcd is one. By the integral residue sequence for logarithmic forms, this defines the unique primitive integral lattice on the rational quotient line, up to overall sign. Consequently the integral dual of the primitive \(v_{\rm alg}\) quotient generator is exactly divisor linking with \(D\); no unknown factor of two remains.

This closes the normalization gate left open by the earlier divisor-linking packet.

## v_alg pairing

At the generic total-energy cusp,

\[
D|_{E=0}=-X_1^2X_2^2
\]

is a unit when \(X_1X_2\ne0\). A sufficiently small total-energy thimble has zero intersection/linking with both components of \(D\). Hence

\[
\boxed{
\langle2m,v_{\rm alg}^\vee\rangle
\equiv0\pmod2.
}
\]

Thus

\[
b=0.
\]

## e6 pairing

The independently constructed paired-node calculation fixes the primitive Betti normalization

\[
e_{6,\mathrm B}=[C_+]-[C_-]
\]

and shows that the two Bunch--Davies node co-cores have equal orientation. Their two half-classes sum to one primitive component difference, so

\[
\boxed{
\langle2m,e_6^\vee\rangle
\equiv1\pmod2.
}
\]

Thus

\[
a=1.
\]

## Integral thimble/Gysin column

Combining the two primitive integral pairings gives

\[
\boxed{
(a,b)=(1,0).
}
\]

Equivalently, after changing the lift by an algebraic integral class to choose the minimal representative,

\[
\boxed{
2m=e_6.
}
\]

The corresponding coinvariant extension is torsion-absorbing and free of rank two:

\[
L_{1,0}
=
\frac{\mathbb Z\langle e_6,v_{\rm alg},m\rangle}
{\langle2m-e_6\rangle}.
\]

## Scope

The sign of \(e_6\) depends on the global Poincaré-residue orientation, but the mod-two column does not. This result is for the generic nonsoft total-energy cusp \(X_1X_2\ne0\). Soft intersections require separate specialization.

This cusp column does not by itself choose the sum-versus-difference kernel in the fixed pyramid route plane; that remains the separate relative-to-absolute route interface \(J\).

Verification:

- `research/voevodsky/checkers/check_integral_thimble_Gysin_column.py`
- `research/voevodsky/results/integral_thimble_Gysin_column.json`
