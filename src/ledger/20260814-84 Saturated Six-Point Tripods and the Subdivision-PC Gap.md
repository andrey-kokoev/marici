# Saturated Six-Point Tripods and the Subdivision–PC Gap

## Record

Date: 2026-08-14

Status: exact six-point subdivision correction and a narrowed worldsheet gap.  The direct rule
which sends every barycentric simplex to the Pochhammer/Cousin summand of its maximal face is
not a chain map on all of \(C_*^{\rm simp}(\operatorname{sd}K_6)\) as presently defined in
entry 38.  Barycentric edges may skip face dimensions, whereas the established Cousin
differential uses only codimension-one face inclusions.

The entry-21 tripod contains exactly six such jumps.  Each has a unique rational,
\(D_6\)-equivariant saturated replacement: the half-sum of the two vertex--edge--facet flags in
the relevant square physical facet.  The repaired tripods have the exact required boundary and
use only codimension-one tangential/Cousin incidences.  Their physical residue-freeness is not
yet proved.  Consequently the proposed complete eight-point PC polarity primitive remains
conditional on a six-point occurrence/Gysin residue theorem, even though the coefficient-level
(G/R/K) decomposition has no additional unmarked remainder.

## Why the naive top-stratum rule fails

Let

\[
\sigma=[b(F_0),\ldots,b(F_k)]
\]

be an oriented simplex of the barycentric subdivision, with

\[
F_0<\cdots<F_k.
\]

Its relative interior lies in \(F_k^\circ\). In the simplicial boundary

\[
\partial\sigma
=
\sum_{j=0}^{k}(-1)^j
[b(F_0),\ldots,\widehat{b(F_j)},\ldots,b(F_k)],
\]

all terms with \(j<k\) retain top stratum \(F_k\) and are tangential. The term \(j=k\) has top
stratum \(F_{k-1}\) and must be the Cousin contribution.

This is compatible with entry 38 when

\[
\operatorname{codim}_{F_k}F_{k-1}=1.
\]

It is not compatible for a nonsaturated flag. Entry 38 defines
\(d_{\rm Cousin}\) as the signed sum over codimension-one face inclusions; it contains no direct
map which jumps two or more strata.  Assigning the last simplicial face directly to the deeper
stratum would silently add a higher exit-path specialization not present in the established PC
complex.

The six-point tripod makes this issue concrete.  Its last segment is

\[
[T_i,b(F_i)],
\]

where \(T_i\) is a vertex and \(F_i\) is a square facet. The face-dimension jump is two.
Therefore the direct maximal-stratum rule does not yet map the entry-21 tripod to entry 38's PC
complex.

## The saturated tripod replacement

Fix a corner \(T<F\) of a square facet. There are exactly two square edges

\[
T<E_0<F,
\qquad
T<E_1<F.
\]

Define

\[
\boxed{
\lambda_{T,F}
=
\frac12
\sum_{a=0}^{1}
\left(
[b(T),b(E_a)]
+
[b(E_a),b(F)]
\right).
}
\]

Each summand is a sequence of cover relations.  Its boundary is

\[
b(F)-b(T),
\]

so the same is true of (\lambda_{T,F}).

The coefficient is forced. The reflection fixing the corner/facet pair exchanges \(E_0\) and
\(E_1\). If their path weights are \(a,b\), equivariance gives \(a=b\), while the endpoint
boundary gives \(a+b=1\). Hence

\[
\boxed{a=b=\frac12.}
\]

There is no integral equivariant choice on the downstairs tripod.  The doubled chain is
integral, and the rational half-sum is canonical over the characteristic-zero nonresonant PC
coefficient field.

The replacement is explicitly homotopic to the original barycentric jump.  If

\[
\tau_a=[b(T),b(E_a),b(F)],
\qquad
j=[b(T),b(F)],
\]

then

