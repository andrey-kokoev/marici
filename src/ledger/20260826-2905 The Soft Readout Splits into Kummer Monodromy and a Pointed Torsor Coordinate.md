# 2905 — The Soft Readout Splits into Kummer Monodromy and a Pointed Torsor Coordinate

## Affine monodromy representation

Use the basis

\[
(P_{\rm aff},\tau_1,\tau_{-3})
\]

and the commuting nilpotents \(N_1,N_{-3}\) of Entry 2897.  Define

\[
a_1=\frac{3-\kappa}{64p^4(1-\kappa)^2},
\qquad
a_{-3}=\frac{1}{64p^4(1+\kappa)}.
\]

With the common factor \(2\pi i\) understood, the three finite monodromies are

\[
M_{-\kappa}=I+a_1N_1,
\]

\[
M_{+\kappa}=I+a_{-3}N_{-3},
\]

and

\[
M_{-1}=I-a_1N_1-a_{-3}N_{-3}.
\]

Because all products of the two translation nilpotents vanish,

\[
M_{-1}M_{+\kappa}M_{-\kappa}=I.
\]

Thus the source-labelled affine monodromy is globally consistent and
generically nontrivial, while its compact elliptic quotient remains the
identity.

## Cohomology versus pointing

Changing an affine primitive by a constant does not change any of the above
monodromies.  The Kummer cohomology class is therefore determined by the
residue packet independently of pointed normalization.

The numerical finite value of the soft primitive is different.  It requires a
chosen origin in the affine torsor.  The source supplies that origin through
the pointed normalization at \(t=2\).

## Result

The physical soft readout contains two differently typed pieces:

1. an intrinsic rank-two labelled Kummer monodromy class;
2. a source-fixed pointed torsor coordinate.

The first survives every constant affine re-normalization.  The second is not
intrinsic without the source basepoint, but it is not arbitrary once the
source normalization is frozen.

Neither piece changes compact elliptic cohomology, and neither requires a new
carrier divisor.

## Next falsifier

Test sewing.  When two source subgraphs carrying such pointed Kummer torsors
are joined along a Cut interface, determine whether their affine origins sew
canonically or leave a finite mismatch class.  This is the first place where
the relative readout mechanism can challenge the shared-calculus hypothesis
globally rather than locally.

## Durable artifacts

- `research/benincasa/check_soft_marked_affine_monodromy.py`
- `research/benincasa/soft-marked-affine-monodromy.json`
