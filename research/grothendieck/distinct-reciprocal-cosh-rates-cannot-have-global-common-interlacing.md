# Distinct Reciprocal Cosh Rates Cannot Have Global Common Interlacing

## Seam zero sets

A centered reciprocal packet with rate (q>0\) is

\[
F_q(z)=\cosh(qz).
\]

On the seam (z=it\),

\[
F_q(it)=\cos(qt).
\]

Its zeros are

\[
t_k(q)=\frac{(k+1/2)\pi}{q},
\qquad
k\in\mathbb Z.
\]

The number of zeros in \([-T,T]\) therefore satisfies

\[
N_q(T)=\frac{2q}{\pi}T+O(1).
\]

## Density obstruction

If two bi-infinite simple zero sequences globally interlace, their counting
functions on every interval differ by at most one up to endpoint convention.
In particular,

\[
N_{q_1}(T)-N_{q_2}(T)=O(1).
\]

But the asymptotic formula gives

\[
N_{q_1}(T)-N_{q_2}(T)
=\frac{2(q_1-q_2)}{\pi}T+O(1).
\]

This is bounded only when

\[
q_1=q_2.
\]

Hence distinct reciprocal cosh rates cannot have globally interlacing seam
zeros.

## Consequence for positive aggregation

A standard sufficient mechanism for positive combinations to preserve real
rootedness is common interlacing or proper position. That mechanism cannot
operate label by label for arithmetic reciprocal packets, because distinct
labels have distinct rates such as \(q_n=\log n\).

This explains why Aspect's two-prime positive sum can leave the seam even
though each summand is individually seam-rooted. The failure is structural,
not a bad choice of coefficients: the component zero densities are
incompatible.

## What remains possible

The all-label coherence law, if it exists, must act after a source-derived
regrouping that changes the elementary components. Viable levels include:

1. the continuous theta kernel after summing integer labels;
2. Poisson-paired scale bands rather than individual arithmetic rates;
3. a de Branges or canonical-system transfer whose elementary states share
   one spectral density;
4. the sectorwise Hardy phase current after outer subtraction.

It cannot be an ordinary common-interlacing theorem for the raw cosh packet
family.

## Falsifier

Any claimed common-interlacing proof must exhibit bounded difference of zero
counts for two distinct source rates. The linear density difference above is
an immediate contradiction.
