# Gaussian-mediator matching obstruction (WP264)

## Minimal microscopic repair

Let \(x\geq0\) denote the normalized commutator mixing invariant. Introduce
one stable real Gaussian mediator \(S\) with

\[
V_{\mathrm{UV}}(S,x)
=\frac{M^2}{2}(S-v)^2-gSx,
\qquad M^2>0.
\]

The mediator equation is

\[
S_*=v+\frac{g}{M^2}x.
\]

Exact tree-level elimination gives

\[
V_{\mathrm{eff}}(x)
=-gvx-\frac{g^2}{2M^2}x^2.
\]

The first term has the sign needed to move away from zero mixing. The induced
quadratic term always has the wrong sign for stabilization when the mediator
is stable and the coupling is real.

## Independent repair coefficient

Adding a direct operator \(b_0x^2\) changes the effective quadratic coefficient
to

\[
b_{\mathrm{eff}}=b_0-\frac{g^2}{2M^2}.
\]

An interior stable selector requires \(b_0>g^2/(2M^2)\). Thus the Gaussian
mediator does not derive WP262's missing positive coefficient; it requires a
new independently normalized source term.

The smallest exact witness uses \(M^2=4\), \(g=1\), and \(v=1\), producing
\(V_{\mathrm{eff}}=-x-x^2/8\) with curvature \(-1/4\).

## Scope and next gate

This is a tree-level theorem for one stable Gaussian mediator coupled linearly
to \(x\). It does not exclude nonlinear or multiple mediators, fermion-loop or
supersymmetric matching, or nonperturbative dynamics. Those are genuine added
source structures. A progressive successor must derive a positive stabilizing
term and its normalization before flavor readout, rather than inserting it to
obtain the desired angle.

Run `uv run --with sympy python
research/flavor/checkers/wp264_gaussian_mediator_matching.py` for exact
completion of the square, coefficient signs, counterterm bound, and hostile
witness.
