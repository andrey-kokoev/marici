# Minimal single-pole scalar grammars do not derive seventeen: WP1031

## Question

Does a symmetry-derived scalar representation naturally turn the surviving
WP1030 condition into one pole with \(m_{m pole}^2=17f^2\)?

## Radial representation test

For an \(O(N)\)-symmetric vector with radial coordinate \(\rho\),

\[
V=\frac\lambda4(\rho^2-f^2)^2,
\]

the radial curvature is

\[
m_\rho^2=2\lambda f^2.
\]

It is independent of \(N\). Representation multiplicity supplies angular
directions, not an \(N\)-fold radial mass coefficient.

## Equal-condensate spectator test

A single spectator pole \(S\) coupled equally to \(N\) condensates gives

\[
V_{\rm port}=\frac g2 S^2\sum_{a=1}^N f_a^2,
\qquad
f_a=f,
\]

and hence

\[
m_S^2=Ngf^2,
\qquad
\frac f{m_S}=\frac1{\sqrt{Ng}}.
\]

Setting \(N=17\) and \(g=1\) reproduces the WP1028 candidate, but the
response

\[
\frac{\partial}{\partial g}\frac1{\sqrt{Ng}}
=-\frac1{2\sqrt N,g^{3/2}}
\]

is nonzero. Unit coupling is an added normalization, not a consequence of the
multiplicity. At the same \(N=17\), the equally legal choice \(g=2\) gives
\(r=1/\sqrt{34}\), outside the reconstructed interval.

## Contextual partition and instrument

The WP1025 interval determines a nontrivial continuous interval of compatible
\(g\) values even after granting \(N=17\). Pole and vev measurements can
identify the product \(Ng\); they do not decompose it or establish
\(g=1\). A Ward identity, protected common kinetic normalization, or other
source law is still required.

## Smallest exact falsifier

The pair \(g=1,2\) at fixed representation and multiplicity preserves the
source grammar while moving the prediction from inside to outside the fitted
interval.

## Claim boundary

This closes the minimal renormalizable \(O(N)\) radial and equal-condensate
spectator constructors. It does not close protected supersymmetric, gauge, or
topological identities capable of fixing a single-pole mass coefficient.

## Disposition

Negative. The single-pole route relocates the continuous normalization into a
portal coupling rather than removing it.

Verification: uv run --with sympy python
research/flavor/checkers/wp1031_minimal_single_pole_seventeen_no_go.py
