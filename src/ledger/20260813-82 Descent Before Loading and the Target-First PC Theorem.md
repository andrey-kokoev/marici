# Descent Before Loading and the Target-First PC Theorem

## Record

Date: 2026-08-13

Status: exact local eight-point composition theorem.  At the representative
rank-two core \(Q=\{03,05\}\), the finite-loaded scalar half-symbol is already
defined once the established operation order is respected:

\[
\boxed{
\mathsf J_Q^{\rm PC}
=
\chi_Q^{\rm PC}\circ j_Q\circ q_Q.
}
\]

Here \(q_Q\) is the support-derived scalar route-to-belt descent of entry 79,
\(j_Q\) includes the belt into the actual regional scalar cube of entry 76,
and \(\chi_Q^{\rm PC}\) is the facewise Pochhammer/Cousin map of entry 38.
Scalar descent occurs first; the result is loaded once, globally, on the
transverse regional target.

This composite supplies the loaded five-term pentagon identity, kills both
internal \(H_s\) cones, descends through all four determinant-overlap
relations, carries the ordered double-residue Koszul sign, is deck covariant,
and has target holonomy exactly one.

No route-first occurrence-decorated Pochhammer map, ambient comparison
homotopy, \(X\mapsto q-1\) substitution, or excess-normal line is required for
this theorem.

Forward correction (entry 83): the marked contact symbols close additively
around the residual octagon after the facewise PC map. The multiplicative
transition product proposed at the end of this entry is not intrinsically
typed: adjacent exact-core cubes are disjoint and are connected only by
noninvertible residue/Gysin spans through their shared rank-one core. The
surviving global problem is the additive correspondence totalization of the
unmarked/full-symbol summands.

## The operation-order correction

Entry 38 fixed the order

