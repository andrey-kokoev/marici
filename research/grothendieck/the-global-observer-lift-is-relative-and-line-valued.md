# The global observer lift is relative and line-valued

## What is already constructed

For every finite place (p), restriction gives an isomorphism of test spaces

\[
J_p:\mathcal S(\mathbb Q_p)\longrightarrow\mathcal T_p,
\]

where (mathcal T_p) retains locally constant multiplicative data together
with the eventual valuation-tail constant encoding (phi_p(0)).

At the real place,

\[
J_\infty:\mathcal S(\mathbb R)\longrightarrow\mathcal T_\infty
\]

retains the matched full jets across zero. The algebraic restricted tensor
product

\[
\mathcal T_0(\mathbb A^\times)
=
\mathcal T_\infty
\mathop\otimes'_p(\mathcal T_p,\tau_p)
\]

exists, and the local restrictions assemble to

\[
J_0:\mathcal S(\mathbb A)
\longrightarrow
\mathcal T_0(\mathbb A^\times).
\]

Fourier--Tate covariance is therefore already defined at the algebraic
test-space level.

## Why an ordinary completed target fails

The primitive anomaly on unramified cutoffs is

\[
C_{1,X}(t)
=
2i\sum_{p\le X}p^{-1/2}\sin(t\log p).
\]

It has no cutoff-independent scalar limit for generic nonzero (t). Hence no
continuous scalar functional on the ordinary restricted-product topology can
simultaneously realize all finite primitive coordinates.

This is not failure of (J_0). It is failure of the proposed value type.

## Relative target

For (X\subset Y), retain the transition increment

\[
\Delta C_{1;X,Y}=C_{1,Y}-C_{1,X}
\]

and similarly (Delta C_{2;X,Y}). These obey the exact triangle law

\[
\Delta C_{j;X,Z}
=
\Delta C_{j;X,Y}
+
\Delta C_{j;Y,Z}.
\]

Thus the completed observer is naturally an affine torsor or line system over
(mathcal T_0), with primitive and square currents as transition
coordinates and the connected tail as an ordinary convergent coordinate.

Write this relative vessel schematically as

\[
\mathfrak T
=
(\mathcal T_0,\mathcal L,\Delta C_1,\Delta C_2,C_{\ge3},C_\infty).
\]

The actual observer lift has the type

\[
J^{\mathrm{rel}}:\mathcal S(\mathbb A)\longrightarrow\mathfrak T.
\]

It need not choose a global scalar origin for the anomaly line.

## Fourier naturality becomes a higher cell

The desired relation is not necessarily literal equality of scalar-valued
maps. Fourier--Tate transport acts on the line system and its transition
cocycles. Naturality is a line-valued comparison

\[
\eta:
J^{\mathrm{rel}}\mathcal F
\Longrightarrow
\mathcal F_{\mathrm{Tate}}J^{\mathrm{rel}},
\]

whose cutoff components must obey their own triangle coherence.

This is precisely a higher rung of the fourth tower. Treating (eta) as an
ordinary equation would silently choose a scalar trivialization that the
source does not supply.

## Seam and off-seam distinction

On the critical seam, the local Tate transitions are unitary, so the line
system has a canonical Hilbert direct limit even when no scalar phase
converges. Off the seam, the same transitions are not unitary in that metric.

Therefore the critical line is already distinguished at the level of the
relative observer target:

- on the seam, the anomaly torsor has unitary descent;
- off the seam, bounded or closable descent remains an additional theorem.

This still does not confine zeros. The distinguished determinant section may
vanish in a nontrivial line bundle or torsor. But it gives the observer lift
the correct type before any zero argument.

## Next exact gate

Construct the Fourier action on

\[
(\Delta C_1,\Delta C_2,C_{\ge3},C_\infty)
\]

and compute the naturality residual cutoffwise. The residual is accepted only
if it is a named central transition cocycle satisfying the triangle law; an
untyped scalar discrepancy fails.

Then determine whether the Poisson four-channel zero section is a canonical
line-valued pairing on (mathfrak T), rather than a scalar imposed after
choosing a chart.

## Falsifiers

The relative observer route fails if:

- a local restriction does not preserve its zero-boundary coordinate;
- restricted tensor products do not assemble;
- anomaly increments violate the triangle law;
- Fourier changes the transition class rather than transporting it;
- the completed section depends on the chosen cutoff trivialization;
- a scalar primitive limit is inserted to force naturality.

