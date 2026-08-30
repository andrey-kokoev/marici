# Connected prime flux requires logarithm before polarization

Author: marici.Grothendieck

## 1. The normalization mismatch

The reciprocal stopped-Dirichlet ingress

\[
 a_N(z)=
 \begin{pmatrix}
 N^{-1/2-iz}\\
 N^{-1/2+iz}
 \end{pmatrix}
\]

has polarized Dirac flux

\[
 J_N(z,w)
 =\frac{2i}{N}
 \sin((\bar w-z)\log N).
\]

By contrast, the prime-power contribution to the centered Weil/Pick kernel
has arithmetic coefficient

\[
 \frac{\Lambda(N)}{\sqrt N}.
\]

After division by the spectral difference, its diagonal scale is

\[
 \frac{\Lambda(N)\log N}{\sqrt N},
\]

not \(\log N/N\). Therefore

\[
\boxed{
\text{raw Dirichlet Gram flux}
\ne
\text{Weil prime-power flux}.}
\]

The ratio \(\Lambda(N)\sqrt N\) is source-dependent, unbounded, and supported
only on prime powers. It cannot be absorbed into a fixed boundary metric.

## 2. The order of operations is forced

The aggregate amplitude is

\[
 \zeta(s)=\sum_{N\ge1}N^{-s}
\]

in its convergence chamber. Its connected determinant-line current is

\[
 -\frac{\zeta'(s)}{\zeta(s)}
 =\sum_{N\ge2}\Lambda(N)N^{-s}.
\]

The logarithm is nonlinear. Consequently it must be taken before forming a
Gram square. Polarizing the aggregate labels first irreversibly produces the
wrong \(1/N\) normalization.

The faithful sequence is

\[
\boxed{
\text{aggregate amplitude}
\to\text{logarithmic connected current}
\to\text{prime-power coefficient measure}
\to\text{boundary polarization}.}
\]

This is the determinant-line analogue of the distinction between moments and
cumulants: connected data are not recovered by taking an ordinary Gram matrix
of aggregate features.

## 3. Formally normalized connected spinor

The exact prime-power coefficient can be represented formally by

\[
 b_N(z)=
 \sqrt{\Lambda(N)}\,N^{-1/4}
 \begin{pmatrix}
 e^{-iz\log N}\\
 e^{iz\log N}
 \end{pmatrix},
 \qquad \Lambda(N)>0.
\]

Its polarized flux is

\[
\boxed{
 \widetilde J_N(z,w)
 =\frac{2i\Lambda(N)}{\sqrt N}
 \sin((\bar w-z)\log N).}
\]

Hence

\[
 \frac{\widetilde J_N(z,w)}{i(\bar w-z)}
 =
 \frac{2\Lambda(N)\log N}{\sqrt N}
 \operatorname{sinc}((\bar w-z)\log N),
\]

which has the required arithmetic normalization.

This formula does not yet construct a physical boundary Hilbert space. The
square root appears only after the positive prime-power coefficient measure
has been derived by the logarithmic connected transform.

## 4. Why this is not a repair of the raw packet

There is no labelwise constant operator sending \(a_N\) to \(b_N\). The
required multiplier

\[
 \sqrt{\Lambda(N)}\,N^{1/4}
\]

vanishes away from prime powers and grows along them. It changes both support
and Hilbert scale.

Therefore the connected boundary is a new typed object: a determinant-line
or cumulant object derived from the aggregate Euler amplitude. Treating it as
the same label Hilbert space with adjusted weights would erase the nonlinear
source operation that creates prime support.

## 5. The remaining sign problem

The isolated prime-power coefficient measure is positive, but in the Weil
explicit formula its contribution has an orientation relative to the gamma
and endpoint terms. Positivity of the prime feature space alone therefore
does not imply positivity of the completed boundary form.

The next required identity must place

\[
 \text{archimedean current}
 \quad\text{and}\quad
 \text{connected prime flux}
\]

in one Green form with the exact completion signs. Only the combined form can
define a self-adjoint boundary relation.

## 6. Infinite-energy obstruction

Even the connected diagonal weights do not sum without testing or damping:

\[
 \sum_{N\ge2}\frac{\Lambda(N)}{\sqrt N}
\]

diverges. Thus \(b_N\) is not a single square-summable boundary vector. The
correct object is distributional on the logarithmic test algebra, or a
weighted analytic boundary space whose damping is fixed by the test vector.

This agrees with the explicit formula: the prime current exists naturally as
a distribution paired with compactly supported or sufficiently decaying
logarithmic tests, not as an unweighted vector in \(\ell^2\).

## 7. Revised next target

Construct the connected prime boundary first as a positive operator-valued
distribution

\[
 d\Sigma_{\mathrm{prime}}
 =\sum_{N\ge2}
 \frac{\Lambda(N)}{\sqrt N}
 |N,+-\rangle\langle N,+-|\,\delta_{\log N},
\]

with reciprocal flux orientation retained. Then derive the archimedean
completion current in the same boundary triple and test whether the full
Green relation is isotropic and maximal.

The sharp falsifier is a normalization, support, or sign mismatch between
this connected flux and the exact Weil kernel on one compactly supported
test pair.

## 8. Scope

The mismatch, forced order of operations, formally normalized connected
spinor, and distributional divergence are exact. No source-derived GNS
completion of the connected current, combined archimedean Green identity,
maximal relation, self-adjoint operator, or RH proof is claimed.