\[
\boxed{
\operatorname{Poch}_{\alpha'}
\circ
\operatorname{gr}_R,
}
\]

because exponentiating the scalar shift before taking its associated grade
creates an essential singularity in the scalar normal parameter.  The same
order applies to the dependent eight-point descent.

The previous frontier tried to construct a square comparing

\[
\text{load the dependent route charts first}
\quad\text{with}\quad
\text{descend first and load the regional target}.
\]

The left-hand operation is not currently defined on the complete
occurrence-decorated route complex.  More importantly, it is not needed to
define the physical normal symbol.  The scalar derived quotient must be
formed before the worldsheet regulator is applied.

Thus the correct conclusion is not that a missing Beck--Chevalley square has
silently been proved.  It is that this stronger, opposite-order comparison is
not a prerequisite for local loaded factorization naturality.

## The scalar descent object

Let \(K_{F_i}^{\rm w}\) be the four weighted regional facet resolutions and
let \(K_e^{\rm w}\) be the four determinant intervals resolving their
support-adjacent overlaps.  Entry 79 proves the strict, cellwise split exact
sequence

\[
0
\longrightarrow
\bigoplus_{e\in C_4}K_e^{\rm w}
\longrightarrow
\bigoplus_{i=0}^{3}K_{F_i}^{\rm w}
\xrightarrow{\ q_Q\ }
B_Q^{\rm w}
\longrightarrow0.
\]

Equivalently,

\[
\boxed{
\operatorname{Desc}_Q(\mathcal R_Q)
:=
\operatorname{cofib}\!\left[
\bigoplus_eK_e^{\rm w}
\longrightarrow
\bigoplus_iK_{F_i}^{\rm w}
\right]
\simeq B_Q^{\rm w}.
}
\]

The independent raw-polygon calculation gives the same quotient.  Its
saturated kernel has ranks \((10,6,0)\); two interval summands are
\(H_{s,+}\oplus H_{s,-}\), and the remaining four are exactly the overlap
determinant relations.

Therefore \(q_Q\) is not a guessed target projection.  It is the canonical
effective descent of the scalar route presentation, unique in the derived
category after the fixed orientation and normalization.

## The single loaded target

Entry 76 identifies

\[
K_Q^{\rm w}
=
K_0^{\rm w}\otimes K_1^{\rm w}\otimes K_2^{\rm w}
\]

with the weighted cellular complex of an actual fixed-core scalar face
\(K_Q\cong I^3\).  Its four physical side facets form

\[
B_Q^{\rm w}\subset K_Q^{\rm w}.
\]

For every actual regional cell \(F\), entry 38 and the weighted cellular
identity give

\[
\boxed{
\chi_Q^{\rm PC}[F;m_F]
=
m_F\otimes\mathbb P_{\alpha'}(F),
}
\]

with

\[
d_{\rm PC}\chi_Q^{\rm PC}
=
\chi_Q^{\rm PC}d_{\rm w}.
\]

The two kinds of coefficients remain separate:

- \(m_F\) is a scalar \(X\)-monomial in the lcm resolution;
- \(\mathbb P_{\alpha'}(F)\) contains the normal factors
  \(q_E-1\), their contractions, orientation lines, and all forced lower-face
  terms.

There is no \(X\mapsto q-1\) substitution.  Hence there is no double loading.

## Chain-map theorem

Each factor in

\[
\mathsf J_Q^{\rm PC}
=
\chi_Q^{\rm PC}j_Qq_Q
\]

is a chain map.  Therefore

\[
\begin{aligned}
d_{\rm PC}\mathsf J_Q^{\rm PC}
&=d_{\rm PC}\chi_Q^{\rm PC}j_Qq_Q\\
&=\chi_Q^{\rm PC}d_{\rm w}j_Qq_Q\\
&=\chi_Q^{\rm PC}j_Qq_Qd_{\rm route}\\
&=\mathsf J_Q^{\rm PC}d_{\rm route}.
\end{aligned}
\]

This short proof is consequential because every premise is now independently
established:

1. the route-polygon maps are polynomial chain maps;
2. their complete support relation complex is known;
3. the belt and cube consist of actual scalar faces;
4. the facewise PC map is a chain map on those transverse faces.

The theorem is not obtained by freely adjoining a homotopy.

## Loaded five-term pentagon identity

Let \(P\) be a route pentagon with oriented cellular boundary

\[
\partial P
=
\sum_{a=0}^{4}\epsilon_a e_a.
\]

Then

\[
\boxed{
d_{\rm PC}\mathsf J_Q^{\rm PC}(P)
=
\sum_{a=0}^{4}
\epsilon_a\mathsf J_Q^{\rm PC}(e_a).
}
\]

This is the requested loaded five-term identity.

The apparently missing terms are accounted for before loading:

1. the unique same-core scalar edge belongs to one of the two internal
   \(H_s\) cones and has zero \(q_Q\)-image;
2. the four physical edges descend to the four oriented edges of the
   corresponding regional facet;
3. the four inter-chart determinant intervals make that image independent
   of the chosen route representative;
4. all endpoint tubes and lower-face terms are already part of
   \(\mathbb P_{\alpha'}(F)\).

Thus the fifth term is killed by an admitted scalar relation before the
Pochhammer functor is applied; it is not discarded after evaluating the
amplitude.

## Physical residues

The facewise PC map is strongly monoidal on physical boundaries.  The scalar
descent respects the established double-Gysin supports, and the weighted
regional tensor carries the common normal factor

\[
-\kappa_D\kappa_E,
\qquad
\kappa_D
=
\frac{2\pi i\alpha'}{q_D-1}.
\]

Consequently

\[
\boxed{
\operatorname{Res}_{D,E}^{\rm PC}
\mathsf J_Q^{\rm PC}
=
-\kappa_D\kappa_E\,
\operatorname{pol}_Q^{\rm PC}.
}
\]

Exchanging the order of \(D\) and \(E\) reverses the oriented normal line:

\[
\operatorname{Res}_{E,D}^{\rm PC}
\mathsf J_Q^{\rm PC}
=
-
\operatorname{Res}_{D,E}^{\rm PC}
\mathsf J_Q^{\rm PC}.
\]

Both \(H_s\) endpoint quotient lines are killed by the supported double
Gysin map.  The four overlap relations are imposed before the residue is
taken.  Hence no unsupported state or extra normal factor appears.

## Holonomy

The normalized four-chart scalar descent has unit integral holonomy: its
compatibility matrix has determinant \(\pm1\), and the deck orbit closes with
the established orientation signs.  The target-first construction then
applies \(\chi_Q^{\rm PC}\) once on the single regional cube.

Therefore

\[
\boxed{
H_Q^{\rm target-first}=1.
}
\]

There are no four independent loaded chart-transition units whose product
could be \(1+O(\alpha')\).  This does not prove that a hypothetical
route-first current model has trivial transition holonomy.  It proves that
such transition data are absent from, and unnecessary for, the correctly
ordered construction.

## Representation independence

The actual route polygons and the resolved support hyper--Cech diagram are
two presentations of the same effective descent object.  Entry 79 identifies
their complete saturated relation complexes, and the local derived Hom has no
negative-degree ambiguity.  Consequently \(\mathsf J_Q^{\rm PC}\) depends on
the canonical descended belt class, not on one of the forty strict
pentagon-to-square representatives.

This is the appropriate local meaning of representation independence.  A
stronger equivalence with an independently loaded route presentation may be
scientifically useful, but it compares two constructions after both exist; it
does not define the present one.

## Epistemic-graph relation

Entry 81 introduced the successor conjecture

    conjecture:qtds-loaded-endpoint-determinant-kernel

after falsifying the excess-line typing.  The present target-first theorem
proves its local representative \(n=8\) realization in the facewise PC/Cousin
derived category, with the qualifications recorded below.

Epistemic-graph event:

    ev-000000000020-f7127d13-9401-4da3-ad85-3fc3b2b988a2

## Epistemic boundary

Established:

1. the correctly ordered local object is
   \(\mathsf J_Q^{\rm PC}=\chi_Q^{\rm PC}j_Qq_Q\);
2. it is a chain map in the canonical facewise PC/Cousin derived target;
3. scalar \(X\)-weights and Pochhammer \(q-1\) factors remain separately
   typed;
4. both \(H_s\) cones and all four determinant-overlap relations descend
   before loading;
5. the loaded five-term pentagon identity follows exactly;
6. the two ordered double residues differ by the Koszul sign;
7. the construction is covariant over the eight-element deck orbit;
8. target-first local holonomy is exactly one;
9. no division by \(2\) or \(8\) and no excess-normal factor occurs.

Not established:

1. an occurrence-decorated PC map on the dependent route charts before
   descent;
2. a comparison homotopy between such a route-first map and the target-first
   object;
3. a privileged tubular current, collar system, or smooth twisted form;
4. extension through resonance without retaining the filtered/nearby-cycle
   object;
5. horizontal assembly around the full quadrangulation compatibility
   complex;
6. vanishing of the residual octagon/Jordan holonomy;
7. the global all-chart identification with \((\operatorname{Pf}'A)^2\).

Reject:

> Loaded factorization naturality requires a rank-one excess Thom line.

Also reject:

> One must Pochhammer-load the dependent route presentation before taking
> scalar support descent.

Also reject:

> Failure to construct the stronger route-first comparison prevents the
> target-first normal symbol from being defined.

## Next formula objective

Entry 83 supersedes the transition-product objective. For adjacent cores
\(Q_i,Q_{i+1}\) sharing \(d_{i+1}\), retain the correspondence

\[
\operatorname{PC}(K_{Q_i})
\longrightarrow
\operatorname{PC}(K_{d_{i+1}})
\longleftarrow
\operatorname{PC}(K_{Q_{i+1}})
\]

with its occurrence coefficients, Gysin degrees, and normal orientation
lines. Assemble these spans over the Möbius compatibility carrier and compute
the additive full-symbol class

\[
\boxed{
[\Theta_{O,\rm full}^{\rm PC}]
\in
H^\bullet(\mathcal T_O^{\rm PC}).
}
\]

Its marked projection is zero by entry 83. The unmarked projection is the
remaining strict/null-homotopic/obstructed trichotomy.

Only after this horizontal test should the complete Parke--Taylor period
vector be evaluated and compared globally with
\([(\operatorname{Pf}'A)^2]\).

## Reproducible certificates

The theorem is a composition of previously certified maps; no new numerical
ansatz or checker is required.  Re-run its three bounded inputs:

    rustfmt --check research/nima/check_resolved_overlap_hypercech.rs
    rustc --edition=2021 -D warnings -O research/nima/check_resolved_overlap_hypercech.rs -o "$env:TEMP\\marici-resolved-overlap-hypercech.exe"
    & "$env:TEMP\\marici-resolved-overlap-hypercech.exe"

    rustfmt --check research/nima/check_decorated_source_cap.rs
    rustc --edition=2021 -D warnings -O research/nima/check_decorated_source_cap.rs -o "$env:TEMP\\marici-decorated-source-cap.exe"
    & "$env:TEMP\\marici-decorated-source-cap.exe"

    rustfmt --check research/nima/check_loaded_route_cube_gysin.rs
    rustc --edition=2021 -D warnings -O research/nima/check_loaded_route_cube_gysin.rs -o "$env:TEMP\\marici-loaded-route-cube.exe"
    & "$env:TEMP\\marici-loaded-route-cube.exe"

Certificate SHA-256 values:

    check_resolved_overlap_hypercech.rs
    54294778b90b634c4bc542d93a1bc7273e52008a34da37ea06becd65ab554acf

    check_decorated_source_cap.rs
    81828d55d754cb25acac89ef42abf02e709e2f3e67c1ede16a0e0fe714998556

    check_loaded_route_cube_gysin.rs
    f3489edc4e5017e4f39ecfcb9fc982e7af8c6234094ec22e219343d6661288ad

## Decision

Promote:

> At the first nontransverse eight-point stratum, scalar support descent
> followed by one facewise Pochhammer/Cousin loading produces a canonical,
> representation-independent local normal symbol with exact chain,
> factorization, deck, and holonomy properties.

Retain as the immediate frontier:

> Assemble the eight local target-first symbols horizontally and compute the
> residual octagon/Jordan obstruction before making a global eight-point
> claim.

## Internal dependencies

- Entry 38: order of operations and facewise PC/Cousin chain map.
- Entries 74--76: derived Gysin class, weighted cube, caps, and actual scalar
  target faces.
- Entries 78--79: route comparison, resolved support descent, and complete
  relation kernel.
- Entries 80--81: double-loading no-go and determinant, not excess, typing.