\[
\partial\tau_a
=
\bigl([b(T),b(E_a)]+[b(E_a),b(F)]\bigr)-j.
\]

Consequently

\[
\boxed{
\lambda_{T,F}-j
=
\partial\left(\frac12(\tau_0+\tau_1)\right).
}
\]

The difference of the two integral saturated routes is likewise the boundary of

\[
\tau_0-\tau_1.
\]

Thus the half-sum selects a symmetric representative of an already explicit homotopy class.  A
strict zero statement after a tubular/current realization would not be invariant under this
representative freedom; the natural derived target is a specified null-homotopy.

Replace the last segment of every entry-21 leg by (\lambda_{T_i,F_i}).  Denote the resulting
leg by (\widetilde\gamma_i^\epsilon), and set

\[
\widetilde\eta_6^\epsilon
=
\sum_i c_i\widetilde\gamma_i^\epsilon,
\qquad
\sum_i c_i=0.
\]

Then

\[
\boxed{
\partial\widetilde\eta_6^\epsilon
=
\sum_i c_i b(F_i)
=
q_{6,+}-q_{6,-}.
}
\]

One-step rotation exchanges the two parity centers.  The saturated half-sum is equivariant under
all twelve elements of \(D_6\), including the reflections which force the averaging.

## PC typing on saturated edges

For a cover relation \(F_0\prec F_1\), orient the barycentric edge from \(b(F_0)\) to
\(b(F_1)\). Its boundary is

\[
\partial[b(F_0),b(F_1)]
=
b(F_1)-b(F_0).
\]

The first term is tangential in \(F_1^\circ\). The second is the unique codimension-one Cousin
face. If \(e\) is the new normal divisor, entry 38 supplies

\[
\partial_{\mathscr L}\ell_e=(q_e-1)p_e,
\qquad
h_e=\frac{\ell_e}{q_e-1}.
\]

Together with

\[
\operatorname{or}(N_{F_0})
\simeq
\operatorname{or}(N_e)\wedge\operatorname{or}(N_{F_1}),
\]

this fixes the Cousin sign and lower Pochhammer term.  Reordering two normal steps gives the
ordinary Koszul sign.  Thus entry 38's local normal-crossing construction applies termwise to
every edge of the saturated tripod without a cellular collapse or a higher-stratum jump.

This proves the boundary identity for the saturated PC image, up to the same filtered
chain-homotopy strength as the facewise normal-cone construction:

