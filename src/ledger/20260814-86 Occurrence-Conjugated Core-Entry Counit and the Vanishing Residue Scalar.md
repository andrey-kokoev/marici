# Occurrence-Conjugated Core-Entry Counit and the Vanishing Residue Scalar

## Record

Date: 2026-08-14

Epistemic-graph event:

    ev-000000000024-aafdfa94-1f08-45c1-b415-6ec7a6bc196b

Status: exact six-point construction.  The missing physical-core entry counit of entry 85 is
canonical on the occurrence-wise marked direct sum.  It is entry 32's physical coaction,
conjugated through the marked Catalan bijection of entry 26 and loaded by entry 38's ordered
normal Pochhammer factor.  Its apparent underdetermination arose only after quotienting the two
sink marks to one unmarked center-to-channel edge.

For one explicit edge the counit has two terms and primitive-dual period (2).  The two center
entries on either polarity sheet sum to (4g_4oxtimes g_4).  The plus and minus sums are
identical, so the six-point polarity-difference residue scalar is

\[
\boxed{\lambda_D=0.}
\]

The construction is exact at the occurrence and Laurent-grade levels.  As throughout entry 38,
literal tubular currents remain defined only up to filtered chain homotopy; the normal-cone/PC
class and its residue are canonical.

## Why entry 32 applies

At partial physical core (P=\varnothing), an occurrence still retains a latent full
quadrangulation (Q), its directed sink, and a sink mark.  Entry 26 gives the bijection

\[
\Phi_\epsilon:
(T,d)
\longleftrightarrow
[Q,\varnothing;d],
\]

where (T) is zero-core, (d) is a scalar mark, and (Q) is the unique full core reached by the
marked Catalan geodesic.  Therefore an edge (D\in Q) is already in the domain of entry 32's
map

\[
G_D:\mathcal L(\varnothing)\longrightarrow\mathcal L(\{D\}).
\]

The first geodesic edge which creates (D) in the scalar triangulation is not an independent
transverse scalar edge.  It does not need to be one: its coefficient specialization is obtained
by conjugating (G_D) through (\Phi_\epsilon).  This is precisely the occurrence-decorated
entry counit:

