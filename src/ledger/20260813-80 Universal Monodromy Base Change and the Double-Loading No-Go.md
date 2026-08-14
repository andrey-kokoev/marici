# Universal Monodromy Base Change and the Double-Loading No-Go

## Record

Date: 2026-08-13

Status: exact universal group-ring/base-change theorem, with a negative
typing result for the physical interpretation.  The polynomial effective
relation groupoid of entry 79 survives the formal substitution
\(X_{ra}\mapsto q_{ra}-1\), including all four overlap bridges, both internal
pentagon cones, the complete polygon boundary identities, deck covariance,
and the ordered-normal sign.  This does **not** construct the missing
Pochhammer/Cousin Beck--Chevalley transformation.  In the physical typing of
entry 38, the \(X_{ra}\) remain scalar occurrence coefficients while
\(q_E-1\) belongs to a separate normal Koszul factor.  Applying both
constructions to the same boundary direction would count its loading twice.

## Epistemic-graph relation

Entry 78 was admitted as the conjecture that the four overlap bridges are
rank-one excess-intersection classes:

    ev-000000000017-5518d0c0-db1f-40be-9edb-59b546ad49ab

The theorem/conjecture split below, its double-loading criticism, and its
next falsification test were subsequently admitted atomically as:

    ev-000000000018-f8b85833-5ac5-406a-bce5-7e6245b5f811

That second event records the algebraic and formal-monodromy statements as
claims, while retaining the geometric excess-line realization as a
conjecture.  Its review gate explicitly records `certifies_truth: false`.

Entry 79 proves the algebraic rank, primitive
\((X_{11},-X_{10})\) boundary, and saturated support-cycle gluing.  The
present result adds a proved formal monodromy child but leaves the geometric
provenance child open.  More precisely:

1. **proved:** the entire support-selected algebra has a universal
   \(q-1\) base change;
2. **not proved:** those formal \(q-1\) variables are the single normal
   factors supplied by an actual scalar specialization/Pochhammer
   correspondence;
3. **still falsifying:** failure of the relative cotangent complex to have
   rank one, failure of a loaded five-term Cousin identity, or nontrivial
   finite holonomy around the four-chart cycle.

Admission continues to certify only the validity of the conjectural graph
node, not the unresolved geometric claim.

## Universal monodromy coefficient ring

For six independent universal monodromies, put

