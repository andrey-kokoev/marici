# Effective invisible residue is the correct naturality coefficient system

## Correction

The raw invisible space
\[
N_s=\ker J_s^*
\]
is not automatically a coefficient system for the horizontal-lift complex. Two prior assumptions must be made explicit:

1. every admitted feature transport satisfies \(R_\alpha N_s\subseteq N_t\);
2. every cutoff retraction is independently source-authorized, not inferred from a zero-padding inclusion.

Even after this typing check, raw invisibility is too coarse. Some vectors in \(N_s\) may be operationally undetectable by every authorized downstream constructor and are genuine gauge.

## Universal harmless gauge

Let \(\mathcal W_s\) be the family of all authorized downstream wiring maps whose domain contains \(N_s\). Define
\[
G_s=\bigcap_{W\in\mathcal W_s}\ker(W|_{N_s}).
\]
Then \(G_s\) is the universally harmless residue. The effective invisible-residue module is
\[
E_s=N_s/G_s.
\]

This quotient is valid as a transported coefficient system only if
\[
R_\alpha N_s\subseteq N_t
\quad\text{and}\quad
R_\alpha G_s\subseteq G_t
\]
for every admitted arrow \(\alpha:s\to t\). These are constructor obligations, not consequences of scalar synthesis naturality.

An infinite-dimensional \(N_s\) can be harmless when \(E_s=0\). Conversely, a one-dimensional \(E_s\) can obstruct realization.

## Effective cocycle

Choose provisional full lifts \(\Lambda_s^0\). Their defects are
\[
\omega_\alpha
=R_\alpha\Lambda_s^0-\Lambda_t^0C_\alpha.
\]
After the typing condition, \(\omega_\alpha\) takes values in \(N_t\). Its operational content is
\[
\bar\omega_\alpha=[\omega_\alpha]\in
\operatorname{Hom}(A_s,E_t).
\]

Corrections \(T_s:A_s\to N_s\) induce effective corrections
\[
\bar T_s:A_s\to E_s,
\]
and
\[
\bar\omega_\alpha\mapsto
\bar\omega_\alpha+\bar R_\alpha\bar T_s-\bar T_tC_\alpha.
\]

Thus the realization invariant is the cohomology class
\[
[\bar\omega]\in H^1(\mathcal C;\operatorname{Hom}(A,E)).
\]
A source-valid horizontal realization requires this effective class to vanish. Raw vanishing in \(N\) is insufficient if the selected correction fails downstream compatibility.

## Refined classification

The correct three-way audit is now:

1. **Effective obstruction:** \([\bar\omega]\neq0\). No operationally valid horizontal lift exists.
2. **Effective torsor:** \([\bar\omega]=0\), but \(H^0(\mathcal C;\operatorname{Hom}(A,E))\neq0\). Realizations differ observably and need an additional constructor.
3. **Gauge uniqueness:** \([\bar\omega]=0\) and the effective \(H^0\) vanishes. Full lifts may still differ in \(G\), but all authorized downstream wiring identifies them.

Literal uniqueness in \(Z_s\) is unnecessary. Uniqueness modulo universal harmless gauge is the categorical requirement.

## Hostile model

Let
\[
Z=\mathbb C^3,\qquad J^*(z_1,z_2,z_3)=z_1,
\]
so
\[
N=\operatorname{span}(e_2,e_3).
\]
Let authorized wiring be
\[
W(z_1,z_2,z_3)=z_1+z_2.
\]
Then
\[
G=\operatorname{span}(e_3),\qquad E\cong\operatorname{span}([e_2]).
\]

The lifts
\[
\Lambda_{a,b}(c)=(c,ac,bc)
\]
all induce the same synthesis. Variation in \(b\) is genuine gauge; variation in \(a\) is effective residue.

Suppose a raw naturality correction uses \(e_2+e_3\) and cancels the defect in \(N\), but the transported correction is changed to \(e_3\) after an arrow. The raw complex can be made to appear exact by an unconstrained gauge choice, while the effective class retains \([e_2]\neq0\). The downstream wiring detects the failure.

## Relation to the weighted moving-seam control

The moving-seam interaction-net messages sharpen the interpretation. Bare geometric transport controls only the skeleton. A positive Adams coefficient supplies the arithmetic weight law, and grade-dependent primitive, square, and connected edges must remain separately typed.

Accordingly, the admitted transports \(R_\alpha\) must include both:

- horizontal geometric continuation between varying feature fibers;
- the positive typed coefficient obeying its semigroup law.

The fixed three-polarizer model is only the trivial-bundle, coefficient-one control. It demonstrates that scalar terminal observation forgets middle coupling, but it does not verify arithmetic transport or preservation of \(G\).

## Next finite-cutoff gate

For every generator and admitted arrow:

1. derive \(R_\alpha\) from source data;
2. verify \(R_\alpha N_s\subseteq N_t\);
3. inventory all authorized downstream wirings;
4. compute \(G_s\) and verify \(R_\alpha G_s\subseteq G_t\);
5. form \(E_s=N_s/G_s\);
6. compute the effective defect class and effective homogeneous torsor;
7. keep cutoff retractions absent unless independently constructed.

Only after this gate may the horizontal lift feed the compact Birman–Schwinger family. This prevents scalar domination from concealing an operationally visible continuation residue.
