# Rank-two moment-map partial repair: WP716

## Post-WP725 typing correction

The two-charge-vector construction below lives on a complexified or doubled
triplet carrier. It does not descend to one admitted real irreducible
\(SO(3)\) triplet, whose commuting orthogonal \(U(1)\) generator is exactly
zero. WP725 supplies the proof. The weighted charge-area identity remains an
exact conditional statement on the enlarged domain, but it is not a direct
repair of the original real-triplet flavor source.

## Question

Does the smallest extension of WP715 make the asymmetric portal unavoidable
while repairing strict stability, and does it thereby supply the requested
Deutschian explanation?

## Exact source construction

Take two independently gauged Abelian moment maps with positive weights:

\[
V_D=\frac12\sum_{a=1}^2G_a
\left(q_{na}|n|^2+q_{ma}|m|^2+q_{\chi a}\chi^2\right)^2,
\qquad G_a>0.
\]

Writing \(\langle u,v\rangle_G=\sum_aG_au_av_a\), the induced couplings are

\[
\lambda_n=\frac12\langle q_n,q_n\rangle_G,
\quad
\lambda_m=\frac12\langle q_m,q_m\rangle_G,
\quad
\lambda_x=\langle q_n,q_m\rangle_G,
\]

and

\[
g_n=\langle q_n,q_\chi\rangle_G,
\qquad
g_m=\langle q_m,q_\chi\rangle_G.
\]

The radial margin is the weighted Gram determinant:

\[
4\lambda_n\lambda_m-\lambda_x^2
=G_1G_2\det(q_n,q_m)^2.
\]

Thus linearly independent source charges repair the rank-one marginality of
WP715. The minimal integer witness

\[
q_n=(1,0),\qquad q_m=(0,1),\qquad q_\chi=(1,-1)
\]

forces

\[
g_n=G_1,qquad g_m=-G_2,qquad
4\lambda_n\lambda_m-\lambda_x^2=G_1G_2>0.
\]

This is real explanatory progress: after the charge geometry is declared,
the opposite portal signs and strict radial support cannot be varied
independently.

## Hostile gates

The construction is not the requested complete explanation.

First, a common gauge-metric rescaling \(G_a\mapsto sG_a\) preserves every
charge and incidence statement but sends

\[
g_n-g_m\longmapsto s(g_n-g_m).
\]

The absolute magnitude is therefore not fixed by rank-two charge geometry.

Second, both moment maps depend only on norms. They generate no
\((n\mathbin\cdot m)^2\) operator and hence no angular stiffness for the
faithful flavor frame.

Third, the low-energy quartic is not automatically a threshold-surviving
observable. If this is realized as a supersymmetric heavy-vector sector, the
ordinary decoupling limit can remove the additional D-term. A claimed
surviving portal must name a nondecoupling source, its soft scale, matching
map, finite-width support, and uncertainty domain.

Finally, a charge contrast is not itself an instrument. The readout must
preserve source incidence through labelled mediator channels or another
source-carried tag; a total unlabelled rate can collapse distinct allocations.

## Claim boundary and disposition

WP716 proves that rank two is sufficient for strict radial stability and can
force a relative portal sign using quantized charges. It does not fix the
absolute magnitude, the angular interaction, an RG-attractive basin,
threshold survival, or a calibrated physical readout.

The surviving source hypothesis is therefore narrower: seek a simple or
otherwise unified non-Abelian moment-map geometry whose invariant metric fixes
relative normalization and whose noncommuting generators produce angular
stiffness. It must still pass anomaly, complete RG, threshold, and instrument
tests. Merely adding a second adjustable Abelian gauge factor is a partial
repair, not the final Deutschian explanation.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp716_rank_two_moment_map_partial_repair.py`

Generated result: `results/wp716_rank_two_moment_map_partial_repair.json`.