\[
q_{ra}=\exp(2\pi i\alpha' s_{ra}),
\qquad
u_{ra}=q_{ra}-1,
\]

and work first over

\[
R_0
=
\mathbf Z[u_{00},u_{01},u_{10},u_{11},u_{20},u_{21}].
\]

The universal rank-one local-system group ring is the flat localization

\[
\Lambda
=
R_0[(1+u_{ra})^{-1}]
\cong
\mathbf Z[q_{ra}^{\pm1}].
\]

Further inversion of the \(u_{ra}\) imposes nonresonance.  It preserves split
exact sequences, but it also makes every labelled monomial ideal the unit
ideal.  Therefore the physical support poset must be retained independently:

\[
\boxed{
\text{nonresonant coefficient localization does not remember support.}
}
\]

If the six physical \(s_{ra}\) obey an integer-linear relation
\(\sum n_{ra}s_{ra}=0\), then the actual monodromies obey

\[
\prod q_{ra}^{n_{ra}}=1.
\]

The theorem below is universal before imposing such a quotient.  Any physical
specialization with additional multiplicative relations must be audited in
the corresponding quotient ring.

## Formal loaded overlap theorem

Apply the coefficient substitution

\[
\varphi:R_X\longrightarrow R_0,
\qquad
X_{ra}\longmapsto u_{ra}.
\]

Every lcm-labelled cellular differential, ideal intersection, and carrier map
of entry 79 base-changes along \(\varphi\).  For a support-adjacent pair,

\[
J_e^{u}
=
C_e(u_{10},u_{11}),
\]

and its primitive interval resolution is

\[
\boxed{
d h_e
=
u_{11}e_{v^1}-u_{10}e_{v^0}.
}
\]

All four adjacent overlaps have this form.  The two opposite facet pairs
still have nonzero coefficient-ideal intersections, but remain absent from
the physical support nerve.

The support hyper--Cech sequence remains cellwise split exact over \(R_0\),
over \(\Lambda\), and after nonresonant localization:

\[
0
\longrightarrow
\bigoplus_{e\in C_4}K_e^{u}
\longrightarrow
\bigoplus_{i=0}^{3}K_{F_i}^{u}
\longrightarrow
B_Q^{u}
\longrightarrow0.
\]

Its shifted total differential squares to zero.  The actual formal route
carriers also remain chain maps:

1. each pentagon satisfies its complete five-edge boundary identity;
2. exactly one edge of each pentagon collapses, giving the two separate
   \(H_{s,+}\) and \(H_{s,-}\) cones;
3. each square satisfies its four-edge identity;
4. the eight outer-square deck symmetries preserve the construction;
5. exchanging the two ordered outer normals produces the Koszul sign;
6. the four literal formal transition ratios have product one.

This is a genuine algebra theorem.  It shows that there is no additional
combinatorial or integral obstruction to a monodromic deformation of the
entry-79 relation groupoid.

## Completed-coordinate interpretation

At fixed nonzero \(\alpha'\), define

\[
\mu_{ra}
=
\frac{q_{ra}-1}{2\pi i\alpha'}
=
X_{ra}\,
\frac{\exp(2\pi i\alpha'X_{ra})-1}
{2\pi i\alpha'X_{ra}}.
\]

The second factor is an analytic unit with constant term one.  In the
completed coefficient ring, the \(\mu\)-complex is therefore unit-conjugate
to the \(X\)-complex and has the latter as its nearby-cycle associated grade.
This explains why the formal deformation is exact and why it introduces no
new torsion.

It does **not** identify the formal deformation with the physical loaded
comparison.

## The double-loading no-go

Entry 38 types the physical facewise comparison as

\[
[F;\mu]
\longmapsto
\mu(X)\otimes\mathbb P_{\alpha'}(F).
\]

Here:

- \(\mu(X)\) is the scalar occurrence/contact coefficient;
- \(\mathbb P_{\alpha'}(F)\) contains the normal Pochhammer Koszul factor;
- the latter has differential \(q_E-1\) and contraction
  \((q_E-1)^{-1}\).

Thus the two appearances have different types:

\[
\boxed{
X_{ra}
\text{ belongs to the scalar coefficient resolution,}
\qquad
q_E-1
\text{ belongs to the worldsheet normal complex.}
}
\]

Replacing every scalar \(X_{ra}\) by \(q_{ra}-1\) and then tensoring with the
normal Pochhammer factor is not a lift of the entry-79 object.  It inserts two
copies of the same proposed boundary loading.  Consequently the formal
group-ring construction cannot be promoted by notation to

\[
\mathcal K_Q^{\alpha'}
=
\operatorname{hofib}
\left[
\bigoplus_i\operatorname{PC}_{\alpha'}(\mathcal U_i)
\longrightarrow
\operatorname{PC}_{\alpha'}(B_Q)
\right].
\]

The arrow in this formula remains the missing theorem.

## Why algebraic rank one is not yet geometric excess

The primitive syzygy proves that the support-selected algebraic overlap has
one relation.  It does not prove that an actual derived fiber product of
scalar specialization strata has a locally free rank-one excess cotangent
complex.

To make the excess-intersection interpretation literal one needs:

1. a scalar parameter or incidence space on which both the rank-jump
   specialization and the two physical cuts are defined;
2. the multi-normal deformation square comparing
   \(\operatorname{Cut}_{D,E}\operatorname{Sp}_R\) with
   \(\operatorname{Sp}_{R|D,E}\operatorname{Cut}_{D,E}\);
3. its relative cotangent triangle;
4. a proof that the excess term is a line on every support-adjacent overlap;
5. the corresponding monodromic Thom/Gysin class in the facewise
   Pochhammer/Cousin category;
6. compatibility of those four classes on the belt, both caps, and the cube.

Only then may the boundary

\[
(q_{11}-1)e_{v^1}-(q_{10}-1)e_{v^0}
\]

be interpreted as the unique normal factor of a physical excess line rather
than as a formal coefficient substitution.

## Finite holonomy remains a real falsifier

The formal carrier has exact four-cycle holonomy one.  The associated grade
therefore has no cycle obstruction.  An actual loaded transition can still
carry a tangential, collar, or orientation unit

\[
H(\alpha')=1+O(\alpha')
\]

which is invisible in the associated grade.  The physical test must compute

\[
\boxed{
H_Q
=
T_{30}^{\rm PC}T_{23}^{\rm PC}
T_{12}^{\rm PC}T_{01}^{\rm PC}
}
\]

and prove \(H_Q=1\) in the correctly oriented derived category.  Assuming
this from the polynomial result would erase exactly the first possible
finite-loaded obstruction.

## Epistemic boundary

Established:

1. universal \(X\mapsto q-1\) base change of the entry-79 algebra;
2. four primitive formal monodromy bridges;
3. split support hyper--Cech exactness after flat local-system localization;
4. both formal \(H_s\) cones and complete pentagon/square boundary identities;
5. deck covariance and ordered-normal Koszul antisymmetry;
6. exact formal transition holonomy one;
7. completed-coordinate unit conjugacy with the scalar associated grade;
8. the double-loading type mismatch with the physical construction of entry
   38.

Not established:

1. the actual scalar multi-normal deformation or specialization square;
2. a locally free rank-one geometric excess conormal complex;
3. a Pochhammer/Cousin Thom or Gysin transition between the disjoint route
   faces and regional belt;
4. tangential loading of the two scalar edges;
5. the physical five-term dependent pentagon identity;
6. trivial physical finite holonomy around the four-chart belt;
7. compatibility after imposing any unrecorded multiplicative monodromy
   relations;
8. global octagon/Jordan holonomy or identification with
   \((\operatorname{Pf}'A)^2\).

Reject:

> Formal substitution \(X\mapsto q-1\) proves the physical finite-loaded
> Pochhammer/Cousin comparison.

Also reject:

> The rank-one algebraic overlap syzygy by itself proves a rank-one geometric
> excess normal line.

## Next formula objective

Construct the actual multi-normal square and its relative cotangent complex:

\[
\begin{CD}
Z_{Q,R} @>>> Z_R\\
@VVV       @VVV\\
Z_Q @>>> Z,
\end{CD}
\qquad
\mathcal E_e
=
H^{-1}\mathbb L_{Z_{Q,R}/(Z_Q\times_Z Z_R)}.
\]

Test

\[
\operatorname{rank}\mathcal E_e=1
\]

and construct its single monodromic Thom factor so that

\[
\operatorname{gr}_V\operatorname{Th}_{\alpha'}(\mathcal E_e)
\simeq
K_e^{\rm w}.
\]

For one representative route pentagon, include its tangential loading and all
lower-face terms, verify the five-term Cousin identity, and compute the full
four-transition holonomy.  Rotate the resulting class through the eight deck
images only after this representative passes.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_finite_loaded_relation.rs
    rustc --edition=2021 -D warnings -O research/nima/check_finite_loaded_relation.rs -o "$env:TEMP\\marici-finite-loaded-relation.exe"
    & "$env:TEMP\\marici-finite-loaded-relation.exe"

Certificate SHA-256:

    44082fdb20af1fe0ceb8aa77c886b7f03a0da74ccb9b1a39b8858ffe748dd156

## Decision

Promote:

> The effective polynomial relation groupoid has an exact universal
> monodromy base change.  No new algebraic, integral, deck, or formal-cycle
> obstruction appears at this level.

Retain as the immediate frontier:

> Realize one and only one \(q-1\) normal factor as the Thom/Gysin class of a
> rank-one excess line in an actual scalar multi-normal specialization square,
> and test its dependent pentagon identity and finite holonomy.

## Internal dependencies

- Entry 38: physical separation of scalar coefficients and normal loading.
- Entries 76--79: regional cube, primitive half-line, carrier kernel, and
  resolved overlap theorem.
- research/nima/check_finite_loaded_relation.rs.
