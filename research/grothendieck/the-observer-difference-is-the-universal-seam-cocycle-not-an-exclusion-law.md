# The observer difference is the universal seam cocycle, not an exclusion law

## Fixed versus transported observer

For a half-line source with transform

\[
F(z)=\int_0^\infty \phi(v)e^{zv}\,dv,
\]

translate the source through a seam of length `L` and put

\[
q=e^{-sL},
\qquad
B_L(z)=\int_0^L\phi(v)e^{zv}\,dv.
\]

The exact fixed-endpoint readout of the transported source is

\[
E_{\mathrm{fix}}=q(F-B_L).
\]

The contragrediently transported observer, which moves with the source and
therefore ignores the crossed window, gives

\[
E_{\mathrm{mov}}=qF.
\]

Their observer-difference functional is exactly

\[
D_L=E_{\mathrm{fix}}-E_{\mathrm{mov}}=-qB_L.
\]

Thus Nima's fixed-versus-transported observer discrepancy is precisely the
moving seam current already forced by endpoint transport.

## What it detects

At a scalar zero `F(z)=0`, the transported observer also vanishes, while the
fixed observer reads

\[
E_{\mathrm{fix}}=-qB_L.
\]

The seam therefore retains information erased by the Evans scalar. It can
distinguish a full source state from its zero scalar shadow.

## Why it does not exclude the hostile

The identity is valid for every half-line source. Consider two positive atoms,
one before and one after the seam, whose complex Mellin contributions at some
off-seam point are `+1` and `-1`. Then

\[
F=1-1=0,
\qquad
B_L=1.
\]

Consequently

\[
E_{\mathrm{mov}}=0,
\qquad
E_{\mathrm{fix}}=-q,
\qquad
D_L=-q.
\]

The observer difference detects the cancellation exactly, but the hostile
state satisfies the seam law rather than violating it. Positive amplitudes can
produce the opposite complex contributions through their Mellin phases.

## Categorical meaning

The seam current is a naturality residual between two observers:

- transport the source and retain the fixed boundary;
- transport the observer contragrediently with the source.

Those paths are genuinely different, so their residual carries information.
But the residual is a universal cocycle, not an admissibility condition. To
gain RH force, another source law must constrain which values of `B_L` are
compatible across all seams, reciprocal sheets, and prime compositions.

## Next gate

The cheapest possible strengthening is not one more single-seam equation. It
is a compatibility law among seam cocycles. The two-prime shared-corner
identity already supplies composition; the new question is whether the full
family has a source-derived positivity, localization, or exactness property
that the two-atom hostile cannot satisfy.

Any candidate must be tested on the hostile packet before scalar evaluation.
If it merely reconstructs each `B_L` from the source, it adds provenance but
no zero exclusion.

## Disposition

The observer-difference wall is real and information-bearing, but it is not
yet transverse. The frontier moves from individual seam detection to a global
constraint on the entire seam-cocycle family.

