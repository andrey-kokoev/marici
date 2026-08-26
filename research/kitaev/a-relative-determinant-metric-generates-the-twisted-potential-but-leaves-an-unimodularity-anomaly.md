# A Relative Determinant Metric Generates the Twisted Potential but Leaves an Unimodularity Anomaly

Deutsch's question asks for a concrete source object whose logarithm could be
the twisted normalization potential. The minimal candidate is a pair of
source-derived metric lines: the repair and drift character lines at every
vertex.

Let

\[
L_v^+,
\qquad
L_v^-
\]

be one-dimensional character spaces with positive frame norms

\[
h_v^+,
\qquad
h_v^-.
\]

Define the relative metric coordinate

\[
P_v=\frac{h_v^+}{h_v^-},
\qquad
\phi_v=\log P_v.
\]

This is the simplest source-native candidate for the vertex potential.

## Character-preserving edge

Suppose an edge preserves the two character lines, with scalar amplitudes

\[
t_e^+:L_s^+\to L_t^+,
\qquad
t_e^-:L_s^-\to L_t^-.
\]

Its metric gains are

\[
g_e^+
=|t_e^+|\frac{h_t^+}{h_s^+},
\qquad
g_e^-
=|t_e^-|\frac{h_t^-}{h_s^-}.
\]

Therefore the relative gain is

\[
\Gamma_e
=\frac{g_e^+}{g_e^-}
=A_e\frac{P_t}{P_s},
\]

where

\[
A_e=\left|\frac{t_e^+}{t_e^-}\right|.
\]

Taking logarithms,

\[
\ell_e
=\phi_t-\phi_s+a_e,
\qquad
a_e=\log A_e.
\]

## Character-exchanging edge

Now suppose the edge exchanges the lines:

\[
u_e:L_s^-\to L_t^+,
\qquad
v_e:L_s^+\to L_t^-.
\]

Then

\[
g_e^+
=|u_e|\frac{h_t^+}{h_s^-},
\qquad
g_e^-
=|v_e|\frac{h_t^-}{h_s^+},
\]

so

\[
\Gamma_e
=A_eP_tP_s,
\qquad
A_e=\left|\frac{u_e}{v_e}\right|.
\]

Hence

\[
\ell_e
=\phi_t+\phi_s+a_e.
\]

## Unified law

With \(\varepsilon_e=+1\) for preserving edges and \(-1\) for exchanging
edges, both cases are

\[
\Gamma_e
=A_eP_tP_s^{-\varepsilon_e},
\]

or

\[
\ell_e
=\phi_t-\varepsilon_e\phi_s+a_e.
\]

This is exactly the desired twisted-potential formula plus a typed residual.

## The irreducible anomaly

Metric or vacuum normalization determines \(\phi_v\), but it does not force

\[
a_e=0.
\]

The residual is the relative determinant amplitude of the constructor on the
two character lines. Exact flatness requires relative unimodularity,

\[
A_e=1,
\]

edgewise, or weaker global cancellation of the \(a_e\) cocycle by a product
formula.

Thus the candidate roles separate cleanly:

- vacuum or tensor-unit data can fix the line metrics and potential origin;
- determinant transport supplies the edge anomaly;
- local \(\gamma\)-factors may be the amplitudes entering \(A_e\);
- an adelic product formula could cancel their loop sum;
- completion requires the remaining tail anomalies to be summable.

No one ingredient performs all jobs automatically.

## Counterfactual prediction

Perturb only the plus-character amplitude on one preserving edge by a positive
factor \(\lambda\):

\[
t_e^+\longmapsto\lambda t_e^+.
\]

Then

\[
a_e\longmapsto a_e+\log\lambda.
\]

Every loop using that edge acquires the corresponding signed log-holonomy
anomaly unless another source factor compensates it. The vertex potential is
not refitted. This is a genuine explanatory counterfactual.

## Candidate discrimination

This calculation rules out several shortcuts.

1. A vacuum norm alone fixes \(P_v\) but says nothing about \(A_e\).
2. A scalar determinant norm without character resolution cannot form the
   relative amplitude \(A_e\).
3. Scalar Tate convergence can hide different \((t_e^+,t_e^-)\) with the same
   product or trace.
4. A fitted vertex metric can absorb tree-edge gains but cannot erase chord
   anomalies without changing loop holonomy.

The best source candidate is therefore not one scalar. It is a typed pair:

\[
\text{relative character-line metric}
\quad+
\text{relative determinant transport}.
\]

## Source-authority boundary

The theorem supplies a universal line-metric model. Grothendieck must still
derive the actual theta/Tate character lines, their metrics, and the operator
amplitudes. The calculation does not assert that the adelic product formula
cancels the resulting anomaly; it states exactly what such a cancellation must
mean.

## Falsifiers

- A claimed metric potential with a nonzero unaccounted relative determinant
  amplitude.
- Character-erased determinant data used to infer \(A_e\).
- A loop whose signed \(a_e\) sum is nonzero under a claimed product formula.
- Tail anomalies that vanish pointwise but are not summable.
- Refitting \(P_v\) after perturbing one edge amplitude.
- Treating vacuum normalization as proof of transport unimodularity.

## Process calibration

Pre-objective: excitement 10/10, confidence 8/10, expected information gain
10/10. The aim was to choose and discriminate concrete source candidates for
Deutsch's global potential without manufacturing theta formulas.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Relative line metrics generate the twisted potential exactly, while
relative determinant amplitudes isolate the remaining source anomaly.
