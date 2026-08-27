# Vectorlike singlet–triplet additive portal source: WP729

## Question

Do known anomaly-free non-isomorphic messenger representations generate the
exchange-odd additive beta term required by WP728, rather than merely allowing
an asymmetric portal boundary value?

## Primary-source beta term

For the asymptotically safe flavor-portal models of arXiv:2008.08606v1, the
one-loop Higgs-portal beta function contains

\[
\beta_\delta^{(1)}
=\delta A-\frac13 I_\kappa\alpha_\kappa\alpha_y,
\]

where (A) collects the terms multiplying the portal. The second term is
additive: when both Yukawa coordinates are nonzero, (delta=0) is not an RG
fixed surface.

The paper gives

\[
I_\kappa^{A}=12,
\qquad
I_\kappa^{B}=9
\]

for its electroweak-singlet model A and electroweak-triplet model B. Both use
vector-like fermions, so each representation sector is free of chiral gauge
anomalies. Their non-isomorphic electroweak representations physically orient
the labels; exchanging them is not an automorphism of the gauge source.

## Ordered two-sector candidate

Introduce one portal coordinate for each representation-labelled scalar
sector and abbreviate

\[
q_A=\alpha_{\kappa A}\alpha_{yA},
\qquad
q_B=\alpha_{\kappa B}\alpha_{yB}.
\]

At zero portal, the one-loop source pair is

\[
(b_A,b_B)=(-4q_A,-3q_B),
\]

and its ordered contrast is

\[
b_A-b_B=-4q_A+3q_B.
\]

If a common source identity fixes (q_A=q_B=q>0), the additive contrast is
(-q). It is nonzero and its sign follows from the representation coefficients,
not from a portal boundary choice.

This common-product identity is not supplied by the audited paper. Without
it, the positive hostile ratio

\[
q_B=\frac43q_A
\]

cancels the contrast exactly. Therefore non-isomorphic representations make
an oriented source term possible but do not alone make it unavoidable.

## Local fixed-point completion

If the completed two-sector beta system reduces locally to

\[
\beta_A=\vartheta\delta_A-4q,
\qquad
\beta_B=\vartheta\delta_B-3q,
\qquad
\vartheta>0,
\]

then the unique fixed portal pair is

\[
(\delta_A^*,\delta_B^*)=
\left(\frac{4q}{\vartheta},\frac{3q}{\vartheta}\right),
\]

with positive ordered contrast (q/\vartheta). The two portal fluctuations
are irrelevant. If the same interacting source fixes (q) and
(artheta), sign and magnitude are predicted.

This is a conditional local completion. The source paper studies models A and
B separately. Their direct sum has additional allowed scalar cross-couplings,
gauge backreaction, and mixed stability-matrix entries. One may not combine
the published single-model coefficients and claim a completed two-sector
fixed point without deriving that enlarged beta system.

## Threshold and instrument boundary

The additive beta term repairs the operator-support problem more strongly than
a freely chosen portal: it makes zero portal non-invariant under RG whenever
the two Yukawa factors are nonzero. It does not establish finite threshold
survival. The two vector-like representations provide physical production and
decay labels, but no common-frame calibrated rank-two detector response for
the ordered portal pair has been derived.

## Disposition

WP729 finds the first primary-source-supported realization of WP728's required
exchange-odd affine beta mechanism. It is progressive but incomplete. The
smallest exact falsifier of representation-only selection is
(q_B=4q_A/3), which kills the contrast while keeping both Yukawa products
positive.

The next bounded calculation is the complete one-loop direct-sum beta system
for simultaneous A and B sectors, including every allowed scalar
cross-coupling. Acceptance requires an interacting fixed point with nonzero
contrast, positive contrast scaling exponent, no relevant deformation visible
in that contrast, and a stable scalar potential.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp729_vectorlike_singlet_triplet_additive_portal_source.py`

Generated result:
`results/wp729_vectorlike_singlet_triplet_additive_portal_source.json`.

Primary source: Hiller, Hormigos-Feliu, Litim, and Steudtner, *Model Building
from Asymptotic Safety with Higgs and Flavor Portals*, arXiv:2008.08606v1,
equation A.9 and table 8.
