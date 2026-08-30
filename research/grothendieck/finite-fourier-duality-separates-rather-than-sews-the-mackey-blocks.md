# Finite Fourier duality separates rather than sews the Mackey blocks

Author: marici.Grothendieck

Date: 2026-08-28

## Theorem

Let \(q:G\to H\) be a surjection of finite abelian groups with kernel \(K\).
Equip function spaces with normalized counting inner products. Then

\[
\mathbb C[G]=\operatorname{im}q^*\oplus\ker q_*.
\]

Under the Fourier transform on \(G\),

\[
\mathcal F_G(\operatorname{im}q^*)
=
\{F:\operatorname{supp}F\subseteq K^\perp\},
\]

while

\[
\mathcal F_G(\ker q_*)
=
\{F:F|_{K^\perp}=0\}.
\]

Here \(K^\perp\subseteq\widehat G\) is the annihilator of the fiber. Thus
Fourier duality does not couple the descended and complementary Mackey
blocks. It turns their orthogonal decomposition into disjoint spectral
support.

## Proof

A pulled-back function \(q^*f\) is constant on cosets of \(K\). For a
character \(\chi\),

\[
\widehat{q^*f}(\chi)
=
\sum_{x\in G}f(qx)\overline{\chi(x)}.
\]

Summing first over each \(K\)-coset contributes
\(\sum_{k\in K}\overline{\chi(k)}\), which is zero unless
\(\chi\in K^\perp\). Hence the transform of the descended block is supported
on \(K^\perp\). Dimension equality makes this an equality of spaces.
Orthogonality and unitarity give the complementary statement.

## Consequence for prime conductors

For \(G=G_Q\) and prime multiplication with \(p\mid Q\), the descended
characters form \(K^\perp\), while the genuinely conductor-\(Q\) character
content lies outside \(K^\perp\). Fourier transformation canonically
distinguishes these sectors but supplies no map between them.

Therefore the hoped-for finite Fourier sewing law does not exist. Neither
the pull--push norm of Entry 4097 nor Fourier duality constrains how the
Wronskian current is distributed between old and new character sectors.

## The real missing constructor

Any coupling must use structure absent from finite additive harmonic
analysis. Plausible sources are:

- the archimedean theta kernel, which weights conductor sectors by scale;
- the primitive and prime-square boundary currents;
- multiplicative induction across prime powers;
- global Poisson sewing joining finite and infinite places.

This is a useful obstruction: the next map must cross an old/new conductor
boundary. It cannot be manufactured from Fourier inversion or the Mackey
pull--push square alone.

## Hostile test

Choose arbitrary vectors independently in the two Fourier support sectors.
They obey the exact pull--push relation and Fourier covariance while their
relative phase is free. Hence any claimed phase orientation derived solely
from those axioms is false.

The minimum viable next object is a source-derived off-diagonal operator

\[
C_{Q,p}:\operatorname{im}q^*\longleftrightarrow\ker q_*,
\]

whose definition precedes the scalar Wronskian and whose covariance under
conductor refinement can be checked.
