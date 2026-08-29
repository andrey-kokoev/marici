# Zero-sieve factorization is generator-wise line semi-invariance

## Problem

The categorical RH certificate requires a factorization from the present zero
object into the full behavioral zero object. This factorization can be tested
on source generators without enumerating every source word.

Let \(\mathcal E\) be the completed state object, let \(\mathcal L\) be the
determinant line, and let

\[
r:\mathcal E\longrightarrow\mathcal L
\]

be the present readout. For a source generator \(g\), write
\(F(g):\mathcal E\to\mathcal E\).

The present kernel propagates through \(g\) exactly when

\[
\ker r\subseteq\ker(rF(g)).
\]

## Line-factor criterion

Assume \(r\) is an epimorphism onto the declared line object. Then the following
are equivalent:

1. \(\ker r\subseteq\ker(rF(g))\);
2. there is a unique line endomorphism
   \(\lambda_g:\mathcal L\to\mathcal L\) such that
   \[
   rF(g)=\lambda_g r.
   \]

Indeed, the kernel inclusion says that \(rF(g)\) descends through the quotient
of \(\mathcal E\) by \(\ker r\). Since that quotient is \(\mathcal L\), the
descended map is \(\lambda_g\). Epimorphy of \(r\) gives uniqueness. The reverse
implication is immediate.

Thus zero propagation is a semi-invariance law for the readout line. It is not
invariance of the state and does not require \(F(g)\) to be invertible.

## Extension from generators to words

Let \(G\) be a generating family for the source action category. Suppose every
\(g\in G\) has a line factor \(\lambda_g\). For a composable word

\[
w=g_n\cdots g_1,
\]

define

\[
\lambda_w
=
\lambda_{g_n}\cdots\lambda_{g_1},
\]

with the appropriate base restrictions when the line varies over objects.
Then induction gives

\[
rF(w)=\lambda_w r.
\]

Consequently,

\[
r(x)=0\quad\Longrightarrow\quad rF(w)(x)=0
\]

for every admitted word \(w\). This constructs the zero-sieve factorization.

If the action category has relations, the line factors must satisfy the same
relations. For two presentations \(w=w'\), one needs

\[
\lambda_w=\lambda_{w'}.
\]

This is the line-valued coherence gate. A family of generator factors that
fails one relation does not define a zero sieve.

## Adams subcategory

For the prime-power Adams arrow \((r,k):k\to rk\), the geometric and Euler
layers already provide the positive scalar

\[
\rho_r(p,k)
=
\frac1r p^{-(r-1)k/2}.
\]

Its composition law is

\[
\rho_s(p,rk)\rho_r(p,k)=\rho_{sr}(p,k).
\]

Therefore the Adams subcategory already has the required line-valued
semi-invariance cocycle at the scalar and moving-seam levels. Once the
type-fiber maps satisfy

\[
A_{s;p,rk}A_{r;p,k}=A_{sr;p,k}
\]

and the readout respects their tensor assembly, the full Adams generator obeys

\[
r\Psi_{r;p,k}
=
\rho_r(p,k)\,r.
\]

Hence the present kernel propagates through every Adams word.

This is a genuine partial construction of the RH zero sieve: the Adams
directions close after the type-fiber functor is supplied. It does not prove
propagation through Fourier, endpoint, seam, Green, or archimedean generators.

## Non-epic readouts

If \(r\) is not epic, kernel inclusion only produces an endomorphism of
\(\operatorname{im}r\), not necessarily an endomorphism of the declared line.
Promoting that partial factor to \(\mathcal L\) adds an extension choice.

The honest replacement is the image factorization

\[
\mathcal E\twoheadrightarrow\operatorname{im}r
\hookrightarrow\mathcal L.
\]

Zero propagation is then semi-invariance of \(\operatorname{im}r\). The
determinant bridge must separately show that this image is the intended
nondegenerate line. This prevents a zero readout from passing the criterion
vacuously.

## Generator table required for RH

The source action must now expose a finite or controlled generating table:

| Generator class | Required line factor | Current status |
|---|---|---|
| Adams grade change | \(\rho_r(p,k)\) | scalar cocycle constructed; type lift open |
| moving seam | identity after reassembly | constructed |
| Fourier--Poisson | source eigencharacter or typed line map | local fiberwise naturality constructed |
| endpoint incidence | source-derived multiplier | open |
| archimedean attachment | gamma-line multiplier | open |
| cross-sector Green link | relative line map | open |
| reciprocal sewing | anti-linear or conjugate line comparison | typed comparison open |

The exact table must be refined to the admitted generator presentation. The
point is structural: every row needs a line factor, and every defining relation
needs the matching multiplier identity.

## Hostile tests

1. A map preserving \(\ker r\) only after scalar aggregation fails the typed
   generator test.
2. Two equal action words with unequal line factors violate the source
   relations and destroy the sieve.
3. A non-epic or zero readout can satisfy kernel inclusion vacuously but cannot
   supply the determinant bridge.
4. A phase perturbation of an Adams coefficient preserves magnitude while
   changing the line cocycle; it must be an authorized coboundary.
5. Cutoffwise factors whose norms or domains do not survive completion fail to
   define a completed zero sieve.

## Consequence

The zero-sieve problem has been reduced from all future probes to two bounded
tasks:

1. construct a line semi-invariance factor for each source generator;
2. verify those factors on the defining relations and through completion.

The Adams residue supplies the first nontrivial multiplier family. The next
decisive constructor is the endpoint or archimedean line factor, because it is
needed to connect the arithmetic Adams sieve to the completed determinant
readout.

## Verdict

Zero-sieve factorization is equivalent, under an epic line readout, to
generator-wise semi-invariance of that line. The Adams coefficient cocycle is
already the correct semi-invariance character for the grade-changing
subcategory. Categorical RH now asks for the remaining generator characters,
their relation coherence, and completion stability.
