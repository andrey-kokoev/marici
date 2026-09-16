# The augmented four-presentation pyramid fillers are conditional on the missing fourth-chart inverse

## Question

Does the bounded augmented edge \(C_{41}^{\mathrm{aug}}\) extend to analytic fillers for every face and the full four-presentation pyramid?

## Claim boundary — corrected after interface audit

The transport calculation below is a valid conditional lemma: if four bounded source charts have bounded inverses on their essential images, all fillers are strict. The premise is not currently established for the fourth semilocal chart. Radial graph observability does not overcome the zero lower margin of the Euler-weighted labelled-to-analytic synthesis, and the common graph domain is missing.

## Four analytic charts

Let \(X=\mathsf{Obs}_S\) carry the admitted source graph norm and define

$$
S_1=\operatorname{id}_X,
\qquad
S_2=C_{12},
\qquad
S_3=C_{13},
\qquad
S_4=\widetilde q_4
=(q_4,\partial,\operatorname{tr}_0,D_{w_\infty}^+).
$$

Use the essential images

$$
E_i=\operatorname{im}S_i.
$$

The first three maps have their previously constructed bounded inverses on their images. A bounded inverse for \(S_4\) would require a labelled-source lower estimate. The derivative–endpoint–tail theorem supplies only a radial \(H^1\) lower estimate, so this premise remains open. Write

$$
R_i=S_i^{-1}:E_i\longrightarrow X.
$$

Thus

$$
R_iS_i=\operatorname{id}_X,
\qquad
S_iR_i=\operatorname{id}_{E_i}.
$$

## Transported analytic edges

For every ordered pair define

$$
C_{ij}^{\mathrm{aug}}=S_jR_i:E_i\longrightarrow E_j.
$$

Every edge is bounded, and

$$
C_{ji}^{\mathrm{aug}}C_{ij}^{\mathrm{aug}}
=S_iR_jS_jR_i
=S_iR_i
=\operatorname{id}_{E_i}.
$$

In particular,

$$
C_{41}^{\mathrm{aug}}=R_4,
\qquad
C_{14}^{\mathrm{aug}}=S_4,
$$

which agrees with the previously constructed fourth-to-source recovery.

## Triangular fillers

For any \(i,j,k\),

$$
C_{jk}^{\mathrm{aug}}C_{ij}^{\mathrm{aug}}
=S_kR_jS_jR_i
=S_kR_i
=C_{ik}^{\mathrm{aug}}.
$$

Hence every triangular face has a strict analytic filler. In particular,

$$
C_{13}C_{41}^{\mathrm{aug}}=C_{43}^{\mathrm{aug}},
\qquad
C_{12}C_{41}^{\mathrm{aug}}=C_{42}^{\mathrm{aug}},
$$

and

$$
C_{41}^{\mathrm{aug}}C_{14}^{\mathrm{aug}}=\operatorname{id}_X,
\qquad
C_{14}^{\mathrm{aug}}C_{41}^{\mathrm{aug}}=\operatorname{id}_{E_4}.
$$

## Tetrahedral filler

For four vertices \(i,j,k,\ell\), both parenthesized composites reduce to the same bounded operator:

$$
C_{k\ell}^{\mathrm{aug}}
\bigl(C_{jk}^{\mathrm{aug}}C_{ij}^{\mathrm{aug}}\bigr)
=
S_\ell R_i
=
\bigl(C_{k\ell}^{\mathrm{aug}}C_{jk}^{\mathrm{aug}}\bigr)
C_{ij}^{\mathrm{aug}}.
$$

Thus the boundary of the presentation tetrahedron has a strict three-dimensional analytic filler. No higher associator choice is needed on these essential images.

## Comparison boundary

This theorem constructs the coherent augmented system from the four source charts. If an edge was previously defined by an independent integral kernel, trace formula, or scattering operator, equality with \(S_jR_i\) must be checked through its source-rooted triangle. Such equality is known for the previously admitted observer-generated presentation maps but must not be inferred for an undeclared external realization.

## Disposition

Conditionally on a bounded fourth-chart inverse, the formulas produce all twelve bounded comparisons, six strict triangular fillers, and the strict tetrahedral filler. That hypothesis is not currently proved for any semilocal fourth-chart completion. Therefore the analytic pyramid is not closed; only the formal transport lemma is retained.