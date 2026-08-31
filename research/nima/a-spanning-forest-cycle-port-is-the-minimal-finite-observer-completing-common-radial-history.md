# A spanning-forest cycle port is the minimal finite observer completing common radial history

## Question

What is the smallest additional observer that separates interval-cycle classes without restoring every shell and theta label?

## Claim boundary

On every finite fixed-ratio cutoff, the common-history kernel is the cycle space of a translated-interval graph. Choosing a spanning forest gives one coordinate per chord. Appending those chord coordinates makes common history faithful, and no lower-dimensional linear observer can do so.

## Fixed-ratio interval graph

Fix a ratio coordinate

\[
D=\log\frac mn.
\]

For every admitted shell-label tuple, absorb the forced half-density amplitude into its coefficient and associate the oriented edge

\[
e=[A_e,B_e],
\qquad
A_e=\log(np),
\qquad
B_e=\log(nq).
\]

For a finite cutoff, let \(G_D=(V_D,E_D)\) be the graph of all such translated endpoints and edges. Its chain space is

\[
C_1(G_D)=\mathbb C^{E_D}.
\]

Define the interval-coverage map

\[
J_Dc
=
\sum_{e\in E_D}c_e\mathbf1_{[A_e,B_e]}.
\]

The common radial history is the analytic transform

\[
B_Dc(t)
=
\int (J_Dc)(v)\Phi_1(v)\Phi_1(v+t+D)\,dv.
\]

## Exact cycle kernel

Distributional differentiation gives

\[
\partial_v(J_Dc)
=
\sum_e c_e(\delta_{A_e}-\delta_{B_e})
=-\partial_Gc,
\]

where \(\partial_G:C_1(G_D)\to C_0(G_D)\) is the graph boundary.

If \(J_Dc=0\), then \(\partial_Gc=0\). Conversely, if \(\partial_Gc=0\), then \(J_Dc\) is constant on the complement of its finite endpoint set; compact support forces that constant to be zero. Hence

\[
\ker J_D=\ker\partial_G=Z_1(G_D).
\]

The analytic transform is injective on finite step functions: a nonzero leftmost interval germ has a nonzero completed-theta separation asymptotic and cannot be cancelled by later support. Therefore

\[
\ker B_D=Z_1(G_D).
\]

The four-term multiplicative squares are elements of this cycle space.

## Spanning-forest observer

Choose a spanning forest \(T_D\subseteq G_D\). Every chord

\[
e\in E_D\setminus T_D
\]

determines one fundamental cycle. Let

\[
Z_D:C_1(G_D)
\longrightarrow
\mathbb C^{E_D\setminus T_D}
\]

record the chord coefficients after the standard tree-cycle decomposition.

Then \(Z_D\) is injective on \(Z_1(G_D)\). Consequently the augmented observer

\[
(B_D,Z_D)

:C_1(G_D)
\longrightarrow
\mathcal H_D
\oplus
\mathbb C^{E_D\setminus T_D}
\]

is injective.

## Minimality

For a graph with \(k_D\) connected components,

\[
\dim Z_1(G_D)
=|E_D|-|V_D|+k_D.
\]

Any linear observer appended to \(B_D\) must be injective on \(\ker B_D=Z_1(G_D)\). Its target dimension is therefore at least

\[
|E_D|-|V_D|+k_D.
\]

The chord port has exactly this dimension. It is minimal on the finite cutoff.

The spanning forest is a coordinate choice, not a canonical physical structure. The invariant object is the cycle-space quotient or, dually, a jointly faithful family on \(Z_1(G_D)\).

## Architecture consequence

A common-history G4 carrier need not retain the full shell-labelled packet. On each finite ratio block it can retain:

1. the common analytic history \(B_Dc\);
2. one cycle coordinate per independent interval loop.

This is strictly smaller than all edge labels whenever the graph has a large forest, yet it preserves the polarized source faithfully.

For projective completion, compatibility of forest choices and continuity of the cycle ports across cutoffs remain to be proved. Finite-cutoff minimality alone does not construct that limit.

## Disposition

The finite-cutoff observer problem is solved: common radial history plus a spanning-forest chord port is jointly faithful and dimension-minimal. The next depth-first issue is cutoff-natural projective completion of these cycle coordinates. No RH conclusion is authorized.
