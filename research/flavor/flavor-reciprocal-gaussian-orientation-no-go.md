# Same-family Gaussian mediation cannot generate the oriented selector

Work package: WP607  
Owner: marici.Figueiredo

## Bounded question

Can a reciprocal Gaussian mediator acting on one cyclic operator family
generate the reflection-breaking carrier required by WP604, and what is the
smallest Gaussian escape?

The no-go domain contains one family of three labelled source channels
collected in (O), any finite set of heavy Gaussian mediator coordinates
(X), a real symmetric invertible heavy Hessian (H), and unrestricted
linear source couplings (G):

\[
V_H={1\over2}X^T H X+X^T G O.
\]

The one-operator-family restriction is load-bearing.

## Exact same-family obstruction

Eliminating the heavy coordinates gives

\[
C=-G^T H^{-1}G.
\]

The effective same-family kernel (C) is necessarily symmetric. A general
real three-channel kernel invariant under cyclic relabelling has the form

\[
C=\begin{pmatrix}
a&b&c\\
c&a&b\\
b&c&a
\end{pmatrix}.
\]

Reciprocity imposes (b=c). That equality also makes the kernel invariant
under a transposition. Call reciprocal Gaussian mediation RGM. At the
same-family bilinear level,

\[
\mathrm{RGM}+C_3\Longrightarrow S_3.
\]

The smallest hostile target has (a=0,b=1,c=0). It is cyclic but
nonsymmetric and reflection-breaking, so it cannot equal any same-family
reciprocal Gaussian Schur complement. Adding mediators does not help because
the sum remains symmetric.

## Exact typed bipartite escape

Reciprocity does not require the cross-block between two inequivalent
operator families to be symmetric. For cyclic families (A) and (B), the
full kernel

\[
\mathcal C=\begin{pmatrix}0&K\\K^T&0\end{pmatrix}
\]

is symmetric for arbitrary (K). Taking (K) to have clockwise coefficient
one and counterclockwise coefficient zero gives an exactly cyclic,
reflection-breaking cross interaction while the complete response remains
reciprocal. The reverse process occupies the transposed (B)-to-(A) block;
it is not a reflection within the typed (A)-to-(B) experiment.

Thus the smallest Gaussian escape requires two physically inequivalent and
experimentally distinguishable channel families. Calling the same channels
by two names would only duplicate presentation data.

## Non-Gaussian alternative

A non-Gaussian cyclic vertex also escapes the same-family obstruction. For
example,

\[
T=x_1x_2^2+x_2x_3^2+x_3x_1^2
\]

is invariant under the three-cycle and changes under a transposition. This is
an algebraic escape, not yet a physical flavor architecture. A completion
must supply charges for which its Hermitian version is CP even, prove
stability and decoupling, and derive its Yukawa portal independently.

## Instrument consequence

Masses, partial widths and an untyped two-port interference record do not
certify which cross-family orientation was used. In the Gaussian escape, the
minimum criticism resolves the (A)-to-(B) clockwise and counterclockwise
channels separately. In the non-Gaussian escape, it instead requires a cyclic
three-point observable. Either route needs a calibrated reversal-odd
difference.

The required experiment must measure, in one common frame:

- mediator masses and the two-point width/interference packet;
- either two inequivalent cross-channel families or a cyclic three-point
  amplitude;
- the corresponding reversal-odd difference with calibrated acceptance and
  background;
- weak-basis-invariant matching from the same source vertex to `physical16`.

The smallest exact falsifier is a vanishing reversal-odd record when the
source predicts it. A formal directed block or cubic coefficient is
insufficient: the physical detector channel must retain family typing and
ordering, and its uncertainty interval must exclude zero.

## Disposition

WP604 is not realized by a reciprocal mediator acting on one operator family.
Its smallest still-reciprocal escape is a typed bipartite source with two
inequivalent channel families; a non-Gaussian cyclic vertex is the
alternative. This narrows the architecture without selecting a fitted scalar.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp607_reciprocal_gaussian_orientation_no_go.py

The generated result is
research/flavor/results/wp607_reciprocal_gaussian_orientation_no_go.json.