\[
\boxed{
d_{\rm PC}\,
\mathbb P^{\rm sat}_{\alpha'}
(\widetilde\eta_6^\epsilon)
=
\mathbb P^{\rm sat}_{\alpha'}
(q_{6,+}-q_{6,-}).
}
\]

It does not define a direct map on every nonsaturated simplex of
\(C_*^{\rm simp}(\operatorname{sd}K_6)\). A full such map requires a flag/exit-path PC
resolution and a filtered quasi-isomorphism from that resolution to entry 38's codimension-one
PC complex.

## The residue test remains open

Every repaired leg has four nonzero saturated edge terms supported inside its physical square
facet.  Therefore residue-freeness does not follow from the simplicial boundary or from support.
One must compute the occurrence-decorated Gysin image, including the term where the leg first
enters the physical facet and the lower normal-Koszul terms.

Entry 85 sharpens the required statement.  Literal chain-level vanishing depends on the chosen
flag/collar representative.  The invariant requirement is

\[
\boxed{
\operatorname{Res}^{\rm PC}_{D}
\mathbb P^{\rm sat}_{\alpha'}
(\widetilde\eta_6^\epsilon)
=d_{\rm PC}s_D^\epsilon,
\qquad
\text{equivalently }[\operatorname{Res}^{\rm PC}_{D}
\mathbb P^{\rm sat}_{\alpha'}(\widetilde\eta_6^\epsilon)]=0.
}
\]

Entries 32 and 37 prove strict physical coaction and transverse scalar base change.  They do not
directly prove this formula: the first tripod segment entering (F_D) changes the physical core,
and is not an independent transverse scalar-refinement edge.  The finite audit therefore does
not encode the residue as zero.

## Consequence for the eight-point decomposition

Entry 23 proves the exhaustive pole-grade decomposition

\[
q_Q^\epsilon
=
G_Q+
\sum_{D\in Q}R_{Q,D}^\epsilon
+K_Q^\epsilon.
\]

It follows that there is no fourth, unmarked coefficient sector in the eight-point polarity
difference:

1. \(G_Q\) is polarity independent;
2. the \(R\)-difference is supported entirely on the eight physical factorization triangles;
3. the \(K\)-difference is the marked contact boundary closed by entries 24 and 83.

Formally the desired primitive is

\[
H_8^{\rm PC}
=
\sum_D
G_D^{\rm PC}
(\widetilde\eta_6^{\rm PC})
+
H_{\rm ct}^{\rm PC}.
\]

Its coefficient-level boundary is exactly

\[
\sum_Q(q_Q^+-q_Q^-).
\]

The marked second term is already a residue-free PC chain.  The first term becomes a proved PC
factorization primitive only after the displayed six-point residue class is shown to vanish.
Accordingly:

> The proposed unmarked octagonal remainder is absent from the exhaustive polarity comparison,
> but the complete PC polarity homotopy is still conditional on the six-point residue map.

This does not settle the stronger problem of gluing the primitive local half-lines (g_Q), nor
does it construct a global Jordan-valued square or octagonal higher-coherence cell.  The bare
Möbius (H_1) may still govern that distinct atlas problem.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_six_point_subdivision_pc.rs
    rustc --edition=2021 -D warnings -O research/nima/check_six_point_subdivision_pc.rs -o "$env:TEMP\\marici-six-subdivision-pc.exe"
    & "$env:TEMP\\marici-six-subdivision-pc.exe"

The checker verifies:

1. all fourteen hexagon triangulations;
2. both parity centers and all three square physical facets;
3. all six original codimension-two tripod jumps;
4. the two saturated flags at every corner/facet pair;
5. uniqueness of the rational weights (1/2,1/2);
6. the exact tripod boundary for a general sum-zero coefficient vector;
7. covariance under all twelve \(D_6\) elements;
8. nonzero physical-facet support of every saturated tail.

Certificate SHA-256:

    46021191c34034bf4cd64f5f80e6fe9f0fb39316f86b263fdfeaae9785a310d4

## Decision

Reject:

> Every barycentric simplex maps directly to entry 38's PC complex merely by assigning it to its
> maximal face.

Promote:

> The six-point scalar tripods possess a unique rational, dihedrally equivariant refinement into
> codimension-one face flags.  Entry 38's local Pochhammer/Cousin construction therefore gives
> them a correctly typed saturated PC boundary.

Retain as the immediate bounded frontier:

> Compute the occurrence-decorated physical residue of one saturated tripod leg, including the
> entry-face Cousin term and its normal Koszul contraction.  Rotate the result through the three
> channels and both sheets.  Entry 85 reduces its class to one scalar
> \(\lambda_D^\epsilon[g_4\boxtimes g_4]\); its vanishing, or an explicit null-homotopy, closes
> the full eight-point PC polarity primitive.

Epistemic-graph event:

    ev-000000000022-fee2a075-f030-4f1a-875a-5dd2f44bfded

## Internal dependencies

- Entry 21: barycentric scalar tripods.
- Entries 23--24: exhaustive (G/R/K) decomposition and marked contact primitive.
- Entries 32 and 37: strict physical coaction and transverse base change.
- Entry 38: facewise PC/Cousin complex and normal Koszul contractions.
- Entries 82--83: local target-first dependent coherence and marked loaded octagon.
- `research/nima/check_six_point_subdivision_pc.rs`.
