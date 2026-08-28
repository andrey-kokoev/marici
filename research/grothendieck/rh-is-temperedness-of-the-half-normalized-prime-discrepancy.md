# RH Is Temperedness of the Half-Normalized Prime Discrepancy

## Logarithmic source coordinate

Let

\[
E(x)=\psi(x)-x
\]

be the prime-power counting discrepancy and set

\[
u=\log x.
\]

The critical normalization is

\[
q(u)=e^{-u/2}E(e^u),
\qquad u\ge0.
\]

The exponent \(1/2\) is forced by the reciprocal center
\(s\leftrightarrow1-s\). It is also exactly the normalization that turns
the classical RH prime-counting bound into polynomial growth.

## Exact Laplace bridge

The multiplicative discrepancy current from the preceding result is

\[
D(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-\frac1{s-1}.
\]

For \(\Re s>1\),

\[
D(s)
=
1+s\int_1^\infty E(x)x^{-s-1}\,dx.
\]

With \(s=1/2+z\) and \(x=e^u\), this becomes

\[
D(1/2+z)
=
1+(1/2+z)
\int_0^\infty q(u)e^{-zu}\,du.
\]

Thus the connected prime current in the right sector is the Laplace transform
of the half-normalized discrepancy.

## Temperedness implies right-sector zero-freeness

Suppose \(q\) defines a tempered distribution supported in
\([0,\infty)\). Its Laplace transform is holomorphic for \(\Re z>0\):
after multiplication by \(e^{-zu}\), the positive real part supplies
exponential decay on the support.

The displayed identity then continues \(D(s)\) holomorphically throughout
\(1/2<\Re s<1\). But every zeta zero in that sector would give \(D\) a
pole. Hence no such zero exists. Reciprocal symmetry excludes zeros in the
left sector.

## RH implies temperedness

The classical von Koch consequence of RH is

\[
\psi(x)-x=O\bigl(x^{1/2}\log^2x\bigr).
\]

Therefore

\[
q(u)=O(u^2),
\]

so \(q\) is a tempered function and hence a tempered distribution.

Conversely, temperedness gives a holomorphic right-sector Laplace transform
and therefore zero-freeness there. With the standard functional equation and
critical-strip localization, this yields RH.

Consequently:

> RH is equivalent to the statement that the prime-power discrepancy becomes
> tempered after removal of exactly one half-unit of exponential growth.

## What the half-offset denotes

The critical shift is not merely where reciprocal coordinates look
symmetric. It is the regularity threshold separating two kinds of completed
source behavior:

- at or below the threshold, the normalized discrepancy is allowed
  polynomial growth and lives in the tempered boundary rigging;
- an off-line zero with real part \(1/2+a\) contributes an exponential mode
  of rate \(a\), which cannot inhabit that tempered boundary space.

In this sense an off-seam zero would be an impossible trajectory into the
declared source topology: it would require a state whose normalized boundary
current grows exponentially while still being treated as tempered.

## Connection with the additive theta defect

The theta lattice--Haar deficit is a positive self-dual additive source. The
prime discrepancy \(q\) is its connected multiplicative image after Fock
logarithm, differentiation, and half-density normalization.

The missing source theorem can now be stated without mentioning zeros:

> The canonical Fock--Mellin--Poisson comparison sends the completed theta
> deficit into a tempered half-normalized prime discrepancy.

If derived independently, this statement implies RH through the Laplace
bridge. It is harder to vary than a direct zero assertion because it names the
source operation, target topology, and precise normalization.

## Falsifier

A proposed proof fails if:

- temperedness is inferred from a bound already equivalent to RH;
- the half-normalization is inserted only after inspecting the critical line;
- primitive and continuum currents are separately divergent in the claimed
  target topology;
- the Laplace transform is defined by analytic continuation from
  \(-\zeta'/\zeta\) rather than from the source distribution;
- or an exponentially growing mode survives in \(q\).

