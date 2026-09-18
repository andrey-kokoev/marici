# NMHV physical residues factor as oriented facet forms, not yet lower amplitudes

## Question

Does arbitrary-n physical-pole survival already imply normalized multiparticle factorization into lower-point superamplitudes?

## Claim boundary

No. The proved object is the momentum-twistor NMHV ratio-function chain. Its source-normalized residue is an oriented simplex-facet canonical form. Converting that form into a product or sum of lower-point amplitudes requires additional source conventions that are not contained in the five-bracket chain.

## Exact normalized residue

For an oriented five-bracket cell

$$
R_C=[v_0,v_1,v_2,v_3,v_4],
$$

let `P_k` be the facet obtained by deleting `v_k`. With the boundary convention

$$
\partial C
=
\sum_{k=0}^4(-1)^kP_k,
$$

the canonical-form normalization gives

$$
\operatorname{Res}_{P_k}R_C
=(-1)^k\Omega(P_k),
$$

where `Omega(P_k)` is the canonical form of the oriented tetrahedral facet. This equality fixes the residue sign and normalization; it is stronger than generic nonvanishing.

Every physical facet of the BCFW chain has incidence one. Hence, for its unique incident cell,

$$
\operatorname{Res}_{P}\mathcal A_n^{\rm NMHV}
=\pm\Omega(P),
$$

with the sign fixed by the explicit unpaired-facet list. Every spurious facet has two opposite copies of the same `Omega(P)` and cancels.

Thus codimension-one factorization is complete in the simplicial canonical-form category.

## Why lower-amplitude factorization is a different map

The expression `A_n^NMHV` used here is a ratio function built from dual-superconformal five-brackets. A physical scattering amplitude additionally involves:

1. the MHV superamplitude prefactor and its little-group normalization;
2. a declaration of which four-bracket boundary is multiparticle and which is collinear in the chosen kinematic chart;
3. the on-shell internal-state gluing measure;
4. the map from a tetrahedral momentum-twistor facet to the two lower-point kinematic spaces;
5. the convention distributing NMHV degree between the two sides.

None is determined by incidence-one or by the six-term identity. In particular, writing a facet form as a lower-amplitude product without the gluing map would conflate a canonical-form residue with a physical factorization residue.

## Acceptance test for physical promotion

For one generic channel, a source-complete promotion must provide a commuting square

$$
\begin{array}{ccc}
\mathcal A_n^{\rm full} & \xrightarrow{\operatorname{Res}_P} &
\operatorname{Res}_P\mathcal A_n^{\rm full}\\
\downarrow && \downarrow\\
\mathcal A_L\otimes\mathcal A_R & \xrightarrow{\text{internal-state gluing}} &
\text{channel form},
\end{array}
$$

with exact MHV prefactors, Grassmann degree, little-group weights, and orientation. It must distinguish multiparticle and collinear boundaries and reproduce the facet sign above.

## Disposition

The strongest current arbitrary-n theorem is:

> every physical NMHV BCFW boundary has the exactly normalized oriented facet residue `plus or minus Omega(P)`.

Normalized lower-amplitude factorization remains outside the declared ratio-function source. It should not be inferred from the completed boundary census. The next amplitude frontier must either supply the full-amplitude gluing conventions from a primary source or move to a different executable sector.
