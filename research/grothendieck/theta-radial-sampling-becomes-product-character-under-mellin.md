# Radial sampling becomes a product character under Mellin rotation

## Bounded question

Can evaluation at the moving arithmetic loci `q=pe^S` be converted exactly
into a fixed transform while retaining the faithful product--ratio ports?

## Evaluation-to-Mellin identity

Let `F_rho(q)` be any integrable radial profile with respect to `dq/q`, and
let `p>0`. Then

\[
 \int_{\mathbb R}e^{ixS}F_\rho(pe^S)\,dS
 =p^{-ix}\int_0^\infty q^{ix}F_\rho(q)\,\frac{dq}{q}.
\]

Indeed, substitute `q=pe^S`.  Writing

\[
 \mathcal M F_\rho(x)
 =\int_0^\infty q^{ix}F_\rho(q)\,\frac{dq}{q},
\]

gives the exact formula

\[
 \boxed{
 \mathcal F_S[F_\rho(pe^S)](x)
 =p^{-ix}\mathcal M F_\rho(x).}
\]

Thus the logarithmic Fourier transform is precisely the unitary Mellin
transform of radial dilation.

## Application to faithful pair coordinates

For a theta label pair, packet 130 gives

\[
 p=nm,
 \qquad \rho=|\log(m/n)|.
\]

After integrating the centered difference fiber and retaining its modular
seam terms, write the resulting radial profile as `F_(n,rho)(q)`.  Its
sum-coordinate transform has the form

\[
 \widehat g_n(x)
 =\sum_{p,\rho}w(p,\rho)
 p^{-ix}\mathcal M F_{n,\rho}(x),
\]

with the exact `C2` stabilizer weights from packet 130.

The product phase factorizes:

\[
 \boxed{p^{-ix}=(nm)^{-ix}=n^{-ix}m^{-ix}.}
\]

Arithmetic sampling has therefore become a tensor-product character.  The
only remaining coupling is in the ratio-dependent Mellin amplitude and its
seam completion.

## Bilinear-versus-Hermitian obstruction

A same-sheet product character is

\[
 n^{-ix}m^{-ix}=(nm)^{-ix}.
\]

By contrast, a Hilbert norm square of labelled amplitudes contains

\[
 n^{-ix}\overline{m^{-ix}}
 =n^{-ix}m^{ix}
 =(n/m)^{-ix}.
\]

Thus Mellin rotation exposes exactly the variance distinction of packet 122:

\[
 \boxed{
 \text{product character} = \text{bilinear same-sheet pairing},}
\]

whereas

\[
 \boxed{
 \text{ratio character} = \text{Hermitian opposite-sheet pairing}.}
\]

Reciprocal sewing must implement a genuine product--ratio quarter-turn before
the coefficient kernel can be interpreted as Gram-positive. Positivity of a
ratio-amplitude matrix alone would not repair the wrong character variance.

## What has and has not been solved

The continuous analytic step is solved:

\[
 \boxed{
 \text{moving radial evaluation}
 \xrightarrow{\text{log Fourier/Mellin}}
 \text{fixed Mellin amplitude times a product character}.}
\]

No RKHS choice is needed for this identity. However, it remains a bilinear
Mellin coefficient. The missing map must exchange product and ratio characters
while transporting the faithful ports and seam terms. The identity alone does
not establish the DPC.

## Next gate and falsifier

Compute the exact order-one reciprocal-sewing operator on the first nontrivial
product fiber `p=6`. In the faithful basis `rho=log6,log(3/2)`, test whether it
intertwines the same-sheet product character with the opposite-sheet ratio
character and preserves the normalized `C2` metric.

Failure of that intertwining identity falsifies the Gram-factor route before
any positivity test. If it intertwines, a negative determinant of the
transported `2x2` metric is the next falsifier.
