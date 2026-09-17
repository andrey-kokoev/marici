# Physical cut preserves the source-pulled L/O graph

## Analytic form of one cut

For a physical edge `e` with sink slots `s_1,s_2`, the source cut coaction is the marked two-branch sum

\[
G_e=-T_{h_1}\otimes m_{s_1}-T_{h_2}\otimes m_{s_2},
\qquad h_j=s_j-e,
\]

where `T_h` is multiplication by the Laurent monomial `X^h` and the two marks land in distinct occurrence fibers.

Under the coefficientwise realization comparison, `T_h` becomes an admitted analytic multiplier `M_{chi_h}`. Thus

\[
U_4G_e
=-M_{\chi_{h_1}}U_4\otimes m_{s_1}
 -M_{\chi_{h_2}}U_4\otimes m_{s_2}.
\]

This is the required finite realization/cut intertwiner on the marked occurrence carrier.

## Compatibility with convolution successor

Analytic Laurent and Mellin multipliers commute:

\[
M_{m_a}M_{\chi_h}=M_{\chi_h}M_{m_a}.
\]

Therefore

\[
M_{m_a}U_4G_e=U_4G_eL_a
\]

branchwise, with the source expression interpreted using associativity and the transported mark. If the noncommutative source convention is retained, left and right successor orientations must be transported separately; the commutative scalar carrier used here identifies them.

## Compatibility with observation

Endpoint evaluation turns `M_{chi_h}` into the diagonal matrix

\[
D_h^\partial
=\operatorname{diag}(\chi_h(i/2),\chi_h(-i/2)).
\]

Hence

\[
\mathcal OU_4G_e
=-D_{h_1}^\partial\mathcal OU_4\otimes m_{s_1}
 -D_{h_2}^\partial\mathcal OU_4\otimes m_{s_2},
\]

and

\[
\mathcal OM_{m_a}U_4G_e
=-D_a^\partial D_{h_1}^\partial\mathcal OU_4\otimes m_{s_1}
 -D_a^\partial D_{h_2}^\partial\mathcal OU_4\otimes m_{s_2}.
\]

Thus every `L/O` graph coordinate after cutting is a bounded finite sum of retained coordinates before cutting.

## Continuity

For every admitted graph multiplier seminorm `mu`,

\[
\mu(M_{\chi_h}f)\le c_{h,\mu}\mu_h(f).
\]

The source Laurent estimate is

\[
q_\delta(T_hc)\le e^{\delta|h|_\lambda}q_\delta(c).
\]

Since one cut has two branches and a finite cut set has finitely many branches, these estimates prove continuity on the source-pulled `L/O` graph. Exact cut-order independence on finite packets extends by density. Consequently the mixed higher faces involving `R,C,L,O,V` commute strictly on the transverse marked occurrence carrier.

## Boundary

The theorem requires the cut Laurent characters to be admitted graph multipliers and uses the source-derived marked branch decomposition. It does not cover nontransverse loaded-current divisors or an output-only completion that forgets the branch marks. Sharp finite windows may still have boundary leakage; this does not affect projective graph-completion continuity.
