# Messenger-topology RG bifurcation: WP663

## Question

Does WP651's matched \(J_n,J_m\) word packet determine the messenger
contribution to WP662's scalar flow?

## Two constructors

In the spin-one representation, let \(J_n=n_iJ_i\) and \(J_m=m_iJ_i\).
A shared messenger multiplet can have field-dependent mass

\[
\mathcal M_s=M I+y_nJ_n+y_mJ_m.
\]

Writing

\[
R=y_n^2|n|^2+y_m^2|m|^2+2y_ny_m(n\mathbin\cdot m),
\]

its exact fourth trace is

\[
\operatorname{Tr}\mathcal M_s^4=3M^4+12M^2R+2R^2.
\]

Two disjoint messenger multiplets instead give

\[
\operatorname{Tr}(MI+y_nJ_n)^4+
\operatorname{Tr}(MI+y_mJ_m)^4
=6M^4+12M^2(y_n^2|n|^2+y_m^2|m|^2)
+2(y_n^4|n|^4+y_m^4|m|^4).
\]

Both architectures can carry independently adjustable tree-level \(J_n\) and
\(J_m\) coefficients. Their loop support is different.

## Exact obstruction

At unit parameters the shared constructor additionally generates

\[
n\mathbin\cdot m,\qquad
|n|^2(n\mathbin\cdot m),\qquad
|m|^2(n\mathbin\cdot m).
\]

These terms are odd under either individual triplet flip and lie outside
WP662's flip-even six-parameter support. The disjoint constructor generates no
cross term. Thus the same low-energy word capacity does not determine the
messenger-induced RG completion.

## Disposition

WP662 remains the complete scalar-only flow. Messenger completion cannot be
obtained from WP651's matched coefficients: a messenger topology and symmetry
charge assignment must first be frozen independently. This is another exact
constructor kernel, not a flavor selector.

The smallest falsifier of a claimed flip-even completion is a nonzero
coefficient of \(n\mathbin\cdot m\).

Reproduce with: uv run --with sympy python research/flavor/checkers/wp663_messenger_topology_rg_bifurcation.py

Generated result: results/wp663_messenger_topology_rg_bifurcation.json.
