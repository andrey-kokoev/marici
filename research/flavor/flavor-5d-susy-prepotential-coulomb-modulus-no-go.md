# The supersymmetric prepotential removes the vertex spurion but restores a Coulomb modulus: WP788

## Question

Can five-dimensional supersymmetry derive both the WP787 cubic orientation
coefficient and the matter vertex from one gauge operation?

## Correct operator typing

Five-dimensional supersymmetric gauge theories admit cubic Coulomb-branch
prepotentials and, when required, supersymmetric Chern--Simons terms. Their
fixed-point and consistency structure is developed by
[Intriligator, Morrison, and Seiberg](https://arxiv.org/abs/hep-th/9702198).
Hypermultiplet loops can generate a supersymmetric Chern--Simons action, as
shown by [Kuzenko](https://arxiv.org/abs/hep-th/0609078).

This does join the Chern--Simons coefficient, vector-multiplet geometry, and
gauge-fixed matter charges in one source framework. It does not identify the
prepotential with the four-dimensional scalar potential used in WP787.

## Exact SU(4) ray

Let \(r=1/g_5^2\). On
\(T=\operatorname{diag}(1,1,1,-3)\), the cubic prepotential has the normalized
form

\[
\mathcal F(a)=6ra^2-4ka^3.
\]

Its second derivative is the Coulomb kinetic metric

\[
G(a)=12r-24ka.
\]

The transformation \((a,k)\mapsto(-a,-k)\) preserves \(G\). On the formal
fixed-point face \(r=0\), positivity requires

\[
-ka>0.
\]

Thus a fixed nonzero level orients an allowed half-ray relative to its sign.
But unbroken supersymmetry leaves the Coulomb potential identically zero:

\[
V_{\mathrm C}(a)=0.
\]

The operation selects a cone, not a point.

## Gauge-fixed matter vertex has the wrong selection content

A fundamental hypermultiplet has signed masses proportional to

\[
(a,a,a,-3a).
\]

The scalar mass squares are

\[
(a^2,a^2,a^2,9a^2).
\]

Extended gauge structure has removed the independent WP787 vertex coefficient
\(\eta\), and it fixes the relative threshold ratio to three. However, the
scalar operator is even under \(a\mapsto-a\), while its triplet--singlet
contrast is

\[
\Delta_{\mathrm{scalar}}=-8a^2.
\]

Two points \(a=-s\) and \(a=-2s\) belong to the same positive half-ray and
share the same level and relative threshold ratio, but their contrasts differ
by a factor four.

## Classification

The supersymmetric prepotential is a genuine parallelizer of topological
level, kinetic geometry, and gauge charge. It improves WP787 by eliminating
an arbitrary matter-vertex sign. It nevertheless fails the full selector:

- the cubic is kinetic/prepotential data, not the WP787 stabilizing potential;
- positivity chooses only a relative orientation half-ray;
- the Coulomb magnitude remains a flat modulus;
- the absolute threshold is proportional to \(\lvert a\rvert\);
- scalar spectroscopy reads the \(3:1\) ratio but not the sign;
- compactification and a signed physical16 instrument remain unspecified.

The next admissible source must lift the Coulomb modulus without introducing
a new arbitrary soft scale or boundary coefficient. It must preserve the
quantized level relation and yield a signed, calibrated threshold observable.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp788_5d_susy_prepotential_coulomb_modulus_no_go.py

Generated result:
research/flavor/results/wp788_5d_susy_prepotential_coulomb_modulus_no_go.json
