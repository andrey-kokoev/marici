# Charged-scalar messenger descent nonselection: WP726

## Question

Can anomaly-free charged messengers carry the representation asymmetry and
induce the required portal on the original real-triplet quotient without the
WP725 domain enlargement?

## Typed mediated source

Let a heavy charged scalar have field-dependent squared mass

\[
m^2=M^2+aR+bX,
\qquad
X=\chi^2.
\]

Here \(R=|n|^2\) for the first channel and \(R=|m|^2\) for the second.

The heavy field may carry gauge charge while \(n\), \(m\), and \(\chi\) remain
on their original real domain. Its determinant depends only on the neutral
real invariants \(R\) and \(X\), so the induced operation descends correctly.
Charged scalars add no chiral gauge anomaly.

## Exact one-loop curvature

For the scalar Coleman–Weinberg kernel

\[
F=m^4\left(\log\frac{m^2}{\mu^2}-\frac32\right),
\]

the mixed curvature at the origin is

\[
\left.\frac{\partial^2F}{\partial R\partial X}\right|_0
=2ab\log\frac{M^2}{\mu^2}.
\]

This proves radiative portal support on the real-triplet quotient. It does not
fix a physical sign: the finite curvature vanishes at \(\mu=M\) and changes
sign across that scale. The scale dependence is compensated by the
renormalized portal counterterm.

For separate species with representation multiplicities \(d_n,d_m\), the
loop contrast is proportional to

\[
d_na_nb_n\log\frac{M_n^2}{\mu^2}
-d_ma_mb_m\log\frac{M_m^2}{\mu^2}.
\]

Representation theory may fix the integers \(d_n,d_m\), but the vertex
products \(a_nb_n,a_mb_m\), mass ratios, and two renormalized boundary values
remain continuous. An allowed counterterm can cancel the total contrast at a
chosen scale exactly.

## Selector and readout verdict

Mediated charged-scalar descent repairs WP725's carrier defect and makes portal
support unavoidable once the vertices are admitted. It does not make the
portal value unavoidable. It is an operator-support rigidifier, not a
numerical selector.

The charged species labels could seed two detector ports. Algebraic labels are
not an instrument: production, decay, mixing, widths, backgrounds, and
calibration must retain rank two in one physical analysis.

## Progressive gate

A viable mediated realization must add all of the following before the loop
can carry selection authority:

1. a representation or gauge–Yukawa identity fixing every vertex product;
2. a fixed trajectory determining the relevant counterterm boundary;
3. complete boson, fermion, and gauge supertrace matching;
4. a scheme-independent nonzero contrast after threshold completion; and
5. an actual labelled detector response.

WP726 therefore preserves the clock-locked architecture only in mediated
form. It rules out the claim that messenger charge or multiplicity alone fixes
the portal sign and magnitude.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp726_charged_scalar_messenger_descent_nonselection.py`

Generated result: `results/wp726_charged_scalar_messenger_descent_nonselection.json`.
