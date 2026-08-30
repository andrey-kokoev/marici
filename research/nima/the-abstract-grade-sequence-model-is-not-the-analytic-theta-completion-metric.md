# The abstract grade sequence model is not the analytic theta completion metric

## Required correction

The quadratic band operator
\[
\mathfrak J
=
4N^2+2N-S(8N+6I)+4S^2
\]
is a valid closed operator on an abstract orthonormal coefficient space \(\ell^2(\mathbb N_0)\).

However, the analytic Gaussian grades
\[
e_k(x)=X^ke^{-X},
\qquad
X=\pi x^2,
\]
are neither orthogonal nor uniformly normalized in the source \(L^2(dx)\) metric.

Therefore the map
\[
\varepsilon_k\longmapsto e_k
\]
is not automatically bounded from the abstract coefficient \(\ell^2\) space into the analytic theta carrier.

The previous compact-embedding statement applies only to the abstract \(N^2\) graph model. It does not establish compactness of the analytic completion domain.

## Exact norm growth

On the full line,
\[
\|e_k\|_{L^2(dx)}^2
=
\int_{\mathbb R}
(\pi x^2)^{2k}e^{-2\pi x^2}\,dx.
\]

Using the Gaussian moment formula,
\[
\|e_k\|^2
=
\frac{\Gamma(2k+\tfrac12)}
{2^{2k+\frac12}\sqrt\pi}.
\]

This grows factorially with \(k\). In particular, the synthesis map from unweighted coefficient \(\ell^2\) cannot be bounded.

The cross-Gram entries are
\[
\langle e_j,e_k\rangle
=
\frac{\Gamma(j+k+\tfrac12)}
{2^{j+k+\frac12}\sqrt\pi},
\]
so the source metric is a Hankel moment Gram, not the identity.

The odd basis
\[
o_k=xX^ke^{-X}
\]
has an analogous shifted Gamma Gram.

## Canonical analytic completion operator

The source-native realization should be defined directly on the positive-ray Hilbert space.

Let
\[
A=x\partial_x.
\]
Under logarithmic half-density transport,
\[
A+\frac12
\]
is the translation generator in \(u\). Its closed realization is fixed by that unitary transport.

The even completion operator is
\[
P_{\mathrm{even}}=A(A+1)
\]
on its natural second-order graph domain, while the odd connection realization is
\[
P_{\mathrm{odd}}=(A-1)A
\]
on the degree-shifted domain.

The polynomial Gaussian grades are a common algebraic core candidate, and the infinite band formula records the action on that nonorthogonal core. It does not define the metric.

## No automatic compactness

In logarithmic coordinate \(u\), the dilation generator becomes a constant-coefficient derivative. On the full line, the Sobolev embedding
\[
H^2(\mathbb R)\hookrightarrow L^2(\mathbb R)
\]
is continuous but not compact because translations can escape.

Therefore analytic compactness cannot follow from grade growth alone. It requires additional confinement, such as:

- Gaussian multiplication retained in the graph norm;
- a compact parameter interval;
- a label-weighted direct sum with a confining potential;
- or a source boundary condition preventing translation escape.

This is a direct instance of the earlier cell-frame-loss obstruction.

## What remains valid

The exact coefficient identity
\[
Pv_k
=
2k(2k+1)v_k-(8k+6)v_{k+1}+4v_{k+2}
\]
remains correct.

The common parity-shifted front matrix \(J_3\) remains correct.

The abstract band operator remains a useful bookkeeping model and a possible coefficient completion if a source-derived Gamma/Fock reweighting proves equivalence.

What is withdrawn is any claim that unweighted coefficient \(\ell^2\) is already the analytic theta topology, or that its compact graph embedding proves analytic compactness.

## Correct comparison theorem

Let
\[
\Gamma_{\mathrm{even}}
=
\bigl(\langle e_j,e_k\rangle\bigr)_{j,k\ge0}
\]
and similarly \(\Gamma_{\mathrm{odd}}\). The coefficient operator must be audited as a form on these Gram completions.

A legitimate coefficient model requires:

1. closability of polynomial synthesis;
2. descent through any Gram radical;
3. closure of the band operator in the Gamma metric;
4. equivalence with the transported analytic graph norm;
5. uniform control under theta label synthesis.

## Hostile

A coefficient sequence can have unit unweighted \(\ell^2\) norm while concentrating at grade \(k\). Its analytic image then has norm \(\|e_k\|\), which diverges factorially. The abstract metric declares the sequence bounded while the analytic source norm explodes.

## Revised frontier

The next theorem is a Gamma-weighted coefficient realization, not merely label summability into \(\operatorname{Dom}N^2\).

Until that theorem is proved, the authoritative completion carrier is the analytic dilation graph domain transported by \(\mathcal M_n\), and the grade matrices are core coordinates only.
