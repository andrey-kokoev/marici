# Minimal product-parent fixed-point no-go: WP737

## Question

Does WP736's minimal diagonal product-group parent also fix the portal
magnitude through a perturbative interacting gauge-Yukawa fixed point?

## Executable parent matter packet

Use

\[
SU(2)_A\times SU(2)_B\times U(1)_Y\times SU(3)_c
\]

with all Standard Model left-handed doublets on the (A) site, the Higgs on
the (B) site, three vectorlike bifundamental fermions, and one complex
bifundamental link scalar. The unique portal Yukawa is the WP736 coupling
(kappa_U). This assignment has the Standard Model chiral anomaly
cancellations and an even number of doublets for the (SU(2)_A) Witten test;
the new fermions are vectorlike. A complete mediator sector for Standard Model
Yukawas is not included.

PyR@TE 3 at revision
`04b219c2016f3fc4f2371d72607edc26a7e06364` gives the one-loop gauge terms

\[
\beta_{g_1}^{(1)}=\frac{137}{6}g_1^3,
\qquad
\beta_{g_A}^{(1)}=g_A^3,
\qquad
\beta_{g_B}^{(1)}=-\frac{17}{6}g_B^3,
\qquad
\beta_{g_3}^{(1)}=-7g_3^3.
\]

Thus hypercharge and (SU(2)_A) require Yukawa-assisted ultraviolet zeros.
The parent Yukawa nullcline in squared rescaled couplings is

\[
15\alpha_\kappa
=\frac{15}{2}\alpha_1+9\alpha_A+\frac92\alpha_B.
\]

This is the maximal gauge-screening value of (alpha_\kappa). Adding the
nonnegative parent flavor Yukawa contributes positively to its beta function
and therefore lowers (alpha_\kappa) on the nullcline.

## Exact 210 obstruction

The two-loop gauge brackets before the Yukawa substitution are

\[
\begin{aligned}
P_1={}&\frac{137}{6}+\frac{1063}{18}\alpha_1
+\frac{44}{3}\alpha_3+39\alpha_A+\frac{75}{2}\alpha_B
-15\alpha_\kappa,\\
P_A={}&1+13\alpha_1+12\alpha_3+57\alpha_A+12\alpha_B
-6\alpha_\kappa.
\end{aligned}
\]

On the Yukawa nullcline they reduce exactly to

\[
\begin{aligned}
P_1|_{\beta_\kappa=0}
&=\frac{137}{6}+\frac{464}{9}\alpha_1
+\frac{44}{3}\alpha_3+30\alpha_A+33\alpha_B,\\
P_A|_{\beta_\kappa=0}
&=1+10\alpha_1+12\alpha_3
+\frac{267}{5}\alpha_A+\frac{51}{5}\alpha_B.
\end{aligned}
\]

Every coefficient is strictly positive. Hence neither required IR-free gauge
factor has a positive interacting zero anywhere in the nonnegative coupling
orthant. Since a nonnegative parent flavor Yukawa can only reduce
(alpha_\kappa), it makes both brackets larger and cannot repair the no-go.

## Disposition

The minimal product group supplies a hard-to-vary matching-scale sign and
Clebsch ratio, but not a magnitude selector or RG basin. It fails before
threshold and detector gates. Additional Yukawa-active matter could change the
two-loop gauge brackets, but it must be fixed by an independent anomaly-free
source grammar; adding representations until a zero appears would be tuning
the explanation at the matter-content level.

The smallest exact falsifier is the constant term of the reduced
(SU(2)_A) bracket:

\[
P_A\geq1.
\]

Any claimed positive fixed point of this minimal packet contradicts that
identity. A progressive successor must make at least one negative
source-derived contribution large enough to reverse this coefficientwise
positivity while keeping the Clebsch matching, link completion, perturbative
control, and anomaly cancellation.

Reproduce with:
`uv run --with sympy python research/flavor/checkers/wp737_minimal_product_parent_fixed_point_no_go.py`.

Generated result:
`results/wp737_minimal_product_parent_fixed_point_no_go.json`.
