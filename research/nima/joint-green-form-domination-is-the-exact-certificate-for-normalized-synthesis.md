# Joint Green-form domination is the exact certificate for normalized synthesis

## Pseudoinverse-free certificate

Let \(\mathcal A\) be the arithmetic coefficient carrier, \(\mathcal V_s\) the common Green form domain, and
\[
S_s:\mathcal A\longrightarrow\mathcal V_s^*
\]
the complete assembled unweighted boundary synthesis.

Before any inverse or pseudoinverse notation, require two properties.

### Radical annihilation

For every coefficient \(c\in\mathcal A\) and every Green-radical vector
\[
h\in\mathcal N_s
=
\{h\in\mathcal V_s:b_s[h,h]=0\},
\]
require
\[
\langle S_sc,h\rangle=0.
\]
This is precisely what lets \(S_s\) descend to the reduced Green quotient.

### Joint form domination

For every compact parameter set \(C\), there must be one constant \(M_C\) such that, for all \(s\in C\), all cutoffs, all \(c\in\mathcal A\), and all \(h\in\mathcal V_s\),
\[
|\langle S_sc,h\rangle|^2
\le
M_C^2\|c\|_{\mathcal A}^2\,b_s[h,h].
\]

This inequality is the exact source-level certificate. It simultaneously proves radical annihilation, but retaining radical annihilation as a separately reported gate makes failures more diagnostic.

## Riesz representation consequence

After quotienting by \(\mathcal N_s\) and completing in the Green norm, the functional
\[
[h]\longmapsto\langle S_sc,h\rangle
\]
is bounded with norm at most \(M_C\|c\|_{\mathcal A}\). Riesz representation therefore gives a unique vector \(A_sc\) in the reduced Green Hilbert space such that
\[
\langle A_sc,[h]\rangle_{b_s}
=
\langle S_sc,h\rangle,
\]
and
\[
\|A_s\|\le M_C.
\]

Only at this point may one write symbolically
\[
A_s=B_s^{\dagger/2}S_s.
\]
The bounded normalized synthesis is a theorem extracted from the form inequality, not a prior operator expression.

Combined with the Euler diagonal,
\[
T_s=A_sD_E
\]
is compact, with the already established grade Schatten ideals.

## Why channelwise bounds do not compose automatically

Write the assembled boundary carrier schematically as
\[
\mathcal V
=
\mathcal V_{\mathrm{tail}}
\oplus
\mathcal V_{\mathrm{seam}}
\oplus
\mathcal V_{\mathrm{end}}
\oplus
\mathcal V_{\infty}.
\]
The Green form need not be the orthogonal sum of its channel restrictions. It may contain cross terms and a joint radical invisible on every coordinate axis.

Separate estimates
\[
|\langle S_i c,h_i\rangle|^2
\le
M_i^2\|c\|^2 b_i[h_i,h_i]
\]
do not imply the joint estimate unless one additionally proves a coercive comparison between the assembled form and the sum of channel energies.

The complete inequality must therefore be tested after seam, endpoint, archimedean, primitive, square, connected, and reciprocal data have all been assembled.

## Mandatory off-diagonal-radical hostile

Let the boundary carrier be
\[
\mathcal V=\mathbb C^2
\]
with channel axes \(\mathcal V_1=\mathbb C\oplus0\) and \(\mathcal V_2=0\oplus\mathbb C\). Define
\[
b((x,y),(x,y))=|x+y|^2.
\]
On each channel separately,
\[
b((x,0),(x,0))=|x|^2,
\qquad
b((0,y),(0,y))=|y|^2.
\]

Let \(\mathcal A=\mathbb C\), and define assembled synthesis by
\[
\langle Sc,(x,y)\rangle=c(x-y).
\]
Each channel restriction obeys the uniform estimate with constant \(1\):
\[
|cx|^2\le|c|^2|x|^2,
\qquad
|cy|^2\le|c|^2|y|^2.
\]

But the off-diagonal vector
\[
h=(1,-1)
\]
lies in the joint Green radical:
\[
b[h,h]=0,
\]
while
\[
\langle Sc,h\rangle=2c.
\]
Thus every channel audit passes and the assembled synthesis still fails radical annihilation and joint form domination.

This hostile is the minimal proof that cross-channel Green geometry cannot be reconstructed from isolated channel bounds.

## A sufficient channel-to-joint theorem

Channelwise estimates become sufficient only if the source supplies a coercive assembly inequality. For example, if
\[
\sum_i b_{s,i}[h_i,h_i]
\le
C_C\,b_s[h,h]
\]
uniformly on compact parameter sets, and
\[
\langle S_sc,h\rangle
=
\sum_i\langle S_{s,i}c,h_i\rangle,
\]
then Cauchy–Schwarz gives a joint bound with a controlled constant.

The direction of this coercive inequality matters. An upper bound of joint energy by channel energy does not rule out a joint radical and is insufficient.

## Uniformity and transport

The certificate must use one \(M_C\) uniformly across:

- all finite cutoffs;
- the parameter patch \(C\);
- direct and reciprocal sheets;
- the declared quotient identifications.

Cutoff inclusion and Real transport must preserve both pairings:
\[
b_{Y,s}[\iota h,\iota h]=b_{X,s}[h,h],
\]
and
\[
\langle S_{Y,s}j c,\iota h\rangle
=
\langle S_{X,s}c,h\rangle,
\]
with conjugate variants for the Real map. Otherwise boundedness may be presentation-dependent.

## Exact consequence and exact limitation

Passing this gate proves:

1. descent through the Green radical;
2. bounded normalized unweighted synthesis;
3. compact normalized Euler-weighted synthesis;
4. Fredholm discreteness and finite algebraic multiplicity at nonzero spectral points;
5. preservation of primitive, square, and connected Schatten grades.

It does not prove:
\[
1\notin\sigma(K_s).
\]
The gap at \(1\), and hence off-seam zero exclusion, remains a separate RH-bearing estimate.

## Revised first missing inequality

The next source theorem is now exact:

> prove the complete assembled Green-form domination inequality for the unweighted theta boundary synthesis, uniformly on compact parameter sets and finite cutoffs, after every channel and cross-channel term is present.

The corresponding checker must report radical annihilation before operator norm, and joint-bound failure before any Schatten or determinant conclusion.