\[
\boxed{
\epsilon_D^{\mathrm{entry},\epsilon}
=
\chi_{D,\alpha'}\,G_D\,\Phi_\epsilon
}
\]

on the marked core-entry summand.  Here (\chi_{D,\alpha'}) means entry 38's facewise PC loading
on the resulting (D)-facet occurrence.  This formula does not descend termwise to the quotient
which forgets the sink mark; that quotient is the source of entry 85's free scalar.

## One explicit center-to-channel edge

Use

\[
D_0=(0,3),
\qquad
X_{D_0}=y_0.
\]

The two boundary quadrilaterals are

\[
L=(0,1,2,3),
\qquad
R=(0,3,4,5),
\]

with scalar slots

\[
(X_{02},X_{13})=(x_0,x_1),
\qquad
(X_{04},X_{35})=(x_4,x_3).
\]

Choose the plus-polarity even center

\[
E_{\rm even}=\{(0,2),(0,4),(2,4)\}
\]

and its mark (d=(0,4)).  The direct Catalan rule derives, rather than assumes, the unique
sink-compatible endpoint

\[
T_{\rm even}=\{(0,2),(0,3),(0,4)\},
\]

obtained by the flip

\[
(2,4)\longmapsto(0,3).
\]

For plus polarity the directed physical dual edge points from (L) to (R).  Thus (R) is the
old sink containing (d=(0,4)), while (L) is the new component whose two sink slots are
((0,2)) and ((1,3)).

Put

\[
u_{03}=q_{03}-1,
\qquad
h_{03}=\frac{\ell_{03}}{u_{03}},
\qquad
\widehat h_{03}=2\pi i\alpha' h_{03},
\]

and choose the ordered normal orientation

\[
\operatorname{or}(N_{03})=[dX_{03}].
\]

On the raw marked occurrence basis, the counit is

\[
\boxed{
\epsilon_{03}^{\mathrm{entry},+}[E_{\rm even};04]
=
-\widehat h_{03}
\left(
x_0[e_{02}\boxtimes e_{04}]
+x_1[e_{13}\boxtimes e_{04}]
\right)
\otimes[dX_{03}].
}
\]

The scalar associated-grade coefficient of the marked source is (-x_4).  After multiplying by
it and contracting the ordered normal factor in the residue, the selected edge contributes

\[
\boxed{
(x_0e_{02}+x_1e_{13})\boxtimes x_4e_{04}.
}
\]

The two minus signs have different proven origins: one is the zero-core scalar Laurent
coefficient (-X_d); the other is the physical coaction coefficient of entry 32.  Their product
is positive.

## Endpoint Cousin sign and normal loading

Let (L_{04}^{+}) denote the scalar flip edge between (E_{\rm even}) and
(T_{\rm even}).  The barycentric entry path is

\[
[E_{\rm even},b(L_{04}^{+})]
+[b(L_{04}^{+}),T_{\rm even}].
\]

With both edges oriented as written,

\[
\partial
\left(
[E_{\rm even},b(L_{04}^{+})]
+[b(L_{04}^{+}),T_{\rm even}]
\right)
=T_{\rm even}-E_{\rm even}.
\]

Hence the endpoint Cousin coefficient at (T_{\rm even}) is (+1).  Applying the entry counit
at that endpoint supplies

\[
-\widehat h_{03}(x_0e_{02}+x_1e_{13})\otimes[dX_{03}],
\]

including the forced coaction minus sign and no further incidence sign.  Reversing the ordered
normal convention reverses both (h_{03}\otimes[dX_{03}]) and the Gysin contraction, leaving the
paired residue scalar unchanged.

The scalar and normal variables remain separate:

\[
X_{03}=y_0,
\qquad
u_{03}=q_{03}-1.
\]

There is no substitution (y_0\mapsto u_{03}).  Entry 38 gives only the associated-grade
identity

\[
\operatorname{gr}^{-1}_{V_{03}}\widehat h_{03}=\frac1{y_0}.
\]

## Recovery of the actual (t^4) scalar Laurent grade

The individual source and endpoint grades are

\[
[t^4]E_{\rm even}=-(x_0+x_2+x_4),
\]

\[
[t^4]T_{\rm even}
=
\frac{x_0^2+x_0x_4+x_4^2}{y_0}.
\]

The second expression is not factorized.  Consequently the counit is not a map from one
unmarked scalar endpoint to one boundary monomial.  It is a map on the marked occurrence direct
sum.

Summing all four scalar refinements of the (D_0) facet gives exactly

\[
\boxed{
\sum_{T\supset D_0}[t^4]T
=
\frac{(x_0+x_1)(x_3+x_4)}{y_0}.
}
\]

The two plus-polarity marked entries split this sum by the old sink mark:

\[
\begin{aligned}
-x_4\,\epsilon_{03}^{\mathrm{entry},+}(e_{04})
&\xrightarrow{\operatorname{Res}_{03}}
(x_0e_{02}+x_1e_{13})\boxtimes x_4e_{04},\\
-x_3\,\epsilon_{03}^{\mathrm{entry},+}(e_{35})
&\xrightarrow{\operatorname{Res}_{03}}
(x_0e_{02}+x_1e_{13})\boxtimes x_3e_{35}.
\end{aligned}
\]

This is the occurrence-resolved scalar provenance which was absent from the aggregated tripod.

## Primitive-dual pairing

For the left and right weighted intervals define

\[
c_L=x_0e_{02}+x_1e_{13},
\qquad
c_R=x_4e_{04}+x_3e_{35}.
\]

Entry 77 gives

\[
[c_L]=2g_L,
\qquad
[c_R]=2g_R.
\]

The factorwise primitive duals are normalized by

\[
g_L^\vee(x_0e_{02})=g_L^\vee(x_1e_{13})=1,
\]

\[
g_R^\vee(x_4e_{04})=g_R^\vee(x_3e_{35})=1.
\]

They annihilate the exact weighted interval boundaries

\[
x_1e_{13}-x_0e_{02},
\qquad
x_4e_{04}-x_3e_{35}.
\]

Therefore the one explicit even-center entry has period

\[
\boxed{
(g_L^\vee\boxtimes g_R^\vee)
\left(c_L\boxtimes x_4e_{04}\right)=2.
}
\]

Adding the odd-center entry gives

\[
\operatorname{Res}_{03}^{+}
=c_L\boxtimes c_R
=4g_L\boxtimes g_R,
\]

and hence

\[
\boxed{
(g_L^\vee\boxtimes g_R^\vee)
(\operatorname{Res}_{03}^{+})=4.
}
\]

For minus polarity the old sink is (L), and entry 32 gives

\[
\epsilon_{03}^{\mathrm{entry},-}(e_{02})
=-\widehat h_{03}\,e_{02}\boxtimes c_R,
\]

\[
\epsilon_{03}^{\mathrm{entry},-}(e_{13})
=-\widehat h_{03}\,e_{13}\boxtimes c_R.
\]

Multiplying by the two source coefficients (-x_0,-x_1) gives the same result:

\[
\operatorname{Res}_{03}^{-}
=c_L\boxtimes c_R
=4g_L\boxtimes g_R.
\]

Thus

\[
\boxed{
\operatorname{Res}_{03}^{+}-\operatorname{Res}_{03}^{-}=0,
\qquad
\lambda_{03}=4-4=0.
}
\]

This is strict on the occurrence vector.  It implies the invariant null-homotopy statement after
passing to any filtered PC representative.

## Relation between the aggregate tripod and the marked scalar primitive

For the three channels (D_0,D_1,D_2), the canonical marked contact chain of entry 26 splits
into even- and odd-center tripods with coefficient vectors

\[
a^{\rm even}
=
(x_0-x_4,\ x_4-x_2,\ x_2-x_0),
\]

\[
a^{\rm odd}
=
(x_1-x_3,\ x_5-x_1,\ x_3-x_5).
\]

Both vectors sum to zero, and

\[
a^{\rm even}+a^{\rm odd}
=
\left(
x_0+x_1-x_3-x_4,
x_4+x_5-x_1-x_2,
x_2+x_3-x_5-x_0
\right),
\]

the complete QTDS polarity-difference vector.

Thus the scalar-derived primitive is the sum of two marked tripods with different coefficient
vectors.  It is not either unmarked tripod weighted by the full coefficient vector.  Forgetting
this decomposition permits addition of an arbitrary closed factorized boundary class and
produces entry 85's underdetermination.  Restoring scalar provenance selects the marked direct
sum and removes that freedom.

Accordingly, the counit is canonical on

\[
\bigoplus_{(T,d)}\mathbf k\,[T,d],
\]

not on a lone aggregated center edge after the mark (d) has been forgotten.

## Dihedral covariance

The executable audit transforms the explicit (D_0,+,04) map by all twelve elements of
(D_6).  For each transformed channel, it independently reconstructs the sink and source
quadrilaterals from alternating coorientation, finds the unique compatible polarity, and
compares both raw counit terms.

All comparisons agree exactly.  Reflections exchange the two sink marks, so one marked entry has
a twelve-element orbit.  After forgetting the sink mark this is the expected orbit of the three
channels and two polarity sheets.  The ordered normal line is transported as

\[
[dX_D]\longmapsto[dX_{gD}].
\]

Any alternative sign convention changes both the loaded normal and its Gysin dual and does not
change the scalar (0).

## Consequence

Entry 85's nonuniqueness statement remains correct for an arbitrary unmarked PC lift.  It is not
an obstruction to the scalar-derived marked lift.  On the occurrence-wise direct sum the maps of
entries 26, 32, and 38 compose, and the physical boundary residue of the six-point polarity
primitive vanishes.

Therefore the stated condition in entry 84 is satisfied:

\[
[\operatorname{Res}^{\rm PC}_{D}H_{6}^{\rm mark}]=0
\quad\text{for every }D.
\]

Together with (D_6) covariance, the one explicit calculation fixes every channel and sheet.
This removes the six-point residue condition from the proposed eight-point factorization
primitive.  It does not by itself solve the separate global atlas/Jordan coherence problem for
gluing the local primitive half-lines.

## Exact certificate

Run:

    rustfmt --check research/nima/check_six_point_core_entry_counit.rs
    rustc --edition=2021 -D warnings -O research/nima/check_six_point_core_entry_counit.rs -o "$env:TEMP\\marici-six-core-entry-counit.exe"
    & "$env:TEMP\\marici-six-core-entry-counit.exe"

The certificate verifies:

1. all fourteen scalar hexagon triangulations;
2. the direct Catalan source/endpoint rule for both centers, every mark, and both polarities;
3. the explicit (E_{\rm even}\to T_{\rm even}) edge and its retained mark;
4. every individual central and (D_0)-corner (t^4) grade used above;
5. the factorized sum of all four (D_0)-facet grades;
6. the two-term raw entry counit and both minus signs;
7. the endpoint incidence/Cousin sign;
8. the selected-edge primitive-dual period (2);
9. the plus and minus sheet periods (4) and their zero difference;
10. annihilation of the actual weighted interval differentials by the primitive duals;
11. exact covariance of the raw map under all twelve elements of (D_6).

Certificate SHA-256:

    7a0602f9559f85c0a5430ebc6730c1239be51c31e533f17a58bf64b059ec7e8d

## Decision

Reject:

> The scalar data leave the occurrence-decorated physical-core entry counit undetermined.

Retain the qualification:

> After forgetting the sink mark, a lone aggregated center-to-channel edge does not retain enough
> data to define the counit canonically.

Promote:

> On the marked occurrence direct sum, the core-entry counit is the physical coaction conjugated
> through the scalar Catalan bijection and equipped with the ordered PC normal loading.  One
> marked entry has primitive-dual period (2); one complete polarity sheet has period (4); the
> plus-minus residue scalar is (0).

## Internal dependencies

- Entries 20--21: six-point Laurent grades and presentation tripods.
- Entry 26: marked Catalan source/endpoint bijection and coefficient (-X_d).
- Entry 32: occurrence-wise physical coaction and its sign.
- Entry 38: normalized (h_D) loading, ordered normal line, and nearby-cycle grade.
- Entry 77: primitive weighted-interval generator and its dual normalization.
- Entries 83--85: fixed-mark PC descent, saturated tripods, and the quotient-level residue gap.
- `research/nima/check_six_point_core_entry_counit.rs`.
