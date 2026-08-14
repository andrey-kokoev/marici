# Unfiltered Comparison and the Four Missing Overlap Bridges

## Record

Date: 2026-08-13

Status: exact polynomial comparison theorem and exact support obstruction at
eight points.  The ordinary derived comparison exists and is unique up to
homotopy.  The occurrence-only route Čech source does not carry the four
interval generators required to make that comparison land in the physical
four-facet belt.  Entry 79 proves that resolving the support-selected overlap
ideals, or equivalently taking the residual kernel of the actual polygon map,
supplies those generators canonically.  Only their finite-\(\alpha'\) loaded
scalar realization remains conditional.

Forward correction (entry 82): their target-first finite-loaded realization
is the composite of the completed scalar descent with the facewise PC map on
the actual regional cube.  What remains conditional is the stronger
route-first PC presentation and a comparison between the two orders.

This entry resolves the Hom-complex question posed in entries 76--77.  It
also changes the diagnosis of the remaining problem:

\[
\boxed{
\text{the obstruction is not derived lifting;
it is filtered geometric provenance.}
}
\]

## The actual four-chart diagram

Retain the representative physical rank-two core

\[
Q=\{03,05\}
\]

and the regional scalar cube

\[
K_Q=(02,13)\times(04,35)\times(06,57).
\]

Order the four marked route charts as

\[
\mathcal U_0=P_+,
\qquad
\mathcal U_1=P_-,
\qquad
\mathcal U_2=S_+,
\qquad
\mathcal U_3=S_-.
\]

Here \(P_\pm\) are copies of the actual route pentagon
\(P=\{13,35,57\}\), and \(S_\pm\) are copies of the actual companion square
\(S=\{02,04,06\}\).  Their established double-Gysin supports in the cube are

\[
P_+:x_2=1,
\qquad
P_-:x_0=1,
\qquad
S_+:x_2=0,
\qquad
S_-:x_0=0.
\]

Each chart contains four of the eight occurrence words
\(v\in\{0,1\}^3\).  Every occurrence belongs to exactly two charts.  The
nonempty chart intersections are

\[
(0,1),
\qquad
(0,3),
\qquad
(1,2),
\qquad
(2,3),
\]

and each contains exactly two occurrences.  These four pairs form a cycle.
In each pair the two occurrences differ only in the middle regional bit
\(v_1\), corresponding to the scalar refinement \((04,35)\).

The four raw-weighted maps from the actual route polygons to their indicated
cube facets are polynomial cellular chain maps.  Thus the problem is not a
failure of any individual chart map.

## The established Čech source has eight disconnected components

Let \(c_{i,v}\) denote the copy of occurrence \(v\) in chart
\(\mathcal U_i\).  For every nonempty pair \((i,j)\) and every occurrence
\(v\in\mathcal U_i\cap\mathcal U_j\), the established extension-by-zero
Čech differential has one column

\[
d u_{ij,v}=c_{j,v}-c_{i,v}.
\]

There are eight such columns: two for each of the four nonempty chart
intersections.  They identify duplicate copies of the same occurrence.  They
do not connect the two different occurrences in an intersection.

Equivalently, the degree-zero incidence graph has

\[
16\ \text{chart-occurrence copies},
\qquad
8\ \text{duplicate-identification edges},
\]

and is the disjoint union of eight two-vertex components, one component for
each \(v\in\{0,1\}^3\).

This is the exact source-side reason that an ordinary Čech totalization does
not yet see the interval overlaps of the target belt.

## The unfiltered polynomial augmentation exists

Let

\[
A=\mathbf Z[X_{00},X_{01},X_{10},X_{11},X_{20},X_{21}]
\]

and label occurrence \(v\) by its opposite monomial

\[
m_v=\prod_{r=0}^{2}X_{r,1-v_r}.
\]

Define on every chart copy

\[
\boxed{
a_Q(c_{i,v})=m_v.
}
\]

Every established Čech column is killed:

\[
a_Q(d u_{ij,v})=m_v-m_v=0.
\]

All eight minimal occurrence generators occur, so the image is precisely

\[
I_Q
=
\prod_{r=0}^{2}(X_{r0},X_{r1}).
\]

Therefore the route totalization admits a polynomial augmentation

\[
\boxed{
a_Q:
\mathcal C_Q^{\rm route}
\longrightarrow
I_Q[-2].
}
\]

No localization, division by two, or common scalar parent face is used.

Since \(\mathcal C_Q^{\rm route}\) is represented by the established
K-projective cellular totalization and

\[
\epsilon_Q:K_Q^{\rm w}\longrightarrow I_Q
\]

is the free cellular resolution of entry 76, the projective comparison
theorem gives a lift

\[
\widetilde a_Q:
\mathcal C_Q^{\rm route}
\longrightarrow
K_Q^{\rm w}[-2]
\]

which is unique up to chain homotopy after fixing the derived morphism
\(a_Q\).

Thus the unfiltered derived Hom problem is solved.  In particular, there is
no polynomial obstruction class to an abstract comparison with the full
regional cube.

## Why the unfiltered lift is not physical belt descent

The target of physical double Gysin is not the whole cube with its support
forgotten.  It is the four-facet belt

\[
B_Q^{\rm w}\subset K_Q^{\rm w}.
\]

The intersection of any adjacent pair of belt facets is a complete middle
interval.  Write its endpoints as

\[
v^0=(v_0,0,v_2),
\qquad
v^1=(v_0,1,v_2).
\]

The established source overlap supplies two duplicate columns, one at
\(v^0\) and one at \(v^1\), but no chain joining them.  Direct integral
incidence computation proves that the endpoint difference lies outside the
span of all eight established Čech columns.

Consequently an unfiltered lift may send every overlap generator to zero and
still represent the correct morphism into \(I_Q[-2]\).  It need not send a
source overlap to the corresponding target interval.  Forgetting the support
filtration has erased exactly the Beck--Chevalley datum we need.

This proves

\[
\boxed{
\operatorname{RHom}
(\mathcal C_Q^{\rm route},K_Q^{\rm w}[-2])
\text{ is too coarse to test factorization naturality.}
}
\]

## The four primitive missing syzygies

For each of the four adjacent chart pairs, order the two overlap occurrences
by their middle bit.  Then

\[
m_{v^0}=C_eX_{11},
\qquad
m_{v^1}=C_eX_{10}
\]

for the monomial \(C_e\) supplied by the two fixed outer regions.  Hence

\[
\boxed{
X_{11}m_{v^1}-X_{10}m_{v^0}=0.
}
\]

This is the unique primitive polynomial first syzygy joining the two
occurrence generators in that overlap.  It is exactly the boundary relation
of the middle weighted interval in \(K_Q^{\rm w}\):

\[
d h_e
=
X_{11}e_{v^1}-X_{10}e_{v^0}.
\]

After inserting the established raw occurrence anchors, the same equation
becomes

\[
d(\rho_eh_e)
=
w_{v^1}e_{v^1}-w_{v^0}e_{v^0},
\]

where \(\rho_e\) is the product of the two fixed outer raw weights.

Thus the coefficient and target data do not leave an arbitrary numerical
choice.  They specify four primitive interval relations, one for each edge
of the chart-overlap cycle.  What is missing is a source generator realizing
each relation.

Let \(E_\square\) be the four chart-overlap edges.  The minimal required
enhancement is schematically

\[
\widehat{\mathcal C}_Q^{\rm route}
=
\mathcal C_Q^{\rm route}
\langle b_e\mid e\in E_\square\rangle,
\]

where, modulo the already established duplicate-identification columns,

\[
d b_e
\equiv
X_{11}c_{e,v^1}-X_{10}c_{e,v^0},
\qquad
\widehat\beta_Q(b_e)=h_e.
\]

This formula describes the required filtered comparison.  It is not a
license to adjoin \(b_e\) formally.  Entry 79 subsequently proves that the
four generators are forced algebraically: they are the minimal resolutions
of the adjacent overlap ideals \(C_e(X_{10},X_{11})\) and the residual
saturated kernel of the actual polygon-to-belt map.  Scalar provenance now
means lifting that canonical polynomial relation complex to the loaded
Cousin or multi-normal boundary geometry.

## Forward correction: the resolved relation complex

Entry 79 constructs the minimal support-selected enhancement.  If
\(K_{F_i}^{\rm w}\) are the four facet resolutions and \(K_e^{\rm w}\) the
four adjacent interval resolutions, then

\[
0\to\bigoplus_eK_e^{\rm w}
\to\bigoplus_iK_{F_i}^{\rm w}
\to B_Q^{\rm w}\to0
\]

is split exact cell by cell over the polynomial ring.  Independently, the
actual polygon carrier has kernel ranks \((10,6,0)\); two interval summands
are the internal \(H_s\) cones, and their quotient is exactly the four
primitive bridge intervals.  All relation lattices are saturated.

Thus the four bridges are absent only from the occurrence-generator
truncation.  They are present canonically in the resolved support overlap.

## Uniqueness if the bridges exist

Let \(\lambda_i\) be the scalar multiplying the normalized chart map on
\(\mathcal U_i\).  The four bridge compatibilities form one connected
four-cycle.  Three independent equations together with the ordered-residue
normalization \(\lambda_0=1\) have coefficient matrix

\[
\begin{pmatrix}
1&-1&0&0\\
1&0&0&-1\\
0&1&-1&0\\
1&0&0&0
\end{pmatrix}
\]

of determinant \(\pm1\).  Therefore a bridge-supported completion, if
geometrically supplied, is normalized uniquely and saturated over
\(\mathbf Z\) and over \(A\).

The complete statement rotates through all eight deck images, and exchanging
the ordered physical normals supplies only the already known Koszul sign.

There is again no evidence for hidden torsion, an eighth-root normalization,
or a new free contact parameter.

## The scalar-edge cone is not a bridge

The internal pentagon scalar-edge cone

\[
H_s(15,37)
\]

maps to zero under supported double Gysin.  Both of its endpoint quotient
lines are killed.  Its labels also differ from the regional middle interval
\((04,35)\).

Hence \(H_s\) cannot supply any of the four missing overlap generators.  The
two roles remain distinct:

1. \(H_s\) implements the scalar-edge Cousin counit inside the pentagon;
2. \(b_e\) must implement dependent route-to-regional base change between
   charts.

## Interpretation

The mathematical pattern is now characteristic of a filtered or
constructible comparison:

\[
\text{underlying derived morphism exists}
\quad\not\Rightarrow\quad
\text{support-compatible natural transformation exists}.
\]

The four missing generators have the form of excess-Koszul intervals.  This
makes the proposed excess-intersection interpretation more concrete, but it
does not yet prove it.  An actual theorem must obtain the intervals from a
scalar deformation-to-the-normal-cone, loaded Pochhammer/Cousin
specialization, or equivalent intrinsic carrier.  A freely completed complex
would only restate the desired answer.

This is also the first precise sense in which the scalar half-object is a
homotopy-coherent dictionary rather than a strict operator on summed
amplitudes.  The local half-lines and their abstract derived comparison are
already present.  Factorization asks for specified paths between their
support charts.

## Epistemic boundary

Established:

1. all four actual route-polygon maps to the indicated belt facets are
   polynomial chain maps;
2. the established Čech source has sixteen chart-occurrence copies and eight
   duplicate columns, hence eight disconnected occurrence components;
3. \(c_{i,v}\mapsto m_v\) is a surjective polynomial augmentation onto
   \(I_Q\);
4. an unfiltered comparison lift into \(K_Q^{\rm w}\) exists and is unique up
   to homotopy;
5. belt support requires four additional middle-interval bridges absent from
   the established source incidence span;
6. each bridge has one unique primitive polynomial syzygy;
7. the normalized four-bridge compatibility problem is saturated with
   determinant \(\pm1\);
8. \(H_s(15,37)\) maps to zero and is not one of these bridges;
9. all statements are deck covariant and respect ordered-normal signs.
10. Entry 79 proves that the four bridges form the canonical resolved
    support-overlap relation complex, with no division by \(2\) or \(8\).

Not established:

1. a finite-\(\alpha'\) scalar-geometric lift of the now-canonical
   polynomial generators \(b_e\);
2. a loaded, support-filtered Beck--Chevalley transformation
   \(\widehat\beta_Q^{\alpha'}\);
3. finite-\(\alpha'\) Pochhammer/Cousin naturality on the dependent
   pentagon;
4. horizontal gluing around the full quadrangulation compatibility complex;
5. identification of the resulting global object with
   \((\operatorname{Pf}'A)^2\) in CHY cohomology.

Reject:

> The dependent route comparison is obstructed in ordinary derived Hom.

Also reject:

> The existing duplicate-occurrence Čech columns already represent the
> interval overlaps of the regional belt.

## Next formula objective

Entry 79 constructs the polynomial resolved overlap complex.  The next object
is its loaded lift

\[
\mathcal K_Q^{\alpha'}
=
\operatorname{hofib}\!\left[
\bigoplus_i\operatorname{PC}_{\alpha'}(\mathcal U_i;\mathcal L_i)
\longrightarrow
\operatorname{PC}_{\alpha'}(B_Q;I_Q)
\right]
\]

with associated grade

\[
\operatorname{gr}\mathcal K_Q^{\alpha'}
\simeq
(H_{s,+}\oplus H_{s,-})
\oplus\bigoplus_eK_e^{\rm w}.
\]

For one representative overlap, derive the primitive relation from the
loaded scalar specialization itself, rotate through the deck orbit, and
verify the five-term pentagon Cousin identity.

The falsification criterion is now sharp:

> If the scalar multi-normal or loaded Cousin geometry does not lift the
> certified polynomial relation complex, then the local half-lines possess
> polynomial effective descent but not a loaded factorization-natural scalar
> half-object.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_dependent_beck_chevalley_hom.rs
    rustc --edition=2021 -D warnings -O research/nima/check_dependent_beck_chevalley_hom.rs -o "$env:TEMP\\marici-dependent-bc.exe"
    & "$env:TEMP\\marici-dependent-bc.exe"

    rustfmt --check research/nima/check_resolved_overlap_hypercech.rs
    rustc --edition=2021 -D warnings -O research/nima/check_resolved_overlap_hypercech.rs -o "$env:TEMP\\marici-resolved-overlap-hypercech.exe"
    & "$env:TEMP\\marici-resolved-overlap-hypercech.exe"

Certificate SHA-256:

    21624eaf9e32a5eed00a2e0f79ce1c06e8bd60520bbc8a81db9d08dadc37a33b
    54294778b90b634c4bc542d93a1bc7273e52008a34da37ea06becd65ab554acf

## Decision

Promote:

> The dependent route source admits the required polynomial augmentation and
> therefore an unfiltered comparison with the scalar regional resolution,
> unique up to homotopy.

Retain as the immediate frontier:

> Lift the canonical polynomial overlap-relation complex of entry 79 to
> intrinsic loaded scalar boundary geometry and prove the five-term
> pentagon naturality identity.

## Internal dependencies

- Entry 38: facewise Pochhammer/Cousin symbols and the finite-loading gap.
- Entries 72--75: constructible route charts, belt support, and derived Hom.
- Entry 76: the actual regional cube, caps, and polynomial resolution.
- Entry 77: Alexander complement and the primitive boundary half-line.
- Entry 79: resolved overlap ideals and the effective relation groupoid.
- research/nima/check_dependent_beck_chevalley_hom.rs.
