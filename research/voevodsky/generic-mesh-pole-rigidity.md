# Generic-mesh pole rigidity

## Question

Why would positivity of every remainder Hankel cone force the general complex-zero spectral parameters to lie on the real rate axis?

## Claim boundary

The finite pole-rigidity mechanism, rational-to-real mesh extension, and phase-alias removal are established. The infinite zero expansion still requires one common analytic-continuation domain and locally uniform pole comparison.

## Two moment transforms

For a fixed mesh \(h\), the general-zero expansion has sampled bases

\[
y_j(h)=e^{-h\lambda_j}
\]

and formal moment transform

\[
A_h(z)
=
\sum_{n\geq0}a_n(h)z^n
=
\sum_j
\frac{w_j(h)}{1-y_j(h)z}.
\]

If all remainder Hankel matrices are positive and the endpoint asymptotic gives compact support, the same moments have a unique positive representation

\[
A_h(z)
=
\int
\frac{d\mu_h(y)}{1-yz}
\]

with \(\mu_h\) supported on a real compact interval.

The positive-measure transform has singular support only on the real reciprocal locus. Any exposed nonreal source pole is therefore incompatible with it.

## Grouping and collisions

Repeated zeros with the same \(\lambda\) must first be grouped. Their residues add multiplicity rather than creating distinct poles. The symmetry \(\rho\mapsto1-\rho\) also preserves

\[
\lambda_ho
=-\left(\rho-\frac12\right)^2.
\]

Conjugation creates the conjugate pole.

For distinct \(\lambda_j\neq\lambda_k\), a sampled collision requires

\[
e^{-h\lambda_j}=e^{-h\lambda_k}.
\]

Each pair contributes a discrete set of bad meshes. With countably many grouped rates, all collisions lie in a countable union of discrete sets. A generic real mesh separates every pole relevant in a bounded continuation region.

## Why rational meshes suffice

For each fixed finite rank and \(t\), localizer entries depend continuously on \(h>0\). If the matrix is positive for every positive rational \(h\), density of the rationals and closure of the PSD cone imply positivity for every positive real \(h\).

Thus one may choose a generic real mesh after proving positivity on rational meshes. This avoids the logical error of assuming that a countable bad set cannot contain all rational meshes.

## Pole rigidity

At a generic mesh, each grouped nonzero residue exposes a pole at

\[
z=y_j(h)^{-1}.
\]

Equality with the compact positive-measure transform forces this pole to lie on the real singular locus. Therefore

\[
y_j(h)=e^{-h\lambda_j}\in\mathbb R.
\]

A single mesh is insufficient: a nonreal phase can alias to \(-1\). But for arbitrarily small positive generic \(h\), continuity places \(e^{-h\lambda_j}\) near \(1\), so a real value must be positive. Writing \(\lambda_j=u+iv\), reality gives

\[
\sin(hv)=0.
\]

For sufficiently small \(h\), this forces

\[
v=0.
\]

Hence every source rate is real.

## Xi consequence

For

\[
\rho=\beta+i\gamma,
\qquad
\lambda_ho
=-\left(\rho-\frac12\right)^2,
\]

one has

\[
\operatorname{Im}\lambda_ho
=-2\left(\beta-\frac12\right)\gamma.
\]

Nontrivial zeros have \(\gamma\neq0\). Therefore reality of \(\lambda_ho\) forces

\[
\beta=\frac12.
\]

This identifies why remainder Hankel positivity already has RH strength.

## Remaining analytic gate

The finite rational-function argument does not by itself apply to the infinite zero set. A complete proof must establish:

1. locally uniform convergence of the grouped zero expansion near the moment disk;
2. analytic continuation of both transforms to one common domain;
3. nonvanishing grouped residues for generic small meshes;
4. absence of cancellation by additional completed terms;
5. pole identification in every bounded part of the continuation domain.

Without these, equality of Taylor coefficients near zero cannot be promoted silently to global pole identity.

## Disposition

The logical core is now explicit. Remainder Hankel positivity constructs a compact real spectral measure; analytic continuation must show that the source poles are its poles; generic meshes then eliminate collisions and phase aliases; real rates force the critical line. The unresolved object is the common meromorphic comparison, not another finite matrix inequality.

## Verification

- `research/voevodsky/generic-mesh-pole-rigidity-v1.json`
- `research/voevodsky/checkers/check_generic_mesh_pole_rigidity.py`
- `research/voevodsky/results/generic_mesh_pole_rigidity.json`
